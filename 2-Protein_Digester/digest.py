#!/usr/bin/env python 3
#

import re, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', type=str, default='dummy.fasta',
    help='the filename of .fasta file containing protein sequence(s)')
parser.add_argument('-e', '--enzyme',
    help='the name of an enzyme [t,l,a,e]', type=str, default='t')
parser.add_argument('-m','--missed', type=int,
    help='an integer value for number of missed cleavages[0-3]', default=0)
parser.add_argument('-o','--output', type=str,
    help='the output name of the file', default='output.fasta')
args=parser.parse_args()

def read_proteins(filename): #processes lines in .fasta file into a list of 2-tuples.
    proteins= []
    protein_name = ''
    sequence = ''
    for line in open(args.filename):
        if line.startswith('>'): #header lines in a .fasta file will always begin >
            if sequence:
                proteins.append((protein_name,sequence))
                sequence ='' #sequence is reset to an empty string for each new protein
            protein_name = line[1:-1] #removes first > and unwanted newline character at end of header line
        else: #any line not beginning > will be sequence in a .fasta file.
            line = line.rstrip('\n*')
            sequence += line #appends my sequence line to sequence
    proteins.append((protein_name,sequence))
    return proteins

#create a dictionary consisting of key = enzyme code, and value = cleavage pattern
recog_seq = {
            't' : re.compile('([KR])(?!P)'),
            'l' : re.compile('(K)(?!P)'),
            'a' : re.compile('(R)(?!P)'),
            'e' : re.compile('(E)(?!P)')
    }

def digest(sequence, enzyme):
    peptides = []
    pattern = recog_seq[args.enzyme]
    peptides_unpaired = re.split(pattern, sequence)
    peptide = zip(peptides_unpaired[::2], peptides_unpaired[1::2]) #run zip on seq_peptides to put pairs together.
    for i, j in peptide:
        full_peptide = i + j
        peptides.append(full_peptide)
    if peptides_unpaired[-1]: #if the cleavage site is not at the end of the protein, zip will leave off the final peptide.
        peptides.append(peptides_unpaired[-1])
    return peptides

def missed(peptides, missed):
    peptides_to_add=[]
    peptides_missed = []
    if args.missed ==0:
        for peptide in peptides:
            peptides_missed.append(peptide)
    else:
        for n in range(1, args.missed + 2):
            for i in range(len(peptides) - n + 1):
                peptides_to_add=(peptides[i:i+n])
                print(peptides_to_add, i, n)
                ''.join(peptides_to_add)
    return peptides_missed

output=open(f'{args.output}','w')
proteins = read_proteins(args.filename)
for name, sequence in proteins:
    peptides = digest(sequence, args.enzyme) #It's a list of lists!!!!
    peptides_missed=missed(peptides, args.missed)
    peptide_num=0
    for peptide in peptides_missed: #for loop to transfer list of dictionaries into .fasta format
        peptide_num+=1
        print(f">{name}\t{peptide_num}\tmissed={args.missed}\t{args.enzyme}\n{peptide}", file =output)

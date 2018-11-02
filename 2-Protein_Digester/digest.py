#SATURDAY
#FIX BUG FOUND - REPEATED OUTPUT.
#to-do: implement shebang
#to-do: implement missed cleavages
#error trapping, warnings, reporting.
#sensible variable names

#!/usr/bin/env python 3
#
import re, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--filename', type=str, default='dummy.fasta',
    help='the filename of .fasta file containing protein sequence(s)')
parser.add_argument('-e', '--enzyme',
    help='the name of an enzyme [t,l,a,e]', type=str, default='t')
parser.add_argument('-m','--missed', type=int,
    help='an integer value for number of missed cleavages[0-3]', default=0)
parser.add_argument('-o','--output', type=str,
    help='the output name of the file', default='output.fasta')
args=parser.parse_args()

def read_proteins(input): #processing task 1: process lines in .fasta file into a list of 2-tuples.
    proteins= []
    protein_name = ''
    sequence = ''
    for line in open(args.filename):
        if line.startswith('>'):
            if sequence:
                proteins.append((protein_name,sequence))
                sequence =''
            protein_name = line[1:-1] #remove newline character at end
        else:
            line = line.rstrip('\n*')
            sequence += line #append my sequence line to sequence
    proteins.append((protein_name,sequence)) #p-to-do: could change to handle malformed files here
    return proteins

proteins = read_proteins(args.filename)

#create a dictionary consisting of key = enzyme code, and value = cleavage pattern
recog_seq = {
            't' : re.compile('([KR])(?!P)'),
            'l' : re.compile('(K)(?!P)'),
            'a' : re.compile('(R)(?!P)'),
            'e' : re.compile('(E)(?!P)')
    }

def digest(proteins, enzyme):
    peptides = []
    pattern = recog_seq[args.enzyme]
    for name, sequence in proteins:
        full_peptides=[]
        peptide_num = 0
        peptides_unpaired = re.split(pattern, sequence)
        peptide = zip(peptides_unpaired[::2], peptides_unpaired[1::2]) #run zip on seq_peptides to put pairs together.
        for i, j in peptide:
            full_peptide = i + j
            full_peptides.append(full_peptide)
        if peptides_unpaired[-1]: #if the cleavage site is not at the end of the protein, zip will leave off the final peptide.
            full_peptides.append(peptides_unpaired[-1])
        for peptide in full_peptides:
            peptide_num += 1 #seq_peptides.len gives length
            peptides.append({'name': name, 'peptide_num': peptide_num, 'peptide': peptide})
    return peptides

peptides = digest(proteins, args.enzyme) #It's a list of dictionaries!!!!

#def missed(proteins, missed):
#    peptides_missed = []
#    for peptide in peptides:
#        peptides_missed.append(peptides[1], peptides[2], peptides[1]+peptides[2])
#    return peptides_missed

#peptides_missed=missed(proteins,args.missed)
#print(peptides_missed)

output=open(f'{args.output}','w')
for peptide in peptides: #for loop to transfer list of dictionaries into .fasta format
    print(f">{peptide['name']}\t{peptide['peptide_num']}\t'missed={args.missed}'\t{args.enzyme}\n{peptide['peptide']}", file =output)

#bonus task 1 (missed cleavages):
#list for 1 missed cleavage will look like:
#peptide 1 + peptide 2 + peptide 3 (1+2) + peptide 4 + peptide 5 (2+4) + peptide 6 + peptide 7 (4+6) + peptide 8 + peptide 9 (6+8)

#list for 2 missed cleavages will look like:
#peptide 1 + peptide 2 + peptide 3 (1+2) + peptide 4 + peptide 5 (3+4) + peptide 6 + peptide 7 (2)

#ensure Charles receives information in the form:
    #>ClAUD_F1_1 peptide 1 missed=2 enzyme t
    #GJAIGOEGKDGLLDGD

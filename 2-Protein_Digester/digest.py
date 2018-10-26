import sys
import re

#I want my command line input to look like:
    #python digest.py -enzyme foo.fasta

#To-do: use argparse module?
sys_argv1 = sys.argv[1]
enzyme = sys.argv[2]

def read_proteins(sys_argv1): #processing task 1: process lines in .fasta file into a list of 2-tuples.
    proteins= []
    protein_name = ''
    sequence = ''
    for line in open(sys_argv1):
        if line.startswith('>'):
            if sequence:
                proteins.append((protein_name,sequence))
                sequence =''
            protein_name = line[1:-1] #remove newline character at end
            #replace any whitespace in protein_name with _
        else:
            line = line.rstrip('\n')
            sequence += line #append my sequence line to sequence
    proteins.append((protein_name,sequence)) #p-to-do: could change to handle malformed files here
    return proteins

proteins = read_proteins(sys_argv1)

#create a dictionary consisting of key = enzyme code, and value = cleavage pattern
recog_seq = {
            't' : re.compile('([KR])(?!P)'),
            'l' : re.compile('(K)(?!P)'),
            'a' : re.compile('(R)(?!P)'),
            'e' : re.compile('(E)(?!P)')
    }

def digest(proteins, enzyme):
    full_peptides = []
    peptides = []
    peptide_num = 0
    pattern = recog_seq[enzyme]
    for name, sequence in proteins:
        peptides_unpaired = re.split(pattern, sequence)
        peptide = zip(peptides_unpaired[::2], peptides_unpaired[1::2]) #run zip on seq_peptides to put pairs together.
        for i, j in peptide:
            full_peptide = i + j
            full_peptides.append(full_peptide)
            for peptide in full_peptides:
                peptide_num += 1 #seq_peptides.len gives length
                peptides.append({'name': name, 'peptide_num': peptide_num, 'peptide': peptide})
    return peptides

peptides = digest(proteins, enzyme) #It's a list of dictionaries!!!!

output=open('output.fasta','w')
for peptide in peptides: #for loop to transfer list of dictionaries into .fasta format
    print(f">{peptide['name']}\t{peptide['peptide_num']}\t'missed=0'\t{enzyme}\n{peptide['peptide']}", file =output)

#bonus task 1 (cleavages):
#ensure Charles receives information in the form:
    #>protein_name peptide_num missed=int enzyme
    #'SEQUENCESTRING'

    #>ClAUD_F1_1 peptide 1 missed=2 enzyme t
    #GJAIGOEGKDGLLDGD

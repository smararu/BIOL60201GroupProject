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
            if sequence !='':
                proteins.append((protein_name,sequence))
                sequence =''
            protein_name = line[1:-1] #remove newline character at end
        else:
            line = line.strip('\n')
            sequence += line #append my sequence line to sequence
    proteins.append((protein_name,sequence)) #p-to-do: could change to handle malformed files here
    return proteins

proteins = read_proteins(sys_argv1)

#Create a function (e.g. digest) that can operate on my list of 2-tuples.

def digest(proteins, enzyme):
    peptides=[]
    peptide_num = 0
    i = 0
    if enzyme == 't':
        cleavage_start = 'R'
    if enzyme == 'l':
        cleavage_start = 'K'
    if enzyme == 'a':
        cleavage_start = 'K'
    if enzyme == 'e':
        cleavage_start = 'E'
    for protein in proteins:
        name = protein[0]
        sequence = protein[1]
        if cleavage_start in sequence:
            for ([i][1]) in proteins
                string =(proteins[i][1])
                print(string)
                peptide_num+=1
                print(f"> {proteins[i][0]} peptide {peptide_num} {enzyme}")
                i+= 1
    return

peptides = digest(proteins, enzyme)

#take first tuple in proteins
#scan along j (sequence), until a certain point, then split j!

#my sequences end in *
#if trypsin, identify first peptide at Lysine (K) or Arginine (R), and if the next amino acid is not Proline (P)
#save sequence up to that point as protein 1 peptide 1
#take remaining sequence and repeat process
#when all of protein 1 has been fragmented, move to protein 2 and repeat process
#when the list is finished, output all fragments to a file in fasta format (see Output format below)

#bonus task 1 (cleavages): ensure Charles receives information in the form:
    #>protein_name peptide_num missed=int 'N/I/C' enzyme
    #'SEQUENCESTRING'

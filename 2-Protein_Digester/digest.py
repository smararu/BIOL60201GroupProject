import sys
import re

#I want my command line input to look like:
    #python digest.py -enzyme foo.fasta

#To-do: use argparse module?
sys_argv1 = sys.argv[1]
sys_argv2 = sys.argv[2]

def read_proteins(sys_argv1): #processing task 1: process lines in .fasta file into a list of 2-tuples.
    proteins= []
    protein_name = ''
    sequence = ''
    for line in open(sys.argv[1]):
        if line.startswith('>'):
            sequence =''
            protein_name = line[1:-1] #remove newline character at end
        else:
            line = line.strip()
            sequence = line #append my sequence line to sequence
            proteins.append((protein_name,sequence))
    return proteins

proteins = read_proteins(sys_argv1)
print(proteins) #checks that the list of 2-tuples looks correct!

#Create a function (e.g. digest) that can operate on my list of 2-tuples.
def digest(proteins, enzyme): #defining a function called digest which takes arguments proteins and enzyme
    peptide_num = 1
        if enzyme = trypsin
        if enzyme =
        if enzyme =
        if enzyme =

digest(proteins, enzyme)

#my sequences start with > and end in *
#if trypsin, identify first peptide at Lysine (K) or Arginine (R), and if the next amino acid is not Proline (P)
#save sequence up to that point as protein 1 peptide 1
#take remaining sequence and repeat process
#when all of protein 1 has been fragmented, move to protein 2 and repeat process
#when the list is finished, output all fragments to a file in fasta format (see Output format below)

#bonus task 1 (cleavages): ensure Charles receives information in the form:
    #>protein_name peptide_num missed=int 'N/I/C' enzyme
    #'SEQUENCESTRING'

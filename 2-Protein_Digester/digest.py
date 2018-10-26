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
            't' : re.compile('[K|R]'),
            'l' : re.compile('K'),
            'a' : re.compile('R'),
            'e' : re.compile('E')
    }

def digest(proteins, enzyme):
    peptides=[]
    peptide_num = 0
    i = 0
    cleavage_start = recog_seq[enzyme]
    for name, sequence in proteins:
        seq_peptides=re.split(cleavage_start, sequence)
        for peptide in seq_peptides:
            peptide_num+=1 #seq_peptides.len gives length
            peptides.append({'name': name, 'peptide_num': peptide_num, 'peptide': peptide})
            #print(f"> {proteins[i][0]} peptide {peptide_num} {enzyme}") #add dict to peptides list
            i+= 1
    return peptides

peptides = digest(proteins, enzyme)
#It's a list of dictionaries!!!!

#for loop to transfer list of dictionaries into .fasta format
output=open('output.fasta','w')
output2=open('output2.fasta','w')
for peptide in peptides:
    print ('>%s\t%d\t%s\n%s' % (peptide['name'], peptide['peptide_num'], enzyme, peptide['peptide']), file=output)
    print(f">{peptide['name']}\t{peptide['peptide_num']}\t{enzyme}\n{peptide['peptide']}", file =output2)

#print(f"> {output_name} peptide {output_peptide_num} {output_peptide}")


#f"> {'name'} peptide {'peptide_num'} {'peptide'}")

#output_name = [d['name'] for d in peptides]
#output_peptide_num = [d['peptide_num'] for d in peptides]
#output_peptide = [d['peptide'] for d in peptides]


#my sequences end in *
#if trypsin, identify first peptide at Lysine (K) or Arginine (R), and if the next amino acid is not Proline (P)
#save sequence up to that point as protein 1 peptide 1
#take remaining sequence and repeat process
#when all of protein 1 has been fragmented, move to protein 2 and repeat process
#when the list is finished, output all fragments to a file in fasta format (see Output format below)

#bonus task 1 (cleavages): ensure Charles receives information in the form:
    #>protein_name peptide_num missed=int enzyme
    #'SEQUENCESTRING'

    #>ClAUD_F1_1 peptide 1 missed=2 enzyme t
    #GJAIGOEGKDGLLDGD

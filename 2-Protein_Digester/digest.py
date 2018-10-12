#Ask user for input: Fasta formatted protein sequences, labelled by protein number (Test with 'dummy.fasta')
    # Check that the input is a fasta file! (validate)
#read in fasta file
#assign to an object (thing)

filename = input("Please input your file name and format: ")
print('You entered {0}'.format(filename)) #print as a check!
    #errors might include: filename is not in the same directory, full path not specified, file is not in fasta format, file is in fasta format but does not contain expected amino acid codes.
fread = open('{0}'.format(filename),'r')

#Ask user for choice of four digesting enzymes: Trypsin, Endoproteinase Lys-C, Endoproteinase Arg-C, V8 proteinase (Glu-C)
    # (restrict all other inputs that do not match these options, return error message)
#read in user choice

enzyme = input("Please input your choice of enzyme (from: trypsin, endoproteinase_LysC, endoproteinase_ArgC, V8_proteinase_GluC): ")
    #errors might include user inputting invalid enzyme name
print('You entered {0}'.format(enzyme)) #print as a check!



#Create a function (e.g. digest) that contains the common elements, and use the varying bits as parameters!
#parameters are the variable 'enzyme' (name of enzyme)
#take each protein each time in sequence.


def digest(enzyme): #defining a function called digest which takes an argument enzyme
    protein_name = ??? #pull out name of first protein from fasta file
    peptide_num = 1 #set peptide number to 1

digest(enzyme)


#if trypsin, identify first peptide at Lysine (K) or Arginine (R), and if the next amino acid is not Proline (P)
#save sequence up to that point as protein 1 peptide 1
#take remaining sequence and repeat process
#when all of protein 1 has been fragmented, move to protein 2 and repeat process
#when the list is finished, output all fragments to a file in fasta format (see Output format below)

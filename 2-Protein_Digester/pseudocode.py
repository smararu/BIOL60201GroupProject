#General comments on program structure
#wants program to accept all parameters at the beginning
#will need to use argsv (reading arguments v python) as inputs.

#Ask user for input: Fasta formatted protein sequences, labelled by protein number (Test with 'dummy.fasta')
    # Check that the input is a fasta file! (validate)
#read in fasta file
#assign to an object (thing)

#Ask user for choice of four digesting enzymes: Trypsin, Endoproteinase Lys-C, Endoproteinase Arg-C, V8 proteinase (Glu-C)
    # (restrict all other inputs that do not match these options, return error message)

#read in user choice

#Create a function (e.g. digest) that contains the common elements, and use the varying bits as parameters!

#take a protein each time.

    #if trypsin, identify first peptide at Lysine (K) or Arginine (R), and if the next amino acid is not Proline (P)
        #save sequence up to that point as protein 1 peptide 1
            #take remaining sequence and repeat process
        #when all of protein 1 has been fragmented, move to protein 2 and repeat process
        #when the list is finished, output all fragments to a file in fasta format (see Output format below)

    #if Endoproteinase Lys-C, cut first peptide at Lysine (K), unless the next amino acid is Proline (P)
        #save sequence up to that point as protein 1 fragment 1
            #take remaining sequence and repeat process
        #when all of protein 1 has been fragmented, move to protein 2
        #when the list is finished, output all fragments to a file in fasta format (see Output format below)

    #if Endoproteinase Arg-C, cut first peptide at Arginine (R), unless the next amino acid is Proline (P)
        #save sequence up to that point as protein 1 fragment 1
            #take remaining sequence and repeat process
        #when all of protein 1 has been fragmented, move to protein 2
        #when the list is finished, output all fragments to a file in fasta format (see Output format below)

    #if V8 proteinase (Glu-C), cut first peptide at Glutamic acid (E), unless the next amino acid is Proline (P)
        #save sequence up to that point as protein 1 fragment 1
            #take remaining sequence and repeat process
        #when all of protein 1 has been fragmented, move to protein 2
        #when the list is finished, output all fragments to a file in fasta format (see Output format below)
#Notify user that digest has finished
#Return output file

#Output: Fasta formatted peptides, labelled by protein number and peptide number

#Question - how do we handle e.g. RR or KK or KR?
#Does the cut happen before or after the lysine (cut residue)?
    #in the examples it shows inclusion of the 'cut' residue in the peptide.

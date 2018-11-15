translateORF.py                 README                    


NAME
    foo - frobnicate the bar library

SYNOPSIS (Default run)
    python3 translateORF.py file.fasta,
    python3 translateORF.py genome.fasta - Standard

DESCRIPTION
     translateORF.py is a script  that readss in a file in FASTA  
     format containing a nucleotide sequence. It translates this 
     sequence and then finds all 6  possible reading frames, and  
     the produced amino acid chains (Open Reading Frames). These 
     are  then  output  wit   a  unique   header  in  the  form:
     NAME_FRAME_ORF.  This  is  then  output  in  a  file called 
     realDummy.peps

OPTIONS
     file           This is the file that will be translated
     -h or --help   will print the default run found below:
     
     python3 translateORF.py genome.fasta 


BUGS
     The reading frames are not output in the 'right order'. This
     was noted in a very early git commit.

AUTHOR
     Sebastian Mararu


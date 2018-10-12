#Input -> Genome from BacterialOrganism in FASTA format //
#Nucleotide Sequence from 3 letter to 1 letter amino acid
#TASK: Find ORFs and correct Reading Frame
#Prediction: Correct Reading frame is the longest
#start_codon = ['atg']
#stop_codon = ['tga', 'tag', 'taa']
# Output:
#>ORF frameLenghtStart
#Frame 1 
#>ORF frameLengthStart
#Frame 2 
#
####################
#PSEUDO
#Initialize sequence representation dictionary and other representations
#Read file,
#translateORF function - 
#args:
#1: Frame (0-1st ORF,1-2nd ORF,2-3rd ORF), 
#2: direction (0-Forward, 1-Backward) 
#
#1st Read-through, start at character n (start = 0)
#	In groups of 3 - Increment of 3
#	If ATG (start)
#	Compare to look-up table 
#	Append to frame n
#	Until STOP
#	Shift to next character position
#
#
#
#
#
#
#
#
#
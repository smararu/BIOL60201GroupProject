
# pseudocode for python script
#
#
# choose file ie assign filename to a variable. for coding purposes it will be dummy.peps
#
# create dictionary of M/C ratios of amino acids 
# create 2 dictionaries
monoMasses = {'A' :  71.0371, 'C' : 103.0092, 'D' : 115.0269,   #dictionary of monoisotopic masses
'E' : 129.0426, 'F' : 147.0684, 'G' :  57.0215, 
'H' : 137.0589, 'I' : 113.0841,'K' : 128.0950, 
'L' : 113.0841, 'M' : 131.0405, 'N' : 114.0429,
'P' :  97.0528, 'Q' : 128.0586, 'R' : 156.1011, 
'S' :  87.0320, 'T' : 101.0477, 'V' :  99.0684, 
'W' : 186.0793, 'Y' : 163.0633, '*' : 0.0 }

averageMasses = {'A' :  71.08, 'C' : 103.14, 'D' : 115.09,  #dictionary of average isotopic masses 
'E' : 129.12,'F' : 147.18, 'G' :  57.05, 
'H' : 137.14, 'I' : 113.16,'K' : 128.17, 
'L' : 113.16, 'M' : 131.19, 'N' : 114.10,
'P' :  97.12, 'Q' : 128.13, 'R' : 156.19, 
'S' :  87.08,'T' : 101.10, 'V' :  99.13, 
'W' : 186.21, 'Y' : 163.18, '*' : 0.0 }

outputDict ={}

file = 'dummy.peps' # assign filename to a variable
fileObj = open(file, 'r') # open and read file

lines = fileObj.readlines() # read each line in file, assigns each line as an item in list 'lines'
for headingIdentify in lines:# for eachline in lines
	if '>' in str(headingIdentify): # if this is the heading off a fasta sequence
		splitheading = headingIdentify.split()#		split the heading into separate strings
			#if there is already a key in the dictionary with this heading 
				#add the peptide number as a new item under that heading
			# else
				#create a new key for that peptide
				#append the dictionary to add the peptide number
#   
#	store peptide name as key in dictionary
#	store the peptide number as key in a nested dictionary
#	call a function which assigns the sum masses of AAs for the following line
#


# create dictionary of each peptide, using fasta heading as the keys
# assign the peptide number (ie if its the 1st, second etc) to the first[0] item in the list
# assign the assigns the correct m/c ratio value for each amino acid in the peptide string # to a total
# value at position 2 [1] of the list
# assigns a default value of 1 for charge to 3rd [2] list item
# assign a value of p to 4th position [3]. can this be taken from 2's? work out how to do anyway.
# assign the sequence string to 4th positon in the dictionary 
# 
# output dictionary in table format

fileObj.close() #close file

#

#command line option for doubly or triply charged ions? default is 1
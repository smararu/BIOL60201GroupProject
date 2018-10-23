
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




massdictionary = averageMasses #for testing, assumes user using average masses
file = 'dummy.peps' # assign filename to as variable
fileObj = open(file, 'r') # open and read file

proteinBank = []  #creates a list for which peptide data will be stored

lines = fileObj.readlines() # read each line in file, assigns each line as an item in array 'lines'
for index in range(0, len(lines),2): # for each of the lines in the range, counting in increments of 2
	line = lines[index] # assigns each line as a variale
	nextLine = lines[index + 1] #assigns the next line as a variable
	
	if line.startswith(">"): #if the line starts with a ">"
		heading = line #assigns the line as a variable 'heading'
		aaSeq = nextLine.replace("\n","") #assigns the next line to a variable 'aaSeq
		
		splitHeading = heading.split() #split the heading into separate strings
		proteinName = splitHeading[0][1:]  #assign protein name to a variable from the position [1] of split heading, ie excluding '>'
		peptideNumber = splitHeading[2] #assign peptide number to a variable
		missedCleaves = splitHeading[3][7]
		proteinPosition = splitHeading[4]
		enzyme = splitHeading[5]

	residueValue = [] # creates a new list, residueValue, in which to store peptide masses
	for count in aaSeq:  #for each character in my string 
		residueValue.append(massdictionary[count]) #add each aa mass to list
	residueValueList = (residueValue) #assigns the aa mass list to a new variable
	peptideValue = sum(residueValueList) #adds up the total value of masses in the list
	peptideValue2sf = format(peptideValue, '.2f') #saves the result to 2sf. NOTE let no. of s.f. be 2 or 3 depending on dictionary input

	proteinBank.append({ 'Protein Name' : proteinName ,
	'Number' : peptideNumber, 'Mass' : peptideValue2sf, 
	'MissedCleaves' : missedCleaves, 'Position': proteinPosition, 
	'Enzyme':enzyme, 'Sequence' :  aaSeq })  #store all of the values in the list, under dictionary with variables a key headings

print(proteinBank)


fileObj.close() #close file



#argument for doubly or triply charged ions? default is 1








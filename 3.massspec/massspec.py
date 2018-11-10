



file = 'digested_t.fasta' # assign filename to as variable
fileObj = open(file, 'r') # open and read file
outFile = open('newOutTest.masses', 'w')

monoMassesDict = {'A' :  71.0371, 'C' : 103.0092, 'D' : 115.0269,   #dictionary of monoisotopic masses
'E' : 129.0426, 'F' : 147.0684, 'G' :  57.0215, 
'H' : 137.0589, 'I' : 113.0841,'K' : 128.0950, 
'L' : 113.0841, 'M' : 131.0405, 'N' : 114.0429,
'P' :  97.0528, 'Q' : 128.0586, 'R' : 156.1011, 
'S' :  87.0320, 'T' : 101.0477, 'V' :  99.0684, 
'W' : 186.0793, 'Y' : 163.0633, '*' : 0.0, 
'H2O' : 18.0106, 'proton' : 1}

averageMassesDict = {'A' :  71.08, 'C' : 103.14, 'D' : 115.09,  #dictionary of average isotopic masses 
'E' : 129.12,'F' : 147.18, 'G' :  57.05, 
'H' : 137.14, 'I' : 113.16,'K' : 128.17, 
'L' : 113.16, 'M' : 131.19, 'N' : 114.10,
'P' :  97.12, 'Q' : 128.13, 'R' : 156.19, 
'S' :  87.08,'T' : 101.10, 'V' :  99.13, 
'W' : 186.21, 'Y' : 163.18, '*' : 0.0, 
'H2O' : 18.0153, 'proton' : 1}

import argparse
options = argparse.ArgumentParser()  # introduce arguments 
options.add_argument("-i", help="choose either 'monoisotopic' or 'averageisotopic' mass values ['m','a']", default='a') #arguement for either monoisotopic or average isotopic masses
options.add_argument("-c", help="choose a charge for peptides[1,2,3]", default='1') # argument for charge of peptides
options.add_argument("-t", help="choose to report back only N or C terminal peptides ['n','c', ]", default=' ')  #argument for N or C terminal peptides 
args = options.parse_args()  # stores arguments as variable, args

if args.i == 'm':   #if the user chooses monoisotopic masses
	massDictionary = monoMassesDict   # use the monoisotopic masses dictionary
else:
	massDictionary = averageMassesDict  # otherwise, default to average masses

if args.c == '3':  #if user chooses charge to be 3
	charge = 3   # charge is 3
elif args.c == '2': #likewise for 2
	charge = 2
else:
	charge = 1 # default to 1

if args.t == 'n': #if argument for -t is 'n' ie user chooses to report only N terminal peptides
	terminal = 'n'
elif args.t == 'c':
	terminal = 'c'
else:
	terminal = 'none'  # default to arbitrary string, 'none'

peptideDictionary = {} #initiates a dictionary used to count the number of each type of peptide
terminalDictionary = {} #initiates a dictioary used to store n or c terminal peptide

lines = fileObj.readlines() # read each line in file, assigns each line as an item in array 'lines'
for index in range(0, len(lines),2): # for each of the lines in the range, counting in increments of 2
	heading = lines[index] # assigns each alternate line as a variale 'heading'
	
	splitHeading = heading.split() #split the heading into separate strings
	peptideName = splitHeading[0][1:]  #assign protein name to a variable from the position [1] of split heading, ie excluding '>'
	peptideNumber = splitHeading[1] #assign peptide number to a variable
	missedCleaves = splitHeading[2][8]
	enzyme = splitHeading[3]

	nextLine = lines[index + 1] #assigns the next line as a variable
	aaSeq = nextLine.replace("\n","") #assigns the next line to a variable 'aaSeq', removing new line codes 
	residueValue = [] # creates a new list, residueValue, in which to store peptide masses
	for count in aaSeq:  #for each character in my string 
		protonMass = charge
		residueValue.append(massDictionary[count])   # all these 3 in same command???
		residueValueList = (residueValue) #assigns the aa mass list to a new variable
	
	peptideValue = sum(residueValueList)#adds up the total value of masses in the list
	peptideValueFull = float(peptideValue) + charge + massDictionary['H2O'] # adds the proton mass (==charge) and mass of water
	peptideValue4sf = format(peptideValueFull, '.4f')  #saves the result to 4dp.
	
	def outputPrint():
		print(peptideName.ljust(20), peptideNumber.rjust(2), str(peptideValue4sf).rjust(10), missedCleaves.rjust(1), repr(charge).rjust(1), enzyme.rjust(1), aaSeq, file=outFile) 
	sString =  peptideName.ljust(20), peptideNumber.rjust(2), str(peptideValue4sf).rjust(10), missedCleaves.rjust(1), repr(charge).rjust(1), enzyme.rjust(1), aaSeq

		#above  defines  function to print the peptide information to output file
	
	if terminal =='n':
		if peptideName not in terminalDictionary:
			terminalDictionary[name] = peptideName
			outputPrint()
	elif terminal == 'c':
		terminalDictionary[peptideName] = {'number': peptideNumber, 'mass': peptideValue4sf, 'missed': missedCleaves, 'charge': charge, 'sequence': aaSeq}
	else:
		outputPrint()

	
	if peptideName not in peptideDictionary: # if the peptide is not already in dictionary
		peptideDictionary[peptideName] =  1 # creates a key of peptide and assigns it a value of 1
	else: 									# else, if the peptide has been encountered already, add 1
		peptideDictionary[peptideName] += 1

if terminal == 'c':
	for keys in terminalDictionary:
		print(keys, terminalDictionary[keys]['number'],terminalDictionary[keys]['mass'], terminalDictionary[keys]['missed'], terminalDictionary[keys]['charge'],terminalDictionary[keys]['sequence'], file=outFile)


fileObj.close() #close file
outFile.close()

statsFile = open('enzyme_t_1500_stats.csv', 'w') #initiates a new output file for stats
peptideNumberList= []  #inititates a new list to store peptide numbers in
totalProteins = len(peptideDictionary)  # counts the number of entries in peptideDictionary
print('There are',totalProteins, 'digested proteins which cleave to make peptides in the required range') #prints the number of proteins
for keys in peptideDictionary:  #for each protein in the dictionary 
	peptideNumberList.append(peptideDictionary[keys])  # add the number of peptides
	print(keys, ',',peptideDictionary[keys], file=statsFile)
totalPeptides = sum(peptideNumberList)  # sums the total value of these peptides 
print('There are',totalPeptides,'of these peptides in total')  # prints this total
averagePeptides = format((totalPeptides / totalProteins),'.4f')  # determines the average peptides per protein to 4.dp
print('The average number of peptides (in given range) per ("useful") protein for',file ,'is', averagePeptides)  #prints the average

#error testing - eg arguments aren't correct values

#Bonus task: create dictioary, if peptide name not there, add seq to dictionary
# if not there, overwrite previous 
# change dependent on if user called n or c

#create dictionary of proteins 
#if peptide is there, add 1 to value
#if peptide is not there, add a new item
#output: dictionary as .csv file which can be used for stats
#if normal distribution, use mean, if skewed, use median
#

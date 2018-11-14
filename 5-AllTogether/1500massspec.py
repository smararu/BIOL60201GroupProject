
import argparse
import sys
from pathlib import Path

monoMassesDict = {'A' :  71.0371, 'C' : 103.0092, 'D' : 115.0269,   #dictionary of monoisotopic masses
'E' : 129.0426, 'F' : 147.0684, 'G' :  57.0215, 
'H' : 137.0589, 'I' : 113.0841,'K' : 128.0950, 
'L' : 113.0841, 'M' : 131.0405, 'N' : 114.0429,
'P' :  97.0528, 'Q' : 128.0586, 'R' : 156.1011, 
'S' :  87.0320, 'T' : 101.0477, 'V' :  99.0684, 
'W' : 186.0793, 'Y' : 163.0633, '*' : 0.0, 
'H2O' : 18.0106, 'proton' : 1, 'PO3': 79.9663}

averageMassesDict = {'A' :  71.08, 'C' : 103.14, 'D' : 115.09,  #dictionary of average isotopic masses 
'E' : 129.12,'F' : 147.18, 'G' :  57.05, 
'H' : 137.14, 'I' : 113.16,'K' : 128.17, 
'L' : 113.16, 'M' : 131.19, 'N' : 114.10,
'P' :  97.12, 'Q' : 128.13, 'R' : 156.19, 
'S' :  87.08,'T' : 101.10, 'V' :  99.13, 
'W' : 186.21, 'Y' : 163.18, '*' : 0.0, 
'X' : 0, 'H2O' : 18.0153, 'proton' : 1, 'PO3': 79.98}

options = argparse.ArgumentParser(description='Determine isotopic masses for each digested peptide')  # introduce arguments 
options.add_argument("-f", help="choose file with which to  perform task 3, mass spec analysis")
options.add_argument("-i", help="choose either 'monoisotopic' or 'averageisotopic' mass values ['m','a']", default='a') #argument for either monoisotopic or average isotopic masses
options.add_argument("-c", help="choose a charge for peptides[1,2,3]", default='1') # argument for charge of peptides
options.add_argument("-t", help="choose to report back only N or C terminal peptides ['n','c','a' ]", default='a')  #argument for N or C terminal peptides 
options.add_argument("-s", help="choose to have basic stats files output. y/n. ['y','n']", default='n') # argument to allow user to output some stats files
options.add_argument("-p", help="choose to modify Ser, Try and Thr by adding a phosphorus group. y/n. ['y','n']", default='n') # argument to allow user to output some stats files

args = options.parse_args()  # stores arguments as variable, args


if (args.s is not 'y') and (args.s is not 'n'):  # error checking: if -s argument is neither 'y' or 'n',
	print("Error: Stats argument ('-s') must be 'y' or 'n'. Default is 'n'.")  # Prints error message
	sys.exit()  # halts the program

if (args.i is not 'm') and (args.i is not 'a'): #error checking: if -i argument is neither 'm' or 'a',
	print("Error: Isotopic mass (-i) argument must be 'm' (monoisotopic masses) or 'a' (average isotopic). Default is 'a'.") # prints error message
	sys.exit()  # halts the program
if args.i == 'm':   #if the user chooses 'm' masses
	massDictionary = monoMassesDict   # use the monoisotopic masses dictionary
else:
	massDictionary = averageMassesDict  # otherwise, default to average masses

if (args.c is not '1') and (args.c is not '2') and (args.c is not '3'):  # error checking: if the -c argument is neither 1, 2 or 3,
	print("Error: Charge (-c) can only take value of either 1, 2, or 3. Default is '1'.") # print error message
	sys.exit()  # half program
if args.c == '3':  #if user chooses charge to be 3
	charge = 3   # charge is 3
elif args.c == '2': #likewise for 2
	charge = 2
else:
	charge = 1 # default to 1

if (args.t is not 'n') and (args.t is not 'c') and (args.t is not 'a'):  # if the -t argument is neither n, c or a
	print("Error: terminal (-t) argument must be 'n' (n-terminal), 'c' (c-terminal) or 'a' (all peptides). Default is 'a'.")  # print error message
	sys.exit()  # halt the program
if args.t == 'n': #if argument for -t is 'n' ie user chooses to report only N terminal peptides,
	terminal = 'n' # terminal variable is 'n'
elif args.t == 'c': # likewise for 'c'
	terminal = 'c'
else:  # if 'a' or no argument is given,
	terminal = 'a'  # default to arbitrary string, 'none' (terminal must have a value)


if args.f == None:  #error checking: if there is no file chosen 
	sys.exit("Error: Please choose fasta file (using -f tag) to perform analysis eg. 'massspec.py -f digested_a.fasta'")  #halts the program
file = args.f # assign filename to as variable
if '.fasta' not in file[-6:]: #error checking: if file suffix is not.fasta
	sys.exit("Error: please make sure file is named with '.fasta' suffix")  #halts the program

fileCheck = Path(file)  # check to see if the file (or path to file) returns a true file
if not fileCheck.is_file():  # if pathlib cannot find the file
	sys.exit("Error: Please check chosen file (-f) exists and is in working directory.")  # halts the program

if (args.p is not 'y') and (args.p is not 'n'):  #error checking if the argument is not 'y' or 'n'
	sys.exit("Error: phosphorus '-p' argument must must be 'y' for yes or 'n' for no")  # halts the program

fileObj = open(file, 'r') # open and read file
outFile = open(file[:-6]+'.masses', 'w') #opens output file, with same name as input file, but changes suffix to '.masses'

peptideDictionary = {} #initiates a dictionary used to count the number of each type of peptide
terminalDictionary = {} #initiates a dictioary used to store n or c terminal peptide

lines = fileObj.readlines() # read each line in file, assigns each line as an item in array 'lines'
for index in range(0, len(lines),2): # for each of the lines in the range, counting in increments of 2
	heading = lines[index] # assigns each alternate line as a variale 'heading'
	
	splitHeading = heading.split() #split the heading into separate strings
	peptideName = splitHeading[0][1:]  #assign protein name to a variable from the position [1] of split heading, ie excluding '>'
	peptideNumber = splitHeading[1] #assign peptide number to a variable
	missedCleaves = splitHeading[2][7] # missed cleaves 
	enzyme = splitHeading[3]

	nextLine = lines[index + 1] #assigns the next line as a variable
	aaSeq = nextLine.replace("\n","") #assigns the next line to a variable 'aaSeq', removing new line codes 
	residueValue = [] # creates a new list, residueValue, in which to store peptide masses
	for count in aaSeq:  #for each character in my string 
		residueValue.append(massDictionary.get(count, 0))   # all these 3 in same command???
		if massDictionary.get(count, 0) == 0:
			print("Warning: unknown amino acid: "+count+"in "+ peptideName +". M/Z value for this AA: 0")
		if args.p is 'y':
			if count is "S":
					residueValue.append(massDictionary['PO3'])
			elif count is "Y":
				residueValue.append(massDictionary['PO3'])
			elif count is "T":
				residueValue.append(massDictionary['PO3'])
		residueValueList = (residueValue) #assigns the aa mass list to a new variable
	
	peptideValue = sum(residueValueList)#adds up the total value of masses in the list
	peptideValueFull = (float(peptideValue) + charge + massDictionary['H2O'])/charge # adds the proton mass (==charge) and mass of water the divides by charge
	peptideValue4sf = format(peptideValueFull, '.4f')  #saves the result to 4dp.
	
	def outputPrint(): # defines function to print peptide data, with masses
		print(peptideName.ljust(20), peptideNumber.rjust(2), 
			str(peptideValue4sf).rjust(10), missedCleaves.rjust(1), 
			repr(charge).rjust(1), enzyme.rjust(1), aaSeq, file=outFile) 
	
	if terminal =='n':  # if user has requested n terminal peptides
		if peptideName not in terminalDictionary: # if protein has not already been encountered
			terminalDictionary[peptideName] = peptideName  # add the peptide to dictionary 
			outputPrint()
	elif terminal == 'c':
		terminalDictionary[peptideName] = {'number': peptideNumber, 'mass': peptideValue4sf, 'missed': missedCleaves, 'charge': charge, 'enzyme' :enzyme, 'sequence': aaSeq}
	else:
		outputPrint()

	if 1000 < float(peptideValue4sf) < 1500:
		if peptideName not in peptideDictionary: # if the peptide is not already in dictionary
			peptideDictionary[peptideName] =  1 # creates a key of peptide and assigns it a value of 1
		else: 									# else, if the peptide has been encountered already, add 1
			peptideDictionary[peptideName] += 1

if terminal == 'c':  # if user has requested 'c' terminal peptides
	for keys in terminalDictionary:  # for each peptide
		print(keys.ljust(20), terminalDictionary[keys]['number'].rjust(2),  # prints to output file 
			terminalDictionary[keys]['mass'].rjust(10), 
			terminalDictionary[keys]['missed'].rjust(1), 
			repr(terminalDictionary[keys]['charge']).rjust(1),
			terminalDictionary[keys]['enzyme'].rjust(1),
			terminalDictionary[keys]['sequence'], file=outFile)

fileObj.close() #close files
outFile.close()

if args.s == 'y':
	statsFile = open(file[:-6]+'.csv', 'w') #initiates a new output file for stats
	statsOverview = open(file[:-6]+'.stats', 'w')
	peptideNumberList= []  #inititates a new list to store peptide numbers in
	totalProteins = len(peptideDictionary)  # counts the number of entries in peptideDictionary
	print('There are',totalProteins, 'digested proteins which cleave to make peptides in the required range', file=statsOverview) #prints the number of proteins
	for keys in peptideDictionary:  #for each protein in the dictionary 
		peptideNumberList.append(peptideDictionary[keys])  # add the number of peptides
		print(keys, ',',peptideDictionary[keys], file=statsFile)
	totalPeptides = sum(peptideNumberList)  # sums the total value of these peptides 
	print('There are',totalPeptides,'of these peptides in total', file=statsOverview)  # prints this total
	averagePeptides = format((totalPeptides / totalProteins),'.4f')  # determines the average peptides per protein to 4.dp
	print('The average number of peptides (in given range) per ("useful") protein for',file ,'is', averagePeptides, file=statsOverview)  #prints the average

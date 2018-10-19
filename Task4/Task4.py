#Open file Task 3 ('dummy.pepmasses')
f = open('dummy.pepmasses.fa', 'r')

#Read mass column
  ##Separate results by frame (Task 1 gives only Frame with the largest peptide?)
  ##Separate results by enzyme (chose a enzyme from a list?)
#Define mass column ranges (user entry input())

MinValue= input('Write the MINIMUM VALUE OF MASS you want to analyze') #Define your range, (entry min value input())
MaxValue= input('Write the MAXIMUM VALUE OF MASS you want to analyze') #Define your range, (entry max value input())
print('Write your value with four decimals', MinValue)
print('Write your value with four decimals', MaxValue)

#DISPLAYS WELLCOMING MESSAGE, NAME AND AGE
print('Wellcome to Programming class ', name, '. Your current age is ', age)

  Define number of bins, (how many bins want to visualice in hystogram input())
Count peptides on each range,
  Total number of peptides
    Identify and count peptides with Cys, Met
    Subtotal of peptides with ions (ionA, ionB, ...)
  For mass values on each range or bin, calculate mean values of mass
  Mean of peptides by ions type (ionA, ionB, ...)
Calculate instruments accuracy (error), this is type II error for each range or bin using mass values   
Transform mass values from Da to ppm (accuracy 0.2Da, 5ppm)

Conversion: 
  Error (ppm) = Error (Da) * 1,000,000 / (m/z for sample)
  EXAMPLE: Error1 (ppm) = 0.001 Da * 1,000,000 / 300.0000 = 3.3 = 3 ppm


Report CSV

InputFile = '../project/dummy.pepmasses'
f= open(InputFile,'r')
lines = f.readlines()
nlines = len(lines)
print ('nlines = ', nlines)
MinValue= input('Write the MINIMUM VALUE OF MASS you want to analyze') #Define your range, (entry min value input())
MaxValue= input('Write the MAXIMUM VALUE OF MASS you want to analyze') #Define your range, (entry max value input())


DRAFT CODE
InputFile = '../project/dummy.pepmasses'
import numpy as np
f= open(InputFile,'r')
lines = f.readlines()
nlines = len(lines)
print ('nlines = ', nlines)

Min= input('Write the MINIMUM VALUE OF MASS you want to analyze') #Define your range, (entry min value input())
Max= input('Write the MAXIMUM VALUE OF MASS you want to analyze') #Define your range, (entry max value input())

#NumPep=input('This will be calculated, just write a number for now')
NumPep=0
for line in lines: 
    mz = line.split()[2] # Split each line and handle the 3rd values - mz values -
    if float(mz) >= int(Min):  #range given by user
       NumPep= NumPep+1 #count of events on the given range with IF statement

    Meanmz=float(np.mean(float(mz)))

OutputFile = "OUTPUTFILE"
print(type(mz))
#print("Your filename has {0:.0f} peptides between {0:.1f} Da and {0:.1f}. Average value of m/z is {0:.2f}".format (NumPep,MinValue,MaxValue,Meanmz))
print("Number of Peptides in", Min, " - ", Max, "Daltons mass range is=\t", NumPep)
print("Mean value of m/z in the given range is: \t", Meanmz, "Da \t OR \t ##### ppm")
#print("For detailed information, open", OutputFile )

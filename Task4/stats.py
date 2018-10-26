# (0) Required libraries
import numpy as np # numpy library for work with numbers, lists, arranges
import matplotlib.pyplot as plt #matplotlib.pyplot library for work plots, graphs

# (1) Files
# (1.1) Input file
InputFile = '../project/dummy.pepmasses' #imports FASTA file from task 3 
f= open(InputFile,'r') #open INPUT FILE
lines = f.readlines() #read each line of INPUT FILE f
nlines = len(lines) #determines the length of "lines", count the number of lines
print ('Total number of proteins to analyze= ', nlines) #output "nlines = number"

# (1.2) Select mz from Input file to be used in (3)
masses = [] #creates a list
peptide_data = []
enzyme_used=[]
for line in lines:
    (name,number,mass_to_charge,z,p,prot_sequence)=line.split() # objects from list as strings
    mzf=float(mass_to_charge) # Float type needed for calculations
    enzyme_us = name.str.split(None, 1)[0]
    print(enzyme_us)
    masses.append(mzf) #agregates mzf values to masses list
    
    #print(masses)
    #peptide_data.append({'t': "Trypsin",'l':"Endoproteinase Lys-C",'a':"Endoproteinase Arg-C",'e':"V8 proteinase (Glu-C)"})

plt.hist(masses,bins=30)
plt.show()
#sum(peptide['mass'] for peptide in peptide_data)

# (1.3) Working file
histf=open('result4.csv','w+') #open a file, 'w+' creates file to print results from task 4


# (2) Analysis
# (2.1) User defines to analyze all values of mz or a range of values
select=input('Write "full" to analyze whole mz values or  "range"  to define the a range of values')

# (2.2) If user writes "full" in (2.1)
if select=="full":
    print ('You choosed to analyse ', select, 'of mass to charge (mz) data')
    number_bins = input('Write the number of bins for your histogram')
    bin_width = ( min(masses) + max(masses) ) / len(masses) # Calculates the width of each bin
    print('Width of bins = ', bin_width)
    sum_bin_masses = 0 #Start the sum of masses for each bin
    count_bin_masses = 0
    for bin_n in (1, int(number_bins)):
        for mass in (0, min(masses) + bin_n * bin_width):
            if mass >= min(masses) and mass <= min(masses) + mass*bin_n:
                sum_bin_masses = sum_bin_masses + mass
                count_bin_masses = count_bin_masses + 1
                mean_each_bin = sum_bin_masses / count_bin_masses
    print('Bin:', bin_n,'\t Mass mean = ', mean_each_bin)

    #plt.hist(x=mzf,bins=Nbins,color="red",alpha=0.7, rwidth=0.85)
    #plt.show()

# (3.2) If user writes "range" in (2)
else:
    print ('You choosed to analyse ', select, 'of mass to charge (mz) data')
    Min= int(input('Write the MINIMUM VALUE OF MASS you want to analyze')) #Define minimum value
    Max= int(input('Write the MAXIMUM VALUE OF MASS you want to analyze')) #Define maximum value
    number_pep=0
    meanmz_inrange = 0
    if  mzf > Min and mzf < Max: #mz values within the range given by user
        number_pep = number_pep + 1 #count of events on the given range with IF statement
        meanmz_inrange = np.mean ( Min <= masses <= Max)
    print('Selected range has ', number_pep, '\t and mean mz value of: ', meanmz_inrange)

# mark's code starts here

#total_mass = 0
#mass_count = 0
#for mass in masses:
#    if mass >= Min & mass <= Max:
#        total_mass = total_mass + mass
#        mass_count = mass_count + 1
#average = total_mass / mass_count

# mark's code ends here

    
# (4) Output
# (4.1) Output full analysis
def PrintToFile(outputFile, framedSequence):
    numberOfFrames = len(framedSequence)
    # outputFile = "outputFile.txt"

    with open(outputFile, 'w') as f:
        
        # print('Filename:', outputFile, file=f) 
        for frameNumber, frames in enumerate(framedSequence):
            frameNumber = framedSequence.index(frames) #change index
            for openReadingFrame, aminoAcids in enumerate(frames):
                print (">CLAUD_F" + str(frameNumber+1) + "_" + str(openReadingFrame+1).zfill(4), file=f)
                print (aminoAcids, file=f)
    
finalFrames = 0
finalFrames = TranslateORF(range(1,7))
# print (finalFrames)
PrintToFile("outputFile.txt", finalFrames)

# (4.2) Output range analysis
#print(type(mz))
#print("Your filename has {0:.0f} peptides between {0:.1f} Da and {0:.1f}. Average value of m/z is {0:.2f}".format (NumPep,MinValue,MaxValue,Meanmz))
#print("Number of Peptides in", Min, " - ", Max, "Daltons mass range is=\t", NumPep)
#print("Mean value of m/z in the given range is: \t", Meanmz, "Da \t OR \t ##### ppm")

# (4.2.1) HISTOGRAM RANGE
#plt.hist(mz,bins=10,range=None)
#plt.show()

#print("For detailed information, open", OutputFile )

##### required libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse

##### create arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--inputfile", help = "Choose an input file *.masses format ", type = str)
parser.add_argument("-n", "--analysis", help = "Available data for peptides mass-to-charge is between 1000Da-1500Da, select complete analysis writing full or select a short range analysis writing range", type = str, default = "full")
parser.add_argument("-i", "--minimum", help = "Minimum value for range analysis", type = float, default=1000.0)
parser.add_argument("-x", "--maximum", help = "Maximum value for range analysis", type = float, default=1500.0)
parser.add_argument("-z", "--enzyme", help = "Choose an enzyme t, a, l, e", type = str, default="")
parser.add_argument("-s", "--sequence", help = "Give a sequence to search on data", type = str, default="")
parser.add_argument("-b", "--binss", help = "Number of bins for histogram", type = int, default=30)
args = parser.parse_args()

###### merge task3 output four files
filenames = ['enzyme_t.masses', 'enzyme_a.masses', 'enzyme_l.masses','enzyme_e.masses']
with open('./task31.masses', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

##### input file
f = open(args.inputfile, 'r')
lines = f.readlines()
nlines = len(lines)

##### output_file
t4_results = open('Statistics.tab','w')
print('Total number of peptides in input file is: ', nlines)

# transform *.masses type file to dataframe
prot_name = []
peptide = []
mass_to_charge = []
z = []
p = []
enzym = []
sequenc = []

for line in lines:
    (name,pept,mass_charge,zn,pn,enz,seq) = line.split() # objects from list as strings
    prot_n = str(name)
    pepti = int(pept)
    mass_ch = float(mass_charge)
    znn = int(zn)
    pnn = int(pn)
    enzy = str(enz)
    sequ = str(seq)
    prot_name.append(prot_n)
    peptide.append(pepti)
    mass_to_charge.append(mass_ch)
    z.append(znn)
    p.append(pnn)
    enzym.append(enzy)
    sequenc.append(sequ)
task3_pd = pd.DataFrame({'prot_name':prot_name,'peptide':peptide,'mass_to_charge':mass_to_charge,'z':z , 'p':p,'enzyme':enzym,'sequence':sequenc})
total_rows=task3_pd['prot_name'].count()
print("Number of peptides in data frame is: ",total_rows)

##### select rows with mass_to_charge values between 1000Da - 1500Da
condition1 = task3_pd['mass_to_charge']>=1000
condition2 = task3_pd['mass_to_charge']<=1500
task4dat = task3_pd[condition1 & condition2]

total_rows=task4dat['prot_name'].count()
print("Number of proteins with mass_to_charge values between 1000Da - 1500Da: ",total_rows)

# data by enzyme
task4_t = task4dat[task4dat['enzyme']=="t"]
task4_l = task4dat[task4dat['enzyme']=="l"]
task4_a = task4dat[task4dat['enzyme']=="a"]
task4_e = task4dat[task4dat['enzyme']=="e"]

# main histogram
plt.hist((task4_t['mass_to_charge'],task4_a['mass_to_charge'],task4_l['mass_to_charge'],task4_e['mass_to_charge']),bins = args.binss, label= ["Trypsin", "Endoproteinase Arg-C","Endoproteinase Lys-C","V8 proteinase"], color=('r','b','g','c'),stacked = False, alpha = 0.8,rwidth = 0.8)
plt.title('Mass-to-charge by enzyme')
plt.ylabel('Number of peptides')
plt.xlabel('Mass-to-charge, m/z')
plt.legend()
plt.show()
plt.savefig('plot_mz_all_enzyme.png')

##### user defines range analysis
if args.analysis=="range":
    print("THIS IS A RANGE ANALYSIS RESULTS")
    # select data between user given range
    cond1 = task4dat['mass_to_charge'] >= args.minimum
    cond2 = task4dat['mass_to_charge'] <= args.maximum    
    data1 = task4dat[cond1 & cond2]
    total_rows=data1['prot_name'].count()
    print("Number of peptides within the defined range is: ",total_rows)
    # user defines range, not enzyme
    if args.enzyme == "":
        # user defines range, not enzyme, not sequence
        if args.sequence == "":
            print("Mass to charge within the range is: ",data1['mass_to_charge'].mean()," Da", file = t4_results)
            print("Total number of peptides within the range is: ", data1['mass_to_charge'].count(), file = t4_results)
            print("bin_left \t bin_right \t number_peps \t mean_mz", file = t4_results)
            bin_width = (args.maximum-args.minimum)/args.binss
            bin_left = 0
            bin_right = 0
            for nbin in range (0, args.binss):
                bin_left = args.minimum + (nbin) * bin_width
                bin_right = args.minimum + (nbin+1) * bin_width
                fileObj = data1['mass_to_charge']
                count_mz = 0
                sum_mz = 0
                for massz in fileObj:
                    if massz >= bin_left and massz < bin_right:
                        count_mz = count_mz + 1
                        sum_mz += massz 
                mean_massz = sum_mz / count_mz
                print(str(round(bin_left,2)).ljust(15), str(round(bin_right,2)).ljust(15), str(count_mz).ljust(15),str(round(mean_massz,3)).ljust(15), file = t4_results)

        # user defines range, not enzyme, yes sequence
        else:
            cond3 = data1['sequence'].str.contains(args.sequence, na=False)
            data11 = data1[cond3]
            print("Mass to charge within the range and for defined sequence is: ",data11['mass_to_charge'].mean()," Da", file = t4_results)
            print("Total number of peptides within the range and for defined sequence is: ", data11['mass_to_charge'].count(), file = t4_results)
            print("bin_left \t bin_right \t number_peps \t mean_mz", file = t4_results)
            bin_width = (args.maximum-args.minimum)/args.binss
            bin_left = 0
            bin_right = 0
            for nbin in range (0, args.binss):
                bin_left = args.minimum + (nbin) * bin_width
                bin_right = args.minimum + (nbin+1) * bin_width
                fileObj = data11['mass_to_charge']
                count_mz = 0
                sum_mz = 0
                for massz in fileObj:
                    if massz >= bin_left and massz < bin_right:
                        count_mz = count_mz + 1
                        sum_mz += massz 
                mean_massz = sum_mz / count_mz
                print(str(round(bin_left,2)).ljust(15), str(round(bin_right,2)).ljust(15), str(count_mz).ljust(15),str(round(mean_massz,3)).ljust(15), file = t4_results)
                
    # user defines range and enzyme
    else:
        cond4 = data1['enzyme']== args.enzyme
        data2=data1[cond4]
        # user defines range, enzyme, not sequence
        if args.sequence == "":
            print("Mass to charge within the range and defined enzyme is: ",data2['mass_to_charge'].mean()," Da", file = t4_results)
            print("Total number of peptides within the range and defined enzyme is: ", data2['mass_to_charge'].count(), file = t4_results)
            print("bin_left \t bin_right \t number_peps \t mean_mz", file = t4_results)
            bin_width = (args.maximum-args.minimum)/args.binss
            bin_left = 0
            bin_right = 0
            for nbin in range (0, args.binss):
                bin_left = args.minimum + (nbin) * bin_width
                bin_right = args.minimum + (nbin+1) * bin_width
                fileObj = data2['mass_to_charge']
                count_mz = 0
                sum_mz = 0
                for massz in fileObj:
                    if massz >= bin_left and massz < bin_right:
                        count_mz = count_mz + 1
                        sum_mz += massz 
                mean_massz = sum_mz / count_mz
                print(str(round(bin_left,2)).ljust(15), str(round(bin_right,2)).ljust(15), str(count_mz).ljust(15),str(round(mean_massz,3)).ljust(15), file = t4_results)
                
        # user defines range, enzyme and sequence
        else:
            cond5 = data2['sequence'].str.contains(args.sequence, na=False)
            data21 = data2[cond5]
            print("Mass to charge within the range, defined enzyme and sequence is: ",data21['mass_to_charge'].mean()," Da", file = t4_results)
            print("Total number of peptides within the range, defined enzyme and sequence is: ", data21['mass_to_charge'].count(), file = t4_results)
            print("bin_left \t bin_right \t number_peps \t mean_mz", file = t4_results)
            bin_width = (args.maximum-args.minimum)/args.binss
            bin_left = 0
            bin_right = 0
            for nbin in range (0, args.binss):
                bin_left = args.minimum + (nbin) * bin_width
                bin_right = args.minimum + (nbin+1) * bin_width
                fileObj = data21['mass_to_charge']
                count_mz = 0
                sum_mz = 0
                for massz in fileObj:
                    if massz >= bin_left and massz < bin_right:
                        count_mz = count_mz + 1
                        sum_mz += massz 
                mean_massz = sum_mz / count_mz
                print(str(round(bin_left,2)).ljust(15), str(round(bin_right,2)).ljust(15), str(count_mz).ljust(15),str(round(mean_massz,3)).ljust(15), file = t4_results)
                


##### default analysis (full data between 1000Da - 1500Da)
else:
    print("FULL ANALYSIS RESULTS (1000Da - 1500Da)",file=t4_results)
    
    # if user defines full, not enzyme
    if args.enzyme == "":
        # if user defines full, not enzyme, not sequence
        if args.sequence == "":
            print("Mass to charge for data in default 1000Da-1500Da limits is: ",task4dat['mass_to_charge'].mean()," Da", file = t4_results)
            print("Total number of peptides for data in default 1000Da-1500Da limits is: ", task4dat['mass_to_charge'].count(), file = t4_results)
            print("bin_left \t bin_right \t number_peps \t mean_mz", file = t4_results)
            bin_width = (args.maximum-args.minimum)/args.binss
            bin_left = 0
            bin_right = 0
            for nbin in range (0, args.binss):
                bin_left = args.minimum + (nbin) * bin_width
                bin_right = args.minimum + (nbin+1) * bin_width
                fileObj = task4dat['mass_to_charge']
                count_mz = 0
                sum_mz = 0
                for massz in fileObj:
                    if massz >= bin_left and massz < bin_right:
                        count_mz = count_mz + 1
                        sum_mz += massz 
                mean_massz = sum_mz / count_mz
                print(str(round(bin_left,2)).ljust(15), str(round(bin_right,2)).ljust(15), str(count_mz).ljust(15),str(round(mean_massz,3)).ljust(15), file = t4_results)
                
        # if user defines full, not enzyme, yes sequence
        else:
            cond6 = task4dat['sequence'].str.contains(args.sequence, na=False)
            data3= task4dat[cond6]
            print("Mass to charge for data in default 1000Da-1500Da limits and defined sequence is: ",data3['mass_to_charge'].mean()," Da", file = t4_results)
            print("Total number for data in default 1000Da-1500Da limits and defined sequence is: ", data3['mass_to_charge'].count(), file = t4_results)
            print(data3, file = t4_results)
            print("bin_left \t bin_right \t number_peps \t mean_mz", file = t4_results)
            bin_width = (args.maximum-args.minimum)/args.binss
            bin_left = 0
            bin_right = 0
            for nbin in range (0, args.binss):
                bin_left = args.minimum + (nbin) * bin_width
                bin_right = args.minimum + (nbin+1) * bin_width
                fileObj = data3['mass_to_charge']
                count_mz = 0
                sum_mz = 0
                for massz in fileObj:
                    if massz >= bin_left and massz < bin_right:
                        count_mz = count_mz + 1
                        sum_mz += massz 
                mean_massz = sum_mz / count_mz
                print(str(round(bin_left,2)).ljust(15), str(round(bin_right,2)).ljust(15), str(count_mz).ljust(15),str(round(mean_massz,3)).ljust(15), file = t4_results)
                
                
# if user defines full and enzyme
    else:
        cond7 = task4dat['enzyme']==args.enzyme
        data4= task4dat[cond7]
        
        #if user defines full, enzyme, not sequence
        if args.sequence == "":
            print("Mass to charge for data in default 1000Da-1500Da limits and defined enzyme is: ",data4['mass_to_charge'].mean()," Da", file = t4_results)
            print("Total number of peptides for data in default 1000Da-1500Da limits and defined enzyme is: ", data4['mass_to_charge'].count(), file = t4_results)
            print("bin_left \t bin_right \t number_peps \t mean_mz", file = t4_results)
            bin_width = (args.maximum-args.minimum)/args.binss
            bin_left = 0
            bin_right = 0
            for nbin in range (0, args.binss):
                bin_left = args.minimum + (nbin) * bin_width
                bin_right = args.minimum + (nbin+1) * bin_width
                fileObj = data4['mass_to_charge']
                count_mz = 0
                sum_mz = 0
                for massz in fileObj:
                    if massz >= bin_left and massz < bin_right:
                        count_mz = count_mz + 1
                        sum_mz += massz 
                mean_massz = sum_mz / count_mz
                print(str(round(bin_left,2)).ljust(15), str(round(bin_right,2)).ljust(15), str(count_mz).ljust(15),str(round(mean_massz,3)).ljust(15), file = t4_results)
                
        # if user defines full, enzyme and sequence
        else:
            cond8 = data4['sequence'].str.contains(args.sequence, na=False)
            data41 = data4[cond8]
            print("Mass to charge for data in default 1000Da-1500Da limits, defined enzyme and sequence is: ",data41['mass_to_charge'].mean()," Da", file = t4_results)
            print("Total number of peptides for data in default 1000Da-1500Da limits, defined enzyme and sequence is: ", data41['mass_to_charge'].count(), file = t4_results)
            print("bin_left \t bin_right \t number_peps \t mean_mz", file = t4_results)
            bin_width = (args.maximum-args.minimum)/args.binss
            bin_left = 0
            bin_right = 0
            for nbin in range (0, args.binss):
                bin_left = args.minimum + (nbin) * bin_width
                bin_right = args.minimum + (nbin+1) * bin_width
                fileObj = data41['mass_to_charge']
                count_mz = 0
                sum_mz = 0
                for massz in fileObj:
                    if massz >= bin_left and massz < bin_right:
                        count_mz = count_mz + 1
                        sum_mz += massz 
                mean_massz = sum_mz / count_mz
                print(str(round(bin_left,2)).ljust(15), str(round(bin_right,2)).ljust(15), str(count_mz).ljust(15),str(round(mean_massz,3)).ljust(15), file = t4_results)
#if __name__=='__main__':
#    main()    
f.close() #close file
t4_results.close()

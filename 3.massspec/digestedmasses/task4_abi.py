import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', type=str, default='dummy.pepmasses',
    help='Identify the path/location of your file containing peptide masses')
parser.add_argument('-a', '--analysis', type=str, default='range',
    help='Choose your analysis: "full" to analyze whole m/z values, or  "range"  to define a range of values')
parser.add_argument('-r', '--range', type=int, default=(1000, 1500),
    help='Choose your range of values min, max')
parser.add_argument('-o','--output', type=str,
    help='Designate the name of your output file', default='output')
args=parser.parse_args()

def read_masses(filename):
    filename = open(args.filename, 'r')
    lines = filename.readlines()
    masses = [] # create a list for the masses
    for line in lines: # for each line in the file, split the line
        (name,number,mass_to_charge,z,p,enzyme,prot_sequence)=line.split() # objects from list as strings (name,number,mass_to_charge,z,p,enzyme,prot_sequence)=line.split()
        mzf=float(mass_to_charge)
        masses.append(mzf) # add the mass to a list
    return masses

masses=read_masses(args.filename)

def analysis(analysis, range):
    if args.analysis=='range': # if user choose range analysis
        list = args.range
        min = list[0] #can I assign type as int?
        max = list[1] #can I assign type as int?
        # create initial numeber of peptides and sum of mass to calculate mean mass in range
        number_pep=0
        total_mass = 0
        #calculate mean
        for mzf in masses:
            if mzf > min and mzf < max: #mz values within the range given by user
                number_pep = number_pep + 1 #count of events on the given range with IF statement
                total_mass += mzf
                meanmz_inrange = total_mass / number_pep
        result = f'Range {list} has {number_pep} peptides and mean m/z value {meanmz_inrange}'
        return result

result=analysis(args.analysis, args.range)

output=open(f'{args.output}','w')
print(result, file=output)

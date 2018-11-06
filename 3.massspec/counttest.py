
massDictionary = {'A' :  71.08, 'C' : 103.14, 'D' : 115.09,  #dictionary of average isotopic masses 
'E' : 129.12,'F' : 147.18, 'G' :  57.05, 
'H' : 137.14, 'I' : 113.16,'K' : 128.17, 
'L' : 113.16, 'M' : 131.19, 'N' : 114.10,
'P' :  97.12, 'Q' : 128.13, 'R' : 156.19, 
'S' :  87.08,'T' : 101.10, 'V' :  99.13, 
'W' : 186.21, 'Y' : 163.18, '*' : 0.0, 
'H2O' : 18.0153, 'proton' : 1}

charge = 1
aaSeq = 'MQVSR'
residueValue = []
for count in aaSeq:  #for each character in my string 
		protonMass = charge
		residueValue.append(massDictionary[count])   # all these 3 in same command???
		residueValueList = (residueValue)

peptideValue = sum(residueValueList)#adds up th
peptideValue4sf = format(peptideValue, '.4f')  #saves the result to 4dp.
peptideValueFull = float(peptideValue4sf) + charge + massDictionary['H2O']

print(peptideValueFull)
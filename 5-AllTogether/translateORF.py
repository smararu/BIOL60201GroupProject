import sys
# TODO: Handle command line arguments potentialy using argsparse
# Or just error check seeing as its just one argument
filename = sys.argv[1]  

#Constant Nucleotide Table and Complement Table
NUCLEOTIDE_TABLE = {
'ata':'I', 'atc':'I', 'att':'I', 'atg':'START',
'aca':'T', 'acc':'T', 'acg':'T', 'act':'T', 'acn' : 'T', 
'aac':'N', 'aat':'N', 'aaa':'K', 'aag':'K',
'agc':'S', 'agt':'S', 'aga':'R', 'agg':'R',
'cta':'L', 'ctc':'L', 'ctg':'L', 'ctt':'L', 'ctn' : 'L',
'cca':'P', 'ccc':'P', 'ccg':'P', 'cct':'P', 'ccn' : 'P',
'cac':'H', 'cat':'H', 'caa':'Q', 'cag':'Q',  
'cga':'R', 'cgc':'R', 'cgg':'R', 'cgt':'R',
'gta':'V', 'gtc':'V', 'gtg':'V', 'gtt':'V', 'gtn' : 'V',
'gca':'A', 'gcc':'A', 'gcg':'A', 'gct':'A', 'gcn' : 'A',
'gac':'D', 'gat':'D', 'gaa':'E', 'gag':'E', 
'gga':'G', 'ggc':'G', 'ggg':'G', 'ggt':'G', 'ggn' : 'G',
'tca':'S', 'tcc':'S', 'tcg':'S', 'tct':'S', 'tcn' : 'S',
'ttc':'F', 'ttt':'F', 'tta':'L', 'ttg':'L',
'tac':'Y', 'tat':'Y', 'taa':'STOP', 'tag':'STOP', 
'tgc':'C', 'tgt':'C', 'tga':'STOP', 'tgg':'W',
'':'STOP'
    } 

SWITCHER = {
    "a": "t",
    "t": "a",
    "c": "g",
    "g": "c",
    "n": "n"
}

#Obtain the sequence from a FASTA format file, 
#assuming sequences don't start with a >
def getSequence(inputFilename):
    sequence = ''
    with open(inputFilename, "r") as file:
        for line in file: 
            if ">" not in line:
                sequence += line
    sequence = sequence.replace('\n','')
    return sequence

#Obtain the species from a FASTA format file,
#assuming species is on the line with >
def getSpecies(inputFilename):
    species = ''
    with open(inputFilename, "r") as file:
        for line in file:
            if ">" in line:
                species += line
        species = species.replace('\n','')
    return species

# Translate the DNA using the nucleotide lookup table
def translateDNA(translateSequence):
    #Define a couple of temps
    DNA = translateSequence
    tmpProtein = ""
    finalSequence = []
    #Index through the string until the end of DNA, increment of 3 
    for index in range(0, len(DNA), 3):
        #If we've found a Start codon
        if NUCLEOTIDE_TABLE.get(DNA[index:index+3], 'X') == "START" :
            tmpProtein += "M"
            index += 3
            #While we're not at the end of the sequence
            while (NUCLEOTIDE_TABLE.get(DNA[index:index + 3], 'X') != "STOP"):
                #Look-up, default X
                tmpProtein += NUCLEOTIDE_TABLE.get(DNA[index:index + 3], 'X') 
                index += 3 # Increment of 3 because of codons
            # tmpProtein += "*" #add * at the end of these proteins
            finalSequence.append(tmpProtein) 
            tmpProtein = ""
    return finalSequence 

#Translate each possible frame position
#TODO: Make less brute: use hash table
def translateORF(frames):
    #A couple of variables if we want to determine which is the longest (correct) 
    #reading frame
    longestORF = 0
    correctFrame = [0,0]
    translatedFrames = [0] * 6
    #Start generating all the frames
    for frame in frames:
        sequence = getSequence(filename)
        if (frame == 1):
            translatedSequence = translateDNA(sequence) 
            translatedFrames[frame-1] = translatedSequence
            maxLen = max([len(index) for index in translatedSequence])
            if maxLen > longestORF:
                longestORF = maxLen
                correctFrame[0] = frame
                correctFrame[1] = "3'5 Frame 1" 
        elif (frame == 2):
            sequence = sequence[1:] + sequence[0]
            translatedSequence = translateDNA(sequence) 
            translatedFrames[frame-1] = translatedSequence
            maxLen = max([len(index) for index in translatedSequence])
            if maxLen > longestORF:
                longestORF = maxLen
                correctFrame[0] = frame
                correctFrame[1] = "3'5 Frame 2"
        elif (frame == 3):
            sequence = getSequence(filename)
            sequence = sequence[2:] + sequence[0:2]
            translatedSequence = translateDNA(sequence) 
            translatedFrames[frame-1] = translatedSequence
            maxLen = max([len(index) for index in translatedSequence])
            if maxLen > longestORF:
                longestORF = maxLen
                correctFrame[0] = frame
                correctFrame[1] = "3'5 Frame 3"
        elif (frame == 4):
            sequence = sequenceComplement(sequence[::-1])
            translatedSequence = translateDNA(sequence) 
            translatedFrames[frame-1] = translatedSequence
            maxLen = max([len(index) for index in translatedSequence])
            if maxLen > longestORF:
                longestORF = maxLen
                correctFrame[0] = frame
                correctFrame[1] = "3'5 Frame 1"
        elif (frame == 5):
            sequence = sequence[1:] + sequence[0]
            sequence = sequenceComplement(sequence[::-1])
            translatedSequence = translateDNA(sequence) 
            translatedFrames[frame-1] = translatedSequence
            maxLen = max([len(index) for index in translatedSequence])
            if maxLen > longestORF:
                longestORF = maxLen
                correctFrame[0] = frame
                correctFrame[1] =  "3'5 Frame 2"
        elif (frame == 6):
            sequence = sequence[2:] + sequence[0:2]
            sequence = sequenceComplement(sequence[::-1])
            translatedSequence = translateDNA(sequence) 
            translatedFrames[frame-1] = translatedSequence
            maxLen = max([len(index) for index in translatedSequence])
            if maxLen > longestORF:
                longestORF = maxLen
                correctFrame[0] = frame
                correctFrame[1] = "3'5 Frame 3"
    # Code that tells us which is the correct frame
    # print  ("Longest ORF: " + str(longestORF) + " amino acids" )   
    # print ("The correct frame is frame : " + correctFrame[1] + " (" + str(correctFrame[0])
    #     + ")")     
    return translatedFrames


#Function to derive complement of a sequence, using look-up table
def sequenceComplement(sequence):
    complementSequence = ''
    for nucleotide in sequence:
        complementSequence += SWITCHER[nucleotide]
    return complementSequence


#Actual outpul function - 
#This would have to be tweaked to account for different files, in the initial read
def PrintToFile(outFile, framedSequence):
    numberOfFrames = len(framedSequence)
    # outputFile = "outputFile.txt"
    with open(outFile, 'w') as f:
        
        # print('Filename:', outputFile, file=f) 
        for frameNumber, frames in enumerate(framedSequence):
            frameNumber = framedSequence.index(frames) #change index
            for openReadingFrame, aminoAcids in enumerate(frames):
                print (">CLAUD_F" + str(frameNumber+1) + "_" 
                    + str(openReadingFrame+1).zfill(4), file=f) #NAME_FRAME_ORF
                print (aminoAcids, file=f)
    
finalFrames = 0
finalFrames = translateORF(range(1,7))
# print (finalFrames)
PrintToFile("realDummy.peps", finalFrames)

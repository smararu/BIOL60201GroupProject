import sys
# print ("This is the name of the script: ", sys.argv[0])
# print ("Number of arguments: ", len(sys.argv))
# print ("The arguments are: " , str(sys.argv))
# try:
userFileName = sys.argv[1]  
#     line = userFileName.readline()
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise
def getSequence(inputFilename):
    sequence = ''
    file = open(inputFilename, "r")
    for line in file:
        if ">" not in line:
            sequence += line
    sequence = sequence.replace('\n','')
    return (sequence)

def getSpecies(inputFilename):
    species = ''
    file = open(inputFilename, "r")
    for line in file:
        if ">" in line:
            species += line
    species = species.replace('\n','')
    return (species)
    # with open(inputFilename) as fp:
    #     for record in genomeSequence:
    #         name, sequence = record.id, str(record.seq) 
    # return(sequence)
def TranslateDNA(translateSequence):
    nucleotideTable = {
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
    DNA = translateSequence
    # DNA = "tttatggcaattaaaattggtatcaatggttttggtcgtatcggccgtatcgtattctagttttttttttttatggcaattaaaattggtatcaatggttttggtcgtatcggccgtatcgtattctagttttttttt"
    # DNA = translateSequence
    tmpProtein = ""
    finalSequence = []
    #Index through the string until the end of DNA, increment of 3 
    for index in range(0, len(DNA), 3):
        #If we've found a Start codon
        try:
            if nucleotideTable[DNA[index:index+3]] == "START" :
            # tmpProtein += nucleotideTable[DNA[index:index + 3]]
                tmpProtein += "M"
                index += 3
                while (nucleotideTable[DNA[index:index + 3]] != "STOP"):
                    if DNA[index:index + 3] in nucleotideTable:
                        tmpProtein += nucleotideTable[DNA[index:index + 3]]
                    index += 3
                finalSequence.append(tmpProtein) 
                tmpProtein = ""
        except KeyError:
            tmpProtein += "X"
       
    return (finalSequence)         
def TranslateORF(frames):
    longestORF = 0
    correctFrame = [0,0]
    translatedFrames = [0] * 6

    for frame in frames:
        sequence = getSequence(userFileName)

        if (frame == 1):
            translatedSequence = TranslateDNA(sequence) 
            translatedFrames[frame-1] = translatedSequence
            maxLen = max([len(index) for index in translatedSequence])
            if maxLen > longestORF:
                longestORF = maxLen
                correctFrame[0] = frame
                correctFrame[1] = "3'5 Frame 1" 
        elif (frame == 2):
            sequence = sequence[1:] + sequence[0]
            translatedSequence = TranslateDNA(sequence) 
            translatedFrames[frame-1] = translatedSequence
            maxLen = max([len(index) for index in translatedSequence])
            if maxLen > longestORF:
                longestORF = maxLen
                correctFrame[0] = frame
                correctFrame[1] = "3'5 Frame 2"
        elif (frame == 3):
            sequence = getSequence(userFileName)
            sequence = sequence[2:] + sequence[0:2]
            translatedSequence = TranslateDNA(sequence) 
            translatedFrames[frame-1] = translatedSequence
            maxLen = max([len(index) for index in translatedSequence])
            if maxLen > longestORF:
                longestORF = maxLen
                correctFrame[0] = frame
                correctFrame[1] = "3'5 Frame 3"
        elif (frame == 4):
            sequence = SequenceComplement(sequence[::-1])
            translatedSequence = TranslateDNA(sequence) 
            translatedFrames[frame-1] = translatedSequence
            maxLen = max([len(index) for index in translatedSequence])
            if maxLen > longestORF:
                longestORF = maxLen
                correctFrame[0] = frame
                correctFrame[1] = "3'5 Frame 1"
        elif (frame == 5):
            sequence = sequence[1:] + sequence[0]
            sequence = SequenceComplement(sequence[::-1])
            translatedSequence = TranslateDNA(sequence) 
            translatedFrames[frame-1] = translatedSequence
            maxLen = max([len(index) for index in translatedSequence])
            if maxLen > longestORF:
                longestORF = maxLen
                correctFrame[0] = frame
                correctFrame[1] =  "3'5 Frame 2"
        elif (frame == 6):
            sequence = sequence[2:] + sequence[0:2]
            sequence = SequenceComplement(sequence[::-1])
            translatedSequence = TranslateDNA(sequence) 
            translatedFrames[frame-1] = translatedSequence
            maxLen = max([len(index) for index in translatedSequence])
            if maxLen > longestORF:
                longestORF = maxLen
                correctFrame[0] = frame
                correctFrame[1] = "3'5 Frame 3"

    # print  ("Longest ORF: " + str(longestORF) + " amino acids" )   
    # print ("The correct frame is frame : " + correctFrame[1] + " (" + str(correctFrame[0])
    #     + ")")     
    return(translatedFrames)



def SequenceComplement(sequence):
    switcher = {
        "a": "t",
        "t": "a",
        "c": "g",
        "g": "c",
        "n": "n"
    }
    complementSequence = ''
    for nucleotide in sequence:
        complementSequence += switcher[nucleotide]
    return (complementSequence)

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

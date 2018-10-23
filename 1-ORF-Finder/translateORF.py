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
    'aca':'T', 'acc':'T', 'acg':'T', 'act':'T',
    'aac':'N', 'aat':'N', 'aaa':'K', 'aag':'K',
    'agc':'S', 'agt':'S', 'aga':'R', 'agg':'R',
    'cta':'L', 'ctc':'L', 'ctg':'L', 'ctt':'L',
    'cca':'P', 'ccc':'P', 'ccg':'P', 'cct':'P',
    'cac':'H', 'cat':'H', 'caa':'Q', 'cag':'Q',
    'cga':'R', 'cgc':'R', 'cgg':'R', 'cgt':'R',
    'gta':'V', 'gtc':'V', 'gtg':'V', 'gtt':'V',
    'gca':'A', 'gcc':'A', 'gcg':'A', 'gct':'A',
    'gac':'D', 'gat':'D', 'gaa':'E', 'gag':'E',
    'gga':'G', 'ggc':'G', 'ggg':'G', 'ggt':'G',
    'tca':'S', 'tcc':'S', 'tcg':'S', 'tct':'S',
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
    print (finalSequence)         
# TranslateDNA('genomeShort.fasta')
def TranslateORF(frames):
    sequence = getSequence('genomeShort.fasta')
    for frame in frames:
        sequence = getSequence('genomeShort.fasta')

        if (frame == 1):
            print ("5'3' Frame 1")
            TranslateDNA(sequence)
            print ('\n')
        elif (frame == 2):
            print ("5'3' Frame 2")
            sequence = sequence[1:] + sequence[0]
            TranslateDNA(sequence)
            print ('\n')
        elif (frame == 3):
            sequence = getSequence('genomeShort.fasta')
            print ("5'3' Frame 3")
            sequence = sequence[2:] + sequence[0:2]
            TranslateDNA(sequence)
            print ('\n')
        elif (frame == 4):
            print ("3'5 Frame 1")
            sequence = SequenceComplement(sequence[::-1])
            TranslateDNA(sequence)
            print ('\n')
        elif (frame == 5):
            print ("3'5 Frame 2")
            sequence = sequence[1:] + sequence[0]
            sequence = SequenceComplement(sequence[::-1])
            TranslateDNA(sequence)
            print ('\n')
        elif (frame == 6):
            print ("3'5 Frame 3")
            sequence = sequence[2:] + sequence[0:2]
            sequence = SequenceComplement(sequence[::-1])
            TranslateDNA(sequence)
            print ('\n')
def SequenceComplement(sequence):
    switcher = {
        "a": "t",
        "t": "a",
        "c": "g",
        "g": "c",
    }
    complementSequence = ''
    for nucleotide in sequence:
        complementSequence += switcher[nucleotide]
    return (complementSequence)


TranslateORF(range(1,7))


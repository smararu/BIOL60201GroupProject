def TranslateDNA(sequence):
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
    }
    #fileName = genome.fasta
    DNA = sequence
    DNA = "tttatggcaattaaaattggtatcaatggttttggtcgtatcggccgtatcgtattctagttttttttttttatggcaattaaaattggtatcaatggttttggtcgtatcggccgtatcgtattctagttttttttt"
    startCodon = ["atg"]
    stopCodon = ["tga', 'tag', 'taa"]
    tmpProtein = ""
    finalSequence = []

    #Index through the string until the end of DNA, increment of 3 
    for index in range(0, len(DNA), 3):
        #If we've found a Start codon
        if nucleotideTable[DNA[index:index+3]] == "START" :
            index += 3
            while (nucleotideTable[DNA[index:index + 3]] != "STOP"):
                if DNA[index:index + 3] in nucleotideTable:
                    tmpProtein += nucleotideTable[DNA[index:index + 3]]
                index += 3
            finalSequence.append(tmpProtein) 
            tmpProtein = ""



TranslateDNA(sequence)
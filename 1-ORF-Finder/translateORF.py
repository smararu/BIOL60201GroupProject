import sys

# TODO: Handle command line arguments potentially using argsparse
# Or just error check seeing as its just one argument
filename = sys.argv[1]

# Constant Nucleotide Table and Complement Table
NUCLEOTIDE_TABLE = {
    'ata': 'I', 'atc': 'I', 'att': 'I', 'atg': 'M',
    'aca': 'T', 'acc': 'T', 'acg': 'T', 'act': 'T', 'acn': 'T',
    'aac': 'N', 'aat': 'N', 'aaa': 'K', 'aag': 'K',
    'agc': 'S', 'agt': 'S', 'aga': 'R', 'agg': 'R',
    'cta': 'L', 'ctc': 'L', 'ctg': 'L', 'ctt': 'L', 'ctn': 'L',
    'cca': 'P', 'ccc': 'P', 'ccg': 'P', 'cct': 'P', 'ccn': 'P',
    'cac': 'H', 'cat': 'H', 'caa': 'Q', 'cag': 'Q',
    'cga': 'R', 'cgc': 'R', 'cgg': 'R', 'cgt': 'R',
    'gta': 'V', 'gtc': 'V', 'gtg': 'V', 'gtt': 'V', 'gtn': 'V',
    'gca': 'A', 'gcc': 'A', 'gcg': 'A', 'gct': 'A', 'gcn': 'A',
    'gac': 'D', 'gat': 'D', 'gaa': 'E', 'gag': 'E',
    'gga': 'G', 'ggc': 'G', 'ggg': 'G', 'ggt': 'G', 'ggn': 'G',
    'tca': 'S', 'tcc': 'S', 'tcg': 'S', 'tct': 'S', 'tcn': 'S',
    'ttc': 'F', 'ttt': 'F', 'tta': 'L', 'ttg': 'L',
    'tac': 'Y', 'tat': 'Y', 'taa': 'STOP', 'tag': 'STOP',
    'tgc': 'C', 'tgt': 'C', 'tga': 'STOP', 'tgg': 'W',
    '': 'STOP'
}

SWITCHER = {
    "a": "t",
    "t": "a",
    "c": "g",
    "g": "c",
    "n": "n"
}


# Obtain the sequence from a FASTA format file,
# assuming sequences don't start with a >
def get_sequence(infile):
    sequence = ''
    with open(infile, "r") as file:
        for line in file:
            if ">" not in line:
                sequence += line
    sequence = sequence.replace('\n', '')
    return sequence


# Obtain the species from a FASTA format file,
# assuming species is on the line with >
def get_species(infile):
    species = ''
    with open(infile, "r") as file:
        for line in file:
            if ">" in line:
                species += line
        species = species.replace('\n', '')
    return species


# Translate the dna using the nucleotide lookup table
def translate_dna(translate_sequence):
    # Define a couple of temps
    dna = translate_sequence
    tmp_protein = ""
    final_sequence = []
    # Index through the string until the end of dna, increment of 3
    for index in range(0, len(dna), 3):
        # If we've found a Start codon
        if NUCLEOTIDE_TABLE.get(dna[index:index + 3], 'X') == "M":
            tmp_protein += "M"
            index += 3
            # While we're not at the end of the sequence
            while NUCLEOTIDE_TABLE.get(dna[index:index + 3], 'X') != "STOP":
                # Look-up, default X
                tmp_protein += NUCLEOTIDE_TABLE.get(dna[index:index + 3], 'X')
                index += 3  # Increment of 3 because of codons
            # tmp_protein += "*" #add * at the end of these proteins
            final_sequence.append(tmp_protein)
            tmp_protein = ""
    return final_sequence


# frame_shift function, grouping 1 and 4, 2 and 5, 3 and 6
def frame_shift(frame, sequence):
    if frame == 1 or frame == 4:
        pass
    elif frame == 2 or frame == 5:
        sequence = sequence[1:] + sequence[0]
    elif frame == 3 or frame == 6:
        sequence = sequence[2:] + sequence[0:2]

    return sequence


# Made more compact but no longer keeps track of max length,
# Could be re-implemented using the commented code and a hash / frame object
def translate_orf(orf_frames):
    # A couple of variables if we want to determine which is the longest (correct)
    # reading frame
    # longest_orf = 0
    # correct_frame = [0, 0]
    translated_frames = [0] * 6
    # Start generating all the frames

    for frame in orf_frames:
        sequence = get_sequence(filename)
        sequence = frame_shift(frame, sequence)
        if frame > 3:
            sequence = sequence_complement(sequence[::-1])
        translated_sequence = translate_dna(sequence)
        # noinspection PyTypeChecker
        translated_frames[frame - 1] = translated_sequence

    # Code that tells us which is the correct frame
    # print  ("Longest ORF: " + str(longest_orf) + " amino acids" )   
    # print ("The correct frame is frame : " + correct_frame[1] + " (" + str(correct_frame[0])
    #     + ")")     
    return translated_frames


# Function to derive complement of a sequence, using look-up table
def sequence_complement(sequence):
    complement_sequence = ''
    for nucleotide in sequence:
        complement_sequence += SWITCHER[nucleotide]
    return complement_sequence


# Actual output function -
# This would have to be tweaked to account for different files, in the initial read
def print_to_file(outfile, framed_sequence):
    # outputFile = "outputFile.txt"
    with open(outfile, 'w') as f:
        # Example print:  print('Filename:', outputFile, file=f)
        for frame_number, frames in enumerate(framed_sequence):
            frame_number = framed_sequence.index(frames)  # change index
            for openReadingFrame, aminoAcids in enumerate(frames):
                print(">CLAUD_F" + str(frame_number + 1) + "_"
                      + str(openReadingFrame + 1).zfill(4), file=f)  # NAME_FRAME_ORF
                print(aminoAcids, file=f)


final_frames = translate_orf(range(1, 7))
# print (final_frames)
i = 0
for results in final_frames:
    i += 1
    print(str(i) + str(results) + '\n')

print_to_file("realDummy.peps", final_frames)

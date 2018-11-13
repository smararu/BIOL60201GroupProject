import re, argparse, sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_input', type=argparse.FileType('r'), default=sys.stdin,
        help='the filename of .fasta file containing protein sequence(s) (defaults to standard input).')
    parser.add_argument('-e', '--enzyme',
        help='the name of an enzyme [t,l,a,e] (defaults to t).', type=str, default='t')
    parser.add_argument('-m','--missed', type=int,
        help='an integer value for number of missed cleavages[0-n] (defaults to 0).', default=0)
    parser.add_argument('-o','--output', type=argparse.FileType('w'),
        help='the output name of the file (defaults to standard output).', default=sys.stdout)
    args=parser.parse_args()
    return args

def read_proteins(file_input): #processes lines in .fasta file into a list of 2-tuples.
    proteins = []
    protein_name = ''
    sequence = ''
    for line_num, line in enumerate(file_input, 1):
        if line.startswith('>'): #header lines in a .fasta file will always begin >
            if sequence:
                proteins.append((protein_name,sequence))
                sequence = '' #sequence is reset to an empty string for each new protein
            protein_name = line[1:-1] #removes first > and unwanted newline character at end of header line
        else: #any line not beginning > will be sequence in a .fasta file.
            line = line.rstrip('\n*')
            if re.search('[BOUJZ]', line):
                print(f'Warning: unusual amino acid (B,O,U,J,Z) found in {protein_name} on line {line_num}', file=sys.stderr)
            if 'X' in line:
                print(f'Warning: unknown amino acid X found in {protein_name} on line {line_num}', file=sys.stderr)
            sequence += line #appends my sequence line to sequence
    proteins.append((protein_name,sequence))
    return proteins

#create a dictionary consisting of key = enzyme code, and value = cleavage pattern
recog_seq = {
            't' : re.compile('([KR])(?!P)'),
            'l' : re.compile('(K)(?!P)'),
            'a' : re.compile('(R)(?!P)'),
            'e' : re.compile('(E)(?!P)')
    }

def digest(sequence, enzyme):
    peptides = []
    pattern = recog_seq[enzyme]
    peptides_unpaired = re.split(pattern, sequence)
    peptide = zip(peptides_unpaired[::2], peptides_unpaired[1::2]) #run zip on seq_peptides to put pairs together.
    for i, j in peptide:
        full_peptide = i + j
        peptides.append(full_peptide)
    if peptides_unpaired[-1]: #if the cleavage site is not at the end of the protein, zip will leave off the final peptide.
        peptides.append(peptides_unpaired[-1])
    return peptides

def missed(peptides, missed):
    full_peptides = []
    for n in range(1, missed + 2):
        for i in range(len(peptides) - n + 1):
            peptides_to_add = peptides[i:i+n]
            full_peptides.append(''.join(peptides_to_add))
    return full_peptides

def output(output, protein_name, full_peptides):
    peptide_num = 0
    for peptide in full_peptides:
        peptide_num += 1
        print(f">{protein_name}\t{peptide_num}\tmissed={args.missed}\t{args.enzyme}\n{peptide}", file = output_peptides)
    return output_peptides

def main():
    args = parse_args()
    for protein_name, sequence in read_proteins(args.file_input):
        peptides = digest(sequence, args.enzyme)
        full_peptides = missed(peptides, args.missed)
        output_peptides = output(args.output, protein_name, full_peptides)

if __name__ == '__main__':
    main()

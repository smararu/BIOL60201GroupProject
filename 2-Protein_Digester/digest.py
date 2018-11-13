import re, argparse, sys

def parse_args():
    parser = argparse.ArgumentParser(description=
    'digest.py reads in a file of .fasta format, a user-specified choice of enzyme, '
    'a user-specified number of missed cleavages, and outputs in .fasta format')
    parser.add_argument('-f', '--file_input', type=argparse.FileType('r'), default=sys.stdin,
        help='the filename of .fasta file containing protein sequence(s) (defaults to standard input).')
    parser.add_argument('-e', '--enzyme', type=str, choices=recog_seq.keys(), default='t',
        help='the name of an enzyme [t,l,a,e] (defaults to t).')
    parser.add_argument('-m','--missed', type=int, default=0,
        help='an integer value for number of missed cleavages[0-n] (defaults to 0).')
    parser.add_argument('-o','--output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
        help='the output name of the file (defaults to standard output).')
    args=parser.parse_args()
    return args

#processes lines in .fasta file into a list of 2-tuples.
def read_proteins(file_input):
    proteins = []
    protein_name = ''
    sequence = ''
    for line_num, line in enumerate(file_input, 1):
        #header lines in a .fasta file will always begin >, so we can use this to identify protein name.
        if line_num == 1 and not line.startswith('>'):
            print(f'Fatal error: your input is not a .fasta file.', file=sys.stderr)
            sys.exit(1)
        if line.startswith('>'):
            if sequence:
                proteins.append((protein_name,sequence))
                #sequence is reset for each new protein
                sequence = ''
            #removes first > and unwanted newline character at end of header line
            protein_name = line[1:-1]
        #any line not beginning > will be sequence in a .fasta file.
        else:
            line = line.rstrip('\n*')
            if re.search('[BOUJZ]', line):
                print(f'Warning: unusual amino acid (B,O,U,J,Z) found in {protein_name} on line {line_num}', file=sys.stderr)
            if 'X' in line:
                print(f'Warning: unknown amino acid X found in {protein_name} on line {line_num}', file=sys.stderr)
            #appends my sequence line to sequence
            sequence += line
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
    # Run zip on seq_peptides to put pairs together.
    peptides_paired = zip(peptides_unpaired[::2], peptides_unpaired[1::2])
    peptides = [p+c for p,c in peptides_paired]
    # If the cleavage site is not at the end of the protein, zip will leave off the final peptide, so we add it.
    if peptides_unpaired[-1]:
        peptides.append(peptides_unpaired[-1])
    return peptides

# If missed > total number of cleavage points (len(peptides - 1)), a warning is printed.
def combine(peptides, missed, protein_name):
    if missed > len(peptides) -1:
        print(f'Warning: number of missed cleavages > '
        f'total cleavage sites in {protein_name}.', file=sys.stderr)
    full_peptides = []
    for n in range(1, missed + 2):
        for i in range(len(peptides) - n + 1):
            peptides_to_add = peptides[i:i+n]
            full_peptides.append(''.join(peptides_to_add))
    return full_peptides

def output(peptides, protein_name, missed, enzyme, output):
    for peptide_num, peptide in enumerate(peptides, 1):
        print(f">{protein_name} {peptide_num} missed={missed} {enzyme}\n{peptide}", file = output)

def main():
    args = parse_args()
    for protein_name, sequence in read_proteins(args.file_input):
        peptides = digest(sequence, args.enzyme)
        full_peptides = combine(peptides, args.missed, protein_name)
        output(full_peptides, protein_name, args.missed, args.enzyme, args.output)

if __name__ == '__main__':
    main()

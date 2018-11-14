import re, argparse, sys

def parse_args():
    """Collects and validates command-line arguments."""

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

def read_proteins(file_input):
    """Reads amino acid sequences in .fasta format (checking for errors), and
    returns a list of proteins [(name, sequence) ...]."""

    proteins = []
    protein_name = ''
    sequence = ''
    for line_num, line in enumerate(file_input, 1):
        line = line.rstrip()
        if line.startswith('>'): # header line
            if sequence:
                proteins.append((protein_name,sequence))
            elif protein_name: # no sequence since last header line
                print(f'Error: empty sequence at line {line_num}', file=sys.stderr)
                sys.exit(1)
            sequence = ''
            protein_name = line[1:]
        elif re.fullmatch('[A-Z]*\*?', line): # sequence line
            if not protein_name: # if no header line
                print(f'Error: no header line at line {line_num}', file=sys.stderr)
                sys.exit(1)
            if re.search('[BOUJZ]', line): # unusual amino acid in line
                print(f'Warning: unusual amino acid (B,O,U,J,Z) found in {protein_name} on line {line_num}', file=sys.stderr)
            if 'X' in line: # unknown amino acid in line
                print(f'Warning: unknown amino acid X found in {protein_name} on line {line_num}', file=sys.stderr)
            sequence += line.rstrip('*')
            if line[-1] == '*': #reset protein name at end of protein
                proteins.append((protein_name,sequence))
                protein_name = ''
                sequence =''
        else: #unrecognised line
            print(f'Error: Bad line at line {line_num}.', file=sys.stderr)
            sys.exit(1)
        if protein_name:
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
    """Takes a protein sequence and uses a regular expression pattern keyed to a
    user-specified enzyme code to split the sequence, and returns a list of peptides."""

    peptides = []
    pattern = recog_seq[enzyme]
    peptides_unpaired = re.split(pattern, sequence)
    # Run zip on peptides_unpaired to produce a list of pairs ([peptide, cleavage pattern], ...)
    peptides_paired = zip(peptides_unpaired[::2], peptides_unpaired[1::2])
    #combines each peptide (p) and matched cleavage pattern (c)
    peptides = [p+c for p,c in peptides_paired]
    # If the cleavage site is not at the end of the protein, zip will leave off the final peptide, so we add it.
    if peptides_unpaired[-1]:
        peptides.append(peptides_unpaired[-1])
    return peptides

# If missed > total number of cleavage points (len(peptides - 1)), a warning is printed.
def missed_cleavages(peptides, missed, protein_name):
    """outputs list of peptides with 0 missed cleavages,
    1 missed cleavage, n missed cleavages."""

    full_peptides = []
    for n in range(1, missed + 2):
        for i in range(len(peptides) - n + 1):
            peptides_to_add = peptides[i:i+n]
            full_peptides.append(''.join(peptides_to_add))
    return full_peptides

def output(peptides, protein_name, missed, enzyme, output):
    """docstring 4."""

    for peptide_num, peptide in enumerate(peptides, 1):
        print(f"{protein_name} {peptide_num} missed={missed} {enzyme}\n{peptide}", file = output)

def main():
    """docstring 5."""

    args = parse_args()
    for protein_name, sequence in read_proteins(args.file_input):
        peptides = digest(sequence, args.enzyme)
        full_peptides = missed_cleavages(peptides, args.missed, protein_name)
        output(full_peptides, protein_name, args.missed, args.enzyme, args.output)

if __name__ == '__main__':
    main()

# digest.py reads a .fasta format file containing protein amino acid sequences,
# splits each protein sequence at the cleavage points for a user-specified enzyme,
# concatenates resulting peptides and outputs a combined list of peptides 0-n missed
# cleavages with accompanying header lines in .fasta format.

import re
import argparse
import sys

def parse_args():
    """Collects and validates command-line arguments."""

    parser = argparse.ArgumentParser(description=
    """digest.py reads a file of .fasta format, a user-specified choice of enzyme [t = trypsin,
    l = endoproteinase Lys-C, a = endoproteinase Arg-C, e = V8 proteinase (Glu-C)], a user-specified
    number of missed cleavages [0-6], and outputs in .fasta format""")
    parser.add_argument('-f', '--file_input', type=argparse.FileType('r'), default=sys.stdin,
        help='the filename of .fasta file containing protein sequence(s) (defaults to standard input).')
    parser.add_argument('-e', '--enzyme', type=str, choices=recog_seq.keys(), default='t',
        help='the 1 letter code for an enzyme [t,l,a,e] (defaults to t).')
    parser.add_argument('-m','--missed', type=int, choices=range(0,7), default=0,
        help='an integer value for number of missed cleavages[0-6] (defaults to 0).')
    parser.add_argument('-o','--output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
        help='the output name of the file (defaults to standard output).')
    return parser.parse_args()

def read_proteins(file_input):
    """Reads amino acid sequences in .fasta format (checking for errors), and
    returns a list of proteins [(name, sequence) ...]."""

    proteins = []
    protein_name = ''
    sequence = ''
    # iterates over lines in file, counts line number
    for line_num, line in enumerate(file_input, 1):
        line = line.rstrip()
        # identifies header line
        if line.startswith('>'):
            if sequence:
                proteins.append((protein_name,sequence))
            elif protein_name:
                print(f'Error: empty sequence at line {line_num}', file=sys.stderr)
                sys.exit(1)
            sequence = ''
            protein_name = line[1:]
        # identifies sequence line
        elif re.fullmatch('[A-Z]*\*?', line):
            if not protein_name:
                print(f'Error: no header line at line {line_num}', file=sys.stderr)
                sys.exit(1)
            # warning for unusual amino acids in line
            if re.search('[BOUJZ]', line):
                print(f'''Warning: unusual amino acid (B,O,U,J,Z) found in
                {protein_name} on line {line_num}''', file=sys.stderr)
            # warning for unknown amino acids in line
            if 'X' in line:
                print(f'''Warning: unknown amino acid X found in {protein_name}
                on line {line_num}''', file=sys.stderr)
            sequence += line.rstrip('*')
            # appends full protein, resets protein name at end of protein
            if line[-1] == '*':
                proteins.append((protein_name,sequence))
                protein_name = ''
                sequence =''
        # exit with error message if line is unrecognised type
        else:
            print(f'Error: Bad line at line {line_num}.', file=sys.stderr)
            sys.exit(1)
    if protein_name:
        proteins.append((protein_name,sequence))
    return proteins

# dictionary where key = 1 letter enzyme code, and value = cleavage pattern
recog_seq = {
            't' : re.compile('([KR])(?!P)'),
            'l' : re.compile('(K)(?!P)'),
            'a' : re.compile('(R)(?!P)'),
            'e' : re.compile('(E)(?!P)')
    }

def digest(sequence, enzyme):
    """Splits a protein sequence at the cleavage points for a user-specified enzyme,
    returns a list of peptide sequences."""

    peptides = []
    pattern = recog_seq[enzyme]
    # split protein sequence at pattern and return a list [(peptide, pattern, peptide...)]
    peptides_unpaired = re.split(pattern, sequence)
    # zip pairs each peptide with the adjacent following pattern
    peptides_paired = zip(peptides_unpaired[::2], # peptides
                          peptides_unpaired[1::2]) #cleavage patterns
    peptides = [p+c for p,c in peptides_paired]
    # if protein ends with a peptide not a pattern, zip ignores it, so we add it here.
    if peptides_unpaired[-1]:
        peptides.append(peptides_unpaired[-1])
    return peptides

def missed_cleavages(peptides, missed, protein_name):
    """Concatenates peptides and returns a combined list of peptides with 0-n missed
    cleavages."""

    combined_peptides = []
    for n in range(1, missed + 2): # number of peptides to combine
        for i in range(len(peptides) - n + 1): # index of first peptide to combine
            peptides_to_add = peptides[i:i+n]
            combined_peptides.append(''.join(peptides_to_add))
    return combined_peptides

def output(peptides, output_file, protein_name, missed, enzyme):
    """Outputs for each peptide a header line containing protein name, peptide
    number, maximum number of missed cleavages, enzyme used for digest, and a
    sequence line."""

    for peptide_num, peptide in enumerate(peptides, 1):
        print(f"{protein_name} {peptide_num} missed={missed} {enzyme}\n{peptide}", file = output_file)

def main():
    """Takes user-specified command-line arguments and executes read_proteins, digest,
    missed_cleavages and outputs a complete set of peptides."""

    args = parse_args()
    for protein_name, sequence in read_proteins(args.file_input):
        peptides = digest(sequence, args.enzyme)
        combined_peptides = missed_cleavages(peptides, args.missed, protein_name)
        output(combined_peptides, args.output, protein_name, args.missed, args.enzyme)

if __name__ == '__main__':
    main()

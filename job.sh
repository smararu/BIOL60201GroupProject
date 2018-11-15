#!/usr/bin/env bash
python3 ./1-ORF-Finder/translateORF.py ./1-ORF-Finder/genome.fasta &&
python3.6	./2-Protein_Digester/digest.py -f ./1-ORF-Finder/outputFile.txt -e e -o digested_e.fasta &&
python3 ./3.massspec/massspec.py -f 2-Protein_Digester/digested_e.fasta &&
python3 ./Task4/Task4_final1.py -Z e

# 2) Defaults for my options:
# 	-f filename default is sys.stdin
# 	-e enzyme default is t
# 	-m missed default is 0
# 	-o output default is sys.stdout
# 3) python3 ./3.massspec/massspec.py -f digested_e.fasta 
# 	digested_l.fasta digested_t.fasta digested_a.fasta   outputs as .masses
# 4) python3 ./Task4/Task4_final1.py  -N range/full -I: minimum -X: maximum 
	# -Z a e l t (enzyme)	[-S] specific sequence -B bins - default 30
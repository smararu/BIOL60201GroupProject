#!/usr/bin/env bash
python3 	translateORF.py genome.fasta &&
python3.6 	digest.py 	-f realDummy.peps -e e -o digested_e.fasta &&
python3.6 	digest.py 	-f realDummy.peps -e t -o digested_t.fasta &&
python3.6 	digest.py 	-f realDummy.peps -e l -o digested_l.fasta &&
python3.6 	digest.py 	-f realDummy.peps -e a -o digested_a.fasta &&
python3 	massspec.py -f digested_e.fasta &&
python3 	massspec.py -f digested_t.fasta &&
python3 	massspec.py -f digested_l.fasta &&
python3 	massspec.py -f digested_a.fasta &&
python3 	Task4_final1.py 

# 2) Defaults for my options:
# 	-f filename default is sys.stdin
# 	-e enzyme default is t
# 	-m missed default is 0
# 	-o output default is sys.stdout
# 3) python3 ./3.massspec/massspec.py -f digested_e.fasta 
# 	digested_l.fasta digested_t.fasta digested_a.fasta   outputs as .masses
# 4) python3 ./Task4/Task4_final1.py  -N range/full -I: minimum -X: maximum 
	# -Z a e l t (enzyme)	[-S] specific sequence -B bins - default 30
#!/usr/bin/env bash
# #Standard Behaviour
# python3 	translateORF.py genome.fasta &&
# python3.6 	digest.py 	-f realDummy.peps -e e -o digested_e.fasta &&
# python3.6 	digest.py 	-f realDummy.peps -e -m 1 t -o digested_t.fasta &&
# python3.6 	digest.py 	-f realDummy.peps -e -m 1 l -o digested_l.fasta &&
# python3.6 	digest.py 	-f realDummy.peps -e -m 1 a -o digested_a.fasta &&
# python3 	massspec.py -f digested_e.fasta &&
# python3 	massspec.py -f digested_t.fasta &&
# python3 	massspec.py -f digested_l.fasta &&
# python3 	massspec.py -f digested_a.fasta &&
# python3 	Task4_final1.py & 

#Peptide/protein stats
# python3 	translateORF.py genome.fasta &&
# python3.6 	digest.py 	-f realDummy.peps -e e -o digested_e.fasta &&
# python3.6 	digest.py 	-f realDummy.peps -e t -m 1  -o digested_t.fasta &&
# python3.6 	digest.py 	-f realDummy.peps -e l -m 1  -o digested_l.fasta &&
# python3.6 	digest.py 	-f realDummy.peps -e a -m 1  -o digested_a.fasta &&
# python3 	massspec.py -f digested_e.fasta -s y &&
# python3 	massspec.py -f digested_t.fasta -s y &&
# python3 	massspec.py -f digested_l.fasta -s y &&
# python3 	massspec.py -f digested_a.fasta -s y &&
# python3 	1500massspec.py -f digested_e.fasta -s y &&
# python3 	1500massspec.py -f digested_t.fasta -s y &&
# python3 	1500massspec.py -f digested_l.fasta -s y &&
# python3 	1500massspec.py -f digested_a.fasta -s y &&
# python3 	Task4_final1.py & 

#
python3 	translateORF.py genome.fasta &&
python3.6 	digest.py 	-f realDummy.peps -e e -o digested_e.fasta &&
python3.6 	digest.py 	-f realDummy.peps -m 1 -e t -o digested_t.fasta &&
python3.6 	digest.py 	-f realDummy.peps -m 1 -e l -o digested_l.fasta &&
python3.6 	digest.py 	-f realDummy.peps -m 1 -e a -o digested_a.fasta &&
python3 	massspec.py -f digested_e.fasta  &&
python3 	massspec.py -f digested_t.fasta  &&
python3 	massspec.py -f digested_l.fasta  &&
python3 	massspec.py -f digested_a.fasta  &&
python3 	Task4_final1.py -B 2500 &
# & &&

# 2) Defaults for my options:
# 	-f filename default is sys.stdin
# 	-e enzyme default is t
# 	-m missed default is 0
# 	-o output default is sys.stdout
# 3) python3 ./3.massspec/massspec.py -f digested_e.fasta 
# 	digested_l.fasta digested_t.fasta digested_a.fasta   outputs as .masses
#	-c charge: should massively impact mass (1,2,3)
#	-t only outputs the end terminal and start terminal peptides
#	-p add phosphate group, should increase mass (yes/no) 
# 4) python3 ./Task4/Task4_final1.py  -N range/full -I: minimum -X: maximum 
	# -Z a e l t (enzyme)	[-S] specific sequence -B bins - default 30

#(DONE)First - standard output which is commented out at the top 

# (DONE)Looked at missed clevages - only show 0, 1, 2

# (DONE) Charge, maybe t (probably not -p)
# (DONE) Ends in Arg (for -t; c - end, n - start) - mention

# (DONE?) Filter for ones that have C (cyst) No difference?

# (DONE ) -bins - defaults at 30 highest accurate would be 2500 (possibly only regular charge)

# start (maybe) 15 (30), 100, 500, 1000,s 2500 

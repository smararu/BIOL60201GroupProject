#!/usr/bin/env bash
# #Standard Behaviour
# python3 	translateORF.py genome.fasta &&
# python3.6 	digest.py 	-f realDummy.peps -e -m 1 e -o digested_e.fasta &&
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
# python3.6 	digest.py 	-f realDummy.peps -e e -m 1  -o digested_e.fasta &&
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
python3.6 	digest.py 	-f realDummy.peps -m 1 -e e -o digested_e.fasta &&
python3.6 	digest.py 	-f realDummy.peps -m 1 -e t -o digested_t.fasta &&
python3.6 	digest.py 	-f realDummy.peps -m 1 -e l -o digested_l.fasta &&
python3.6 	digest.py 	-f realDummy.peps -m 1 -e a -o digested_a.fasta &&
python3 	massspec.py -f digested_e.fasta  &&
python3 	massspec.py -f digested_t.fasta  &&
python3 	massspec.py -f digested_l.fasta  &&
python3 	massspec.py -f digested_a.fasta  &&
python3 	Task4_final1.py -B 2500 &
# & &&

# Task 1
# Only argument is filename

# 						Task 2) digest.py  Arguments: Args tested
# 	-m missed : Number of missed clevages, 0, 2, 3, 4

# 	-f filename default is sys.stdin
# 	-e enzyme default is t
# 	-o output : Name of outputFile 

# 						Task 3) massspec.py
#	-c charge: should massively impact mass (1,2,3)
#	-t only outputs the end terminal and start terminal peptides (n, c)

#	-p add phosphate group, should increase mass (yes/no) 


# 						Task 4) python3 Task4_final1.py 
	#-B bins - default 30 - 15 (30), 100, 500, 1000,s 2500 
	
	# -n range/full  
	#-I: minimum 
	#-X: maximum 
	# -Z a e l t (enzyme)	
	#[-S] specific sequence 


# TASKS
# (DONE) First - standard output which is commented out at the top 

# (DONE) Looked at missed clevages - only show 0, 1, 2

# (DONE) Charge, maybe t (probably not -p)
# (DONE) Ends in Arg (for -t; c - end, n - start) - mention

# (DONE?) Filter for ones that have C (cyst) No difference?

# (DONE ) -bins - defaults at 30 highest accurate would be 2500 (possibly only regular charge)

# start (maybe) 15 (30), 100, 500, 1000,s 2500 

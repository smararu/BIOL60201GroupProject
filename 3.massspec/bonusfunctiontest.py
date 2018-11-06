aaSeq = 'KL'

enzyme = 't'

terminal = 'n'


if terminal == 'n':
	if enzyme == 't':	
		if 'K' in aaSeq[0] and 'P' not in aaSeq[1]:
			print(aaSeq)
		elif 'R' in aaSeq[0] and 'P' not in aaSeq[1]:
			print(aaSeq)
	elif enzyme == 'l':
		if 'K' in aaSeq[0] and 'P' not in aaSeq[1]:
			print(aaSeq)
	elif enzyme == 'a':
		if 'R' in aaSeq[0] and 'P' not in aaSeq[1]:
			print(aaSeq)
	elif enzyme == 'e':
		if 'E' in aaSeq[0] and 'P' not in aaSeq[1]:
			print(aaSeq)
elif terminal == 'c':
	if '*' in aaSeq[-1]:
		print(aaSeq)

#Trypsin: cuts at Lysine (Lys, K) or Arginine (Arg, R) unless the next amino acid is Proline (Pro, P). == t
#Endoproteinase Lys-C: cuts at Lysine (Lys, K) unless the next amino acid is Proline (Pro, P). == l
#Endoproteinase Arg-C: cuts at Arginine (Arg, R) unless the next amino acid is Proline (Pro, P). == a
#V8 proteinase (Glu-C): cuts at Glutamic acid (Glu, E) unless the next amino acid is Proline (Pro, P) == e


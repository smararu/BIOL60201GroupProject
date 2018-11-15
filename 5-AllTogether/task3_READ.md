massspec			User Manuals			massspec


	NAME
		MassSpec - Determine the mass/charge value for digested protein sequences.

	SYNOPSIS

		massspec.py -f [filename] 
			optional arguments: -c [charge] -t [terminal] -i [isotopic masses][-s stats]

	DESCRIPTION
		MassSpec takes enzyme 'digested' peptide sequences, in .fasta format, from task2 and calculates a mass-to-charge value for each sequence, based on known amino acid mass/charge values. By default, average amino masses will be used, however monoisotopic values can be requested. MassSpec also adds a value for water and appropriate proton value (based on charge) Users can select a charge assigned to each peptide of 3, 2 or default, 1, and choose to only output N-terminal or C-terminal peptides. All of the information for each peptide is output to a non-headed table in a '.masses' file, along with number of missed cleavages and enzyme used, which is passed from task2. Users can request an additional stats file, which is a calculation of the average number of peptides per protein, as well as a '.csv' file of the number of peptides per protein.

	FILES
		Input		[file.fasta]
			File name must have '.fasta' suffix and the file contents must be formatted as the standard output from task2.

		Output		[file.masses]	[file.stats][file.csv]
			Main output file name will be in non-headed table format and will take be named as the input file has, with '.masses' suffix replacing .fasta. Optional arguments available output .stats and .csv file for further analysis.
		

	ARGUMENTS
		[-f]	 file	[file.fasta]
			This is the only mandatory argument, user must choose an input file for MassSpec to run. 

		[-c]	 charge		[1][2][3]	default=[1]
			The assigned charge of each peptide. Can take value of [1](default),[2] or [3] and will default to [1]. A value of 1 (representing 1 proton) is added to the mass value for each peptide of charge [1], 2 added to the mass for charge of 2, etc.

		[-i]	 isotopic masses	[a][m]		default=[a]
			The mass values of each amino acid to calculate peptide mass value can be either monoisotopic [m] or average isotopic [a] (default).

		[-t]	 terminal		[n][c][a]	default=[a]
			User can choose to report back only N-terminal [n], C-terminal [c] or all [a] (default) proteins.

		[-p]	phosphorylation		[y][n]		default=[n]
			Uder can choose to 'phosphorylate' (i.e. add the mass of a phosphate group) to Tyr, Trp, and Ser amino acids.

		[-s]	 stats		[y][n]		default=[n]
			User can choose to return 2 files [y], one with average peptides per protein, and a .csv file with the number of peptides for each protein. MassSpec default will not output these files [n]. 

	VERSIONS
		massspec.py		Program main version.	Last updated Nov. 15 2018
		1500massspec.py		Altered to filter out mass/charge values not in 1000-1500 dalton range, in the optional stats output files.

	AUTHOR
		Charles Bannister

	
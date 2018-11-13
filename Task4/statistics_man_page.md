statistics (1) Peptide statistics statistics(1)

NAME
statistics.py - basic statistics for digested peptides using mass-to-charge values

SYNOPSIS
peptide_statistics [--analysis][--minimum] [--maximum][--enzyme][--sequence][--bins]

DESCRIPTION
task4_stats uses mass-to-charge values basic statistics for user defined parameters.

User can define four filters for mass-to-charge values: analysis, minimum, maximum, enzyme and sequence; filters are used in listed order. To visualize for histogram user can define: bins.

Preparation: 

Task 3 four files "*.masses*" were merged into *task3.masses*.
File task3.masses is transformed to data-frame "task3_pd"; this file is filtered for values of mass-to-charge between 1000Da - 1500Da to make it comparable with experimental data from spectrophotometer. Resulting file is task3_for_analysis.

The first filter is range or full, if user choose range then a second filter is required, minimum and maximum values, if not default values are used. With range, two conditions cond1 and cond2 are used to create data1 file from task3_for_analysis. If neither enzyme nor sequence are given, then data 1 is used. If enzyme is not given but sequence is defined, then a condition cond3 is used to create data11 from data1. If enzyme is given a condition cond4 is used to create data2 from data 1. If enzyme is given but not sequence, data 2 is used. If enzyme and sequence are given, a condition cond5 is used to create data21. Mean value of mass, number of peptides, table of filtered data and a histogram are created in task4_results.

If the first filter is full (default), task3_for_analysis is used. If neither enzyme nor sequence is given, task3_for_analysis is used. If enzyme is not defined but sequence is given, a condition cond6 is used to create data3 from task3_for_analysis. If enzyme is given, condition cond7 is used to create data4 from task3_for_analysis. Having enzyme but not sequence data 4 is used. Finally having enzyme and sequence, condition cond8 is used to create data41 from data 4. Mean value of mass, number of peptides, table of filtered data and a histogram are created in task4_results.

OPTIONS

     -N --analysis
          Type of analysis "range" or "full". The first option is for mass-to-charge analysis in shorter
          range between a 1000Da-1500Da, the second option uses all data between 1000Da - 1500Da.
     -I --minimum
          If -N is defined as "range" then this is a Boolean value greater than 1000, but not greater
          than 1500; default value is 1000.

     -X --maximum
          If -N is defined as "range" then this is a Boolean value lower than 1500, but greater than
          1000; default value is 1500. It is preferable a value greater than the minimum.

     -Z --enzyme
          Is an str value deifined by user, it can be t for Trypsine,l for Endoproteinase
          Lys-C, a for Endoproteinase Arg-C, e for V8 proteinase. Only one letter must be write.

     -S --sequence
          Is a str sequence of aminoacids user wants to select within data. Any combination of the
          uppercase letters can be searched: A, C,D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y.

     -B --bins
          Number of bins for histogram. Default value is 30.

FILES
/task3.masses
File from four merged files; it contains peptide name, number of peptide from peptide name, mass-to-charge value in Daltons, z value, p value, enzyme used for digestion, sequence of amino-acids.
~/task4_results.csv
File in csv format for quantitative analysis; it contains a mass-to-charge mean value, number of peptides, a filtered table for parameters given by user (peptide name, number of peptide from peptide name, mass-to-charge value in Daltons, z value, p value, enzyme used for digestion, sequence of amino-acids) and a histogram.

ENVIRONMENT
FOOCONF
If non-null the full pathname for an alternate system
wide foo.conf. Overridden by the -c option.

DIAGNOSTICS
The following diagnostics may be issued on stderr:

     Bad magic number.
          The input file does not look like an archive file.
     Old style baz segments.
          foo  can  only  handle  new  style  baz segments. COBOL
          object libraries are not supported in this version.

BUGS
The command name should have been chosen more carefully to
reflect its purpose.

AUTHOR
Moises Gualapuro <gualapuro dot moises at gmail dot com>

SEE ALSO
bar(1), foo(5), xyzzy(1)

Python Last change: NOVEMBER 2018 1

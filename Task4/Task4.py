Open file Task 3 ('dummy.pepmasses')
Read mass column
  Separate results by frame (Task 1 gives only Frame with the largest peptide?)
  Separate results by enzyme (chose a enzyme from a list?)
  Define mass column ranges (user entry input())
    Define your range, (entry min value input())
    Define your range, (entry max value input())
    or 
  Define number of bins, (how many bins want to visualice in hystogram input())
Count peptides on each range,
  Total number of peptides
    Identify and count peptides with Cys, Met
    Subtotal of peptides with ions (ionA, ionB, ...)
  For mass values on each range or bin, calculate mean values of mass
  Mean of peptides by ions type (ionA, ionB, ...)
Calculate instruments accuracy (error), this is type II error for each range or bin using mass values   
Transform mass values from Da to ppm (convertion formula 0.2Da)

Report CSV

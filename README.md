# Technical Challenge Submission
## Nick Eissler

Main function in combinefiles.py will combine the csv files listed in the command line (as long as all contain the same coloumns), and combine into one
csv with an additional column containing the file it originally came from

To run:
When in the project directory, type:
python(3) combinefiles.py /path/file1.csv /path/file2.csv ... /path/filen.csv

This will accept at least 2 csv files, but all must exist in the directory
An error will be thrown if there are < 2 files, a file does not exist where specified in the directory, or files do not have the same columns

To run test cases:
python(3) -m unittest test_combinefiles.py 

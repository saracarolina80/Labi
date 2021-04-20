import csv
import sys


def main(argv):

	if len(argv) < 2:
		path = input("Please insert the name of the file: ")
	else:
		path = argv[1] 
	
	fich_csv = open(path , "r")
	reader = csv.DictReader(fich_csv , delimiter=',')

	for row in reader:
		print(row)

	fich_csv.close()

#Run the program
main(sys.argv)

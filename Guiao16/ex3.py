import csv
import random
import time
import psutil
import sys

def main():
	print("File is being generated")

	fout = open('ex3.csv' , 'w')
	
	writer = csv.DictWriter(fout, fieldnames = ['time' , 'cpu' , 'net_usage'], delimiter = '|')
	writer.writeheader()

	tstart = time.time()
	tend = tstart + 60

	while time.time() < tend:
		writer.writerow({'time': time.time(), 'cpu' : psutil.cpu_percent(interval=1), 'net_usage': psutil.net_io_counters()[0]})

	fout.close()
	print("File created sucessfuly")

main()

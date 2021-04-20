import json
import time
import psutil


def main():
	print("File is being generated")
	
	fout = open('ex5.json','w')

	#List with data to be written on the file
	data = []

	tstart = time.time()
	tend = tstart + 10
	while time.time() < tend:
		temp = {'stats': {
		     'time' : time.time() , 'cpu': psutil.cpu_percent(interval=1), 'network': psutil.net_io_counters()[0]}
		}
		data.append(temp)

	fout.write(json.dumps(data, indent = 4))
	fout.close()
	print("File created sucessfully")


main()

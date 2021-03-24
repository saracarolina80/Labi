import sys
import hashlib

arguments = sys.argv[1:]

#print(arguments)
for filename in arguments:
	f = open(filename, "rb")
	data = f.read()
	f.close()
	
	h = hashlib.sha1()
	h.update(data)
	print(f"{filename}: {h.hexdigest()}")

import sys
import hashlib

arguments = sys.argv[1:]

#print(arguments)
for filename in arguments:
	f = open(filename , "rb")
	h = hashlib.sha1()
	
	while True:
		buffer = f.read(512)
		if len(buffer)==0:
			break
			
		h.update(buffer)
	
	f.close()
	print(f"{filename}: {h.hexdigest()}")
	

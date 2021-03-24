from Crypto.Hash import SHA256
import sys


arguments = sys.argv[1:]

#print(arguments)
for filename in arguments:
	f = open(filename , "rb")
	h = SHA256.new()
	
	while True:
		buffer = f.read(512)
		if len(buffer)==0:
			break
			
		h.update(buffer)
	
	f.close()
	print(f"{filename}: {h.hexdigest()}")
	

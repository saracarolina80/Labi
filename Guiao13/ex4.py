import os
from Crypto.Cipher import ARC4
import sys



key = sys.argv[1]
arguments = sys.argv[2:]
cipher = ARC4.new(key)

for filename in arguments:
	f = open(filename , "rb")
	w = open(filename + '.crypt' , 'wb')
	buffer = f.read(512)
	
	while len(buffer) > 0:
		cryptogram = cipher.encrypt(buffer)
		w.write (cryptogram)
		buffer = f.read(512)
		
	f.close()
	w.close()
	
	print("Ficheiro encriptado")
	




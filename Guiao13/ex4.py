import os
from Crypto.Cipher import ARC4
import sys



key = sys.argv[1]
arguments = sys.argv[2:]
cipher = ARC4.new(key)

for filename in arguments:
	f = open(filename , "rb")
	buffer = f.read(512)
	
	while len(buffer) > 0:
		cryptogram = cipher.encrypt(buffer)
		buffer = f.read(512)
		
	f.close()
	
	print(cryptogram )
	


os.write(1, cryptogram )

decipher = ARC4.new(key)
decrypted = decipher.decrypt( cryptogram )
print(" " + decrypted.decode('utf-8') )



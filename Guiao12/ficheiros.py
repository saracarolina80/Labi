import os.path
import sys

fname = "ola.txt"

if not os.path.exists(fname):
    sys.exit("Não existe")

if os.path.isdir(fname):
    sys.exit("É diretório")

if not os.path.isfile(fname):
    sys.exit("Não é ficheiro")

f = open(fname,"r")


f = open("ola.txt", "r")

while True:
    linha = f.readline()
    if linha == '':
        break
    print(linha)

f.close()
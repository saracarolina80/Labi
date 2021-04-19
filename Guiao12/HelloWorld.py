print("Hello World!")
#################

s = "Hello"
d = "World"

print(s + " " + d)

i = 20
f = "A Sara tem "
c = " anos"
print(f + str(i) + c)
print("%s%d%s" %(f, i , c))
print(f[0])
print(f[-2])

###########

ano = 2009

if ( ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0 :
    bissexto = True
else:
    bissexto = False

if bissexto:
    ndias = 29
else:
    ndias = 28

print(ndias)

#################

l = "Laboratórios de Informática"

for i in l:
    print(i)

idx = l.find("ó")
print(idx)

print(list (range(1,10)))
print(list (range(10)))
print(list (range(0,10,2)))

############

i = 0
while i < 3:
    i = i + 1
    print(i)

i = 0
while i < len(l):
    print(l[i])
    i = i + 1
   # OK i += 1
   # ERRO i++

########################

def nome(name):
    print("Olá " + name + "!")

nome("Sara")

def fatorial(x):
    a = 1
    while x > 0:
        a = a * x
        x = x - 1
    return a

##############
# LISTAS ( EM PYTHON NAO EXISTEM ARRAYS )

a = [ 1 , 2 ,3]
print(a)
print(a[1])
print(len(a))

for v in a:
    print(v)

a.append(99)
a.append(24)
print(a)
a.insert(2,1000)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.extend([12 , 13 , 14 , 15])
print(a)
a.remove(99)
print(a)
a.append(3)
a.append(3)
a.append(3)
print(a)
a.remove(3)
print(a)

###########################
a = [ 'Pedro' , 'Labi' , 18]

a = {'nome': 'Pedro ' , 'disciplina': 'LABI' , 'nota': '18'}
a = dict(nome = 'Pedro' , nota = '18' )

print(a['nome'])
print(a['nome'] + " " + str(a['nota']))

################

import sys
print("Numero de argumentos do programa: %d" % (len(sys.argv)))
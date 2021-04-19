
a = "Laboratórios"
b = " de "
c = "Informática"
print(len(c))
print(a+b+c)

a = "Laboratórios"
b = " de "
c = "Informática"
print(a[0:3]+"-"+c[0]+" "+str(2018)) # Imprime Lab-I 2018

# 12.4

a = " Laboratórios de Informática 2018 "
print(len(a)) # Comprimento de uma string
print(a.lower()) # Converte para minúsculas
print(a.upper()) # Converte para maiúsculas
print(a.title()) # Converte para título
print(a.find("t")) # Primeira posição de "t"
print(a.isalpha()) # Verifica se só tem letras
print(a.isdigit()) # Verifica se é um número
print(a.islower()) # Verifica se tem só minúsculas
print(a.strip()) # Remove espaços nos extremos
print(a.split(" ")) # Divide por espaços


## 12.5

equipa1 = "MD"
equipa2 = "AC1"
golos1 = 1
golos2 = 0
print("%s %d, %s %d" % (equipa1, golos1, equipa2, golos2))

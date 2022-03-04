# Usando uma fila e uma pilha
letras = []
numeros = []
digitos = [0,1,2,3,4,5,6,7,8,9]
lista = ['E',7,'T',8,'K',5,'C',0,9,'F']

for e in lista:
    if e in digitos:
        numeros.append(e)
    else:
        letras.append(e)
letras.sort()
numeros.sort()
total = letras + numeros
print(total)
# Contando quantos números pares e ímpares existentes entre 1 e 10 bem como a soma deles usando a instrução while 

n = 1
P = 0
I = 0
while n <= 10:
    a = int(input())
    n += 1
    if a % 2 == 0:
        a = P
        P += 1
    else: 
        a = I
        I += 1
print("A quantidade de números pares: ", P)
print("A quantidade de números ímpares: ", I)



# Escrevendo uma função chamada right_justify, que receba uma string chamada s como parâmetro 
# e exiba a string com espaços suficientes à frente para que a última letra da string esteja na coluna 70 da tela:
string = "s"

def right_justify(string):
    i = 1
    j = 70 - len(string)
    while i<= j:
        string = " " + string
        i += 1
    return print(string)

right_justify(string)
# Entrando com a mensagem e com o uso de módulos e funções
s = input("Digite a mensagem ser impressa: ")

def entrada():
  return s
print(s)

# Entrando com os valores de dois multiplicadores e exibindo o resultado na tela
Valor1 = int(input('Digite o 1º valor: '))
Valor2 = int(input('Digite o 2º valor: '))  

def calcular_multiplicação (Valor1, Valor2):
    multiplicação = Valor1 * Valor2
    return print('A mulptiplicação dos valores é: ',multiplicação)

calcular_multiplicação (Valor1, Valor2)
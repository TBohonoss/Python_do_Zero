# Calculando com dois números a soma (+), subtração(-), multiplicação(*) e divisão(/) da operação. 

a = int(input("Primeiro número:"))
b = int(input("Primeiro número:"))
operação = input("Digite a operação a relizar (+,-,* ou /):")
if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)

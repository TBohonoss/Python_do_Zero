# Calcular as raízes de uma equação do 2° Grau usando o módulo math 

import math

a = int(input("Coeficiente de a: "))
b = int(input("Coeficiente de b: "))
c = int(input("Coeficiente de c: "))
delta = (b**2 - 4*a*c)
x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)

print("Raízes: ",x1," e ",x2)
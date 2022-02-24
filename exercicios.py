# Calcular as raízes de uma equação do 2° Grau

a = int(input("Coeficiente de a: "))
b = int(input("Coeficiente de b: "))
c = int(input("Coeficiente de c: "))
delta = (b**2 - 4*a*c)
x1 = (-b + delta**(1/2)) / (2*a)
x2 = (-b - delta**(1/2)) / (2*a)

print("Raízes: ",x1," e ",x2)
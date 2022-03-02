# Criando 3 conjuntos conforme estrutura a seguir:
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])

# a)Fazendo a união dos três conjuntos e imprimindo o resultado
união = setx | sety | setz
print("A união dos três conjunto: ", união)

# b)Verifiquando quais os elementos comuns do conjunto setx e sety e imprima o resultado
intercessão = setx & sety
print("Os elementos comuns do conjunto setx e sety: ", intercessão)

# c)Verifiquando se o conjunto setx é subconjunto do conjunto sety e setz utilizando
print("O conjunto setx é subconjunto sety: ", setx.issubset(sety))
print("O conjunto setx é subconjunto setz: ",setx.issubset(setz))

# d)Verifiquando quais elementos do conjunto setx não existem em sety
print("Quais elementos do conjunto setx não existem em sety: ", setx.difference(sety))
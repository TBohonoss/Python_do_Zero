# Chamando a função duas vezes, passando o valor como um argumento
def do_twice(func, arg):
    func(arg)
    func(arg)

def print_valor(arg):
    print(arg)

do_twice(print, 'spam')
n = int(input())

def fatorial(numero):
    if (numero == 0):
        return 1
    return numero * fatorial(numero - 1)

fatorial_de_n = fatorial(n)

print(fatorial_de_n)
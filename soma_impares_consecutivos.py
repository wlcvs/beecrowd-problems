X = int(input())
Y = int(input())

if (Y < X):
    temp = X
    X = Y
    Y = temp

numeros = []

for i in range(X, Y + 1):
    numeros.append(i)

for i in range(2):
    if (len(numeros) > 0): 
        numeros.pop()
        numeros.reverse()

supostos_numeros_impares = [] 

for i in numeros:
    if (i % 2 != 0):
        supostos_numeros_impares.append(i)

soma = 0

for i in supostos_numeros_impares:
    soma = soma + i

print(soma)

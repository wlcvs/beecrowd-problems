a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

maior_inicial = (a + b + abs(a - b)) / 2

# se eu sei q o valor q ta na variavel maiorAB é o maior entre os
# dois primeiros numeros, entao so me resta testar com o maior numero
# agora

maior = (maior_inicial + c + abs(maior_inicial - c)) / 2

print(f'{int(maior)} eh o maior')
numero_inicial_de_abas, numero_de_acoes = input().split()
numero_inicial_de_abas, numero_de_acoes = int(numero_inicial_de_abas), int(numero_de_acoes)

numero_final_de_abas = numero_inicial_de_abas

for i in range(numero_de_acoes):
    acao = input()
    if (acao == 'fechou'):
        numero_final_de_abas -= 1
        numero_final_de_abas += 2
    else:
        numero_final_de_abas -= 1

print(numero_final_de_abas)




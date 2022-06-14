A = float(input())
B = float(input())

pesoA = 3.5
pesoB = 7.5

A = A * pesoA
B = B * pesoB

resultado_das_multiplicacoes = A + B

divisao_do_resultado_pelos_pesos = resultado_das_multiplicacoes / (pesoA + pesoB)

print(f'MEDIA = {divisao_do_resultado_pelos_pesos:.5f}')

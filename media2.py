A = float(input())
B = float(input())
C = float(input())

pesoA = 2 
pesoB = 3
pesoC = 5

A = A * pesoA
B = B * pesoB
C = C * pesoC

resultado_das_multiplicacoes = A + B + C

divisao_do_resultado_pelos_pesos = resultado_das_multiplicacoes / (pesoA + pesoB + pesoC)

print(f'MEDIA = {divisao_do_resultado_pelos_pesos:.1f}')

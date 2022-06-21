numero_correto = int(input())

respostas_corretas = 0

resposta_dada_pelos_competidores = input().split()

for i in range(len(resposta_dada_pelos_competidores)):
    temp = int(resposta_dada_pelos_competidores[i])
    resposta_dada_pelos_competidores[i] = temp

for i in resposta_dada_pelos_competidores:
    if (i == numero_correto):
        respostas_corretas += 1

print(respostas_corretas)
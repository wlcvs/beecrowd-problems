# ta eu sei q nessa eu vou precisar usar um algoritmo guloso
# apesar de eu nunca ter entendido mt bem como esse tipo
# de algoritmo funciona e oq ele faz pra chegar no resultado

cedulas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0]

entrada = int(input())

backup_entrada = entrada

cedulas_de_troco = []

indice_troco = 0

for i in cedulas:
    cedulas_de_troco.append(entrada // i)
    entrada -= (i * cedulas_de_troco[indice_troco])
    indice_troco += 1

print(backup_entrada)
for i in range(len(cedulas_de_troco)):
    cedula_str = str(cedulas[i]).replace('.', ',')
    cedulas_de_troco_int = int(cedulas_de_troco[i])
    print(f'{cedulas_de_troco_int} nota(s) de R$ {cedula_str}')

# preciso pensar em um nome melhor pra todas esssas
# variaveis
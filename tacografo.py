# vo ter q colocar tudo em uma string gigante e ir quebrando ela
# melhor ter esse trampo e me garantir do q tomar um wrong response
# ate pq eu nao quero digitar todos esses valores, e uma hora eu tenho
# q tomar vergonha na cara e aprender a fazer teste automatizados

# um array de str pra int, seria melhor

# entrada_crua_str_arr = input().splitlines()
# entrada_crua_int_arr = []

# for i in entrada_crua_str_arr:
#     print(i)


quantidade_de_intervalos_de_tempo = int(input())

distancia_total_percorrida = 0 

for i in range(quantidade_de_intervalos_de_tempo):
    tempo_decorrido, velocidade_media = input().split()
    tempo_decorrido, velocidade_media = int(tempo_decorrido), int(velocidade_media)

    distancia_total_percorrida += tempo_decorrido * velocidade_media

print(distancia_total_percorrida)


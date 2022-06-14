tempo_gasto_horas = int(input())
velocidade_media = int(input())

quantidade_de_km_por_l = 12

quantidade_de_litros_necessaria = (tempo_gasto_horas * velocidade_media) / quantidade_de_km_por_l

print(f'{quantidade_de_litros_necessaria:.3f}')

# informações q eu ja tenho:
# o carro faz 12 km/l
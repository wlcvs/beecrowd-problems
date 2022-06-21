n = int(input())

segundo = n % 60 
minuto = round(n / 60) % 60
hora = round(minuto / 60)

print(f'{hora}:{minuto}:{segundo}')
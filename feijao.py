# c1, c2, c3, c4 = input().split()
# c1, c2, c3, c4 = int(c1), int(c2), int(c3), int(c4) 

feijoes = input().split()

# for i in range(len(feijoes)):
#    feijoes[i] = int(feijoes[i])

for i in range(len(feijoes)):
    if (int(feijoes[i]) == 1):
        print(i + 1)
    

# obvio q nao vai vc ta comparando strings com inteiros idiota
# vo tentar fazer um loop pra transformar o nao pera deixa eu testar
# um negocio ta nao foi
# ta eu vo ter q fazer um loop pra transformar os itens do array em
# int
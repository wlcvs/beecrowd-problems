# primeiro eu so tenho q pegar o input
# e depois eu trato ele
# talvez colocar tudo em um array pareça uma escolha 
# interessante
# isso 

valores = []

# primeiro eu preciso pegar o input e colocar ele como
# elementos do array valores

while(True):
    input_bruto = input() 
    for i in input_bruto:
        valores.append(i)

    for i in range(len(valores)):
        print(valores[i])

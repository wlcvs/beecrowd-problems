nome = input()
salario_fixo = float(input())
total_vendas_dinheiro = float(input())

# ponto importante o vendendor ganha 15% de comissão sobre o valor
# das suas vendas, ou seja eu suponho que esses 15% vão para o seu 
# salario, na real q eu tenho certeza q é isso, mas quanto é 15 
# dividido por 100?

# então é só eu multiplicar o 0.15 pelo total_vendas e depois somar  com o salario

salario_com_comissao = salario_fixo + (total_vendas_dinheiro * (15 / 100))

print(f'TOTAL = R$ {salario_com_comissao:.2f}')
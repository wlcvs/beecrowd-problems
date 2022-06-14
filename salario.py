numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_recebido_pro_hora = float(input())

salario = horas_trabalhadas * valor_recebido_pro_hora

print(f'NUMBER = {numero_funcionario}')
print(f'SALARY = U$ {salario:.2f}')

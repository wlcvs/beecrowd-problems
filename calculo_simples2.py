codigo_peca1 = int(input())
numero_peca1 = int(input())
valor_unitario_peca1 = float(input())

codigo_peca2 = int(input())
numero_peca2 = int(input())
valor_unitario_peca2 = float(input())

valor1 = numero_peca1 * valor_unitario_peca1
valor2 = numero_peca2 * valor_unitario_peca2

valor_a_pagar = valor1 + valor2

print(f'VALOR A PAGAR: R$ {valor_a_pagar:.2f}')


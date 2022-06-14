class Peca:
    def __init__(self, codigo, quantidade, valor):
        self._codigo = int(codigo)
        self._quantidade = int(quantidade)
        self._valor = float(valor)

    def valor_a_ser_pago(self):
        return self._quantidade * self._valor

valor_a_pagar = 0

for i in range(2):
    codigo_peca, numero_peca, valor_unitatio_peca = input().split()

    peca = Peca(codigo_peca, numero_peca, valor_unitatio_peca)

    valor_a_pagar += peca.valor_a_ser_pago()

print(f'VALOR A PAGAR: R$ {valor_a_pagar:.2f}')

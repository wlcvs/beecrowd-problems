# basicamente eu tenho que calcular a área de todas essas figuras
# geometricas

# talvez eu possa criar uma class abstrata, chamada figura geometrica
# que tenha as propriedades mais básicas e que depois as suas classes
# filhas vem adptar pra oq elas precisam

# class FiguraGeomtrica:
#     def __init__(self):
#         pass

#     def area(self):
#         pass

class Triangulo:
    # a área de um triângulo consiste na metade da 
    # multiplicação da base pela altura.
    # aparentemente é  (base * altura) / 2

    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)

    def calcula_area(self):
        return (self.base * self.altura) / 2

class Circulo:
    # area = pi * raio ** 2
    # o raio seria C nesse caso
    # pi seria 3.14159

    def __init__(self, raio):
        self.raio = float(raio)
        self.pi = 3.14159

    def calcula_area(self):
        return self.pi * self.raio ** 2


class Trapezio:
    # area = ((A + B) * C) / 2 

    def __init__(self, base_maior, base_menor, altura):
        self.base_maior = float(base_maior)
        self.base_menor = float(base_menor)
        self.altura = float(altura)

    def calcula_area(self):
        return ((self.base_maior + self.base_menor) * self.altura) / 2

class Quadrado:
    # B ** 2
    def __init__(self, lado):
        self.lado = float(lado)

    def calcula_area(self):
        return self.lado ** 2

class Retangulo:
    # A * B
    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)

    def calcula_area(self):
        return self.base * self.altura

A, B, C = input().split()

triangulo = Triangulo(A, C)
circulo = Circulo(C)
trapezio = Trapezio(A, B, C)
quadrado = Quadrado(B)
retangulo = Retangulo(A, B)

print(f'TRIANGULO: {triangulo.calcula_area():.3f}')
print(f'CIRCULO: {circulo.calcula_area():.3f}')
print(f'TRAPEZIO: {trapezio.calcula_area():.3f}')
print(f'QUADRADO: {quadrado.calcula_area():.3f}')
print(f'RETANGULO: {retangulo.calcula_area():.3f}')

# depois eu tenho q voltar aqui e fazer um codigo melhor
# aplicar herança, polimorfismo, design patterns e os krl a 4
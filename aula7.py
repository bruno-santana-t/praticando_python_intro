# classe por convenção o nome inicia com letra maiúscula
# função por convenção o nome inicia com letra minuscula
# função no Pyhton SEMPRE retorna valor
# método no Python NUNCA retorna valor

# def adicao(a, b):
#     return a + b
#
#
# def subtracao(a, b):
#     return a - b
#
#
# def multiplicacao(a, b):
#     return a * b
#
#
# def divisao(a, b):
#     return a / b
#
#
# print(adicao(4, 4))
# print(adicao(5, 3))
# print(subtracao(10, 4))
# print(multiplicacao(5, 5))
# print(divisao(10, 2))

class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def adicao(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calculadora = Calculadora(5, 5)
    print('O valor de a é: {valor_a}  \nO valor de b é: {valor_b}'.format(valor_a=calculadora.valor_a,
                                                                          valor_b=calculadora.valor_b))

    # passando apenas uma única vez os valores, é possível chamar todas as funções
    print(calculadora.adicao())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())

class Calculadora:
    def adicao(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b


# sem inicializar, é possísivel passar os valores a cada vez que for necessário
calculadora = Calculadora()

print(calculadora.adicao(5, 5))
print(calculadora.subtracao(3, 2))
print(calculadora.multiplicacao(4, 7))
print(calculadora.divisao(30, 6))

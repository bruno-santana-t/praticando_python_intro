# contador_letras = lambda lista: [len(x) for x in lista]
# lista_animais = ['tigre', 'onça', 'cobra']
# print(contador_letras(lista_animais))

# adicao = lambda num1, num2: num1 + num2
# subtracao = lambda num1, num2: num1 - num2
# print(adicao(5, 50))
# print(subtracao(10, 2))


calculadora = {
    'adicao': lambda num1, num2: num1 + num2,
    'subtracao': lambda num1, num2: num1 - num2,
    'multiplicacao': lambda num1, num2: num1 * num2,
    'divisao': lambda num1, num2: num1 / num2
}

print(type(calculadora))

adicao = calculadora['adicao']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']
print('A adição é: {}'.format(adicao(5, 5)))
print('A subtração é: {}'.format(subtracao(5, 5)))
print('A multiplicação é: {}'.format(multiplicacao(5, 5)))
print('A divisão é: {}'.format(divisao(5, 5)))

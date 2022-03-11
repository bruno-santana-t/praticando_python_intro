a = int(input('Nota do primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou uma nota errada! \nNota do primeiro bimestre: '))
b = int(input('Nota do segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou uma nota errada! \nNota do segundo bimestre: '))
c = int(input('Nota do terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou uma nota errada! \nNota do terceiro bimestre: '))
d = int(input('Nota do quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou uma nota errada! \nNota do quarto bimestre: '))

media = (a + b + c + d) / 4

print('Média: {}'.format(media))

# a = int(input('Nota do primeiro bimestre: '))
# b = int(input('Nota do segundo bimestre: '))
# c = int(input('Nota do terceiro bimestre: '))
# d = int(input('Nota do quarto bimestre: '))
#
# media = (a + b + c + d) / 4
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média: {}'.format(media))
# else:
#     print('Foi informado alguma nota inválida!')

# a = int(input('Digite o primeiro número: '))
# b = int(input('Digite o segundo valor: '))
#
# resto_a = a % 2
# resto_b = b % 2
# # if resto_a == 0 or resto_b == 0:
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um número par!')
# else:
#     print('Não foi digitado nenhum número par!')

# if resto == 0:
#     print('O número é par!')
# else:
#     print('O número é ímpar!')

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# # indentação é igual à 4 espaços ou tab da IDE
# if a > b and a > c:
#     print('O maior número digitado é: {}'.format(a))
# elif b > a and b > c:
#     print('O maior número digitado é: {}'.format(b))
# else:
#     print('O maior número digitado é: {}'.format(c))
# print('\nFim do código!')

# checar se um número é primo ou não
# ou seja: se ele é apenas divisível por 1 e por ele mesmo

# a = int(input('Digite um número: '))
# div = 0
# for x in range(1, a + 1):
#     resto = a % x
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('O número {} é primo!'.format(a))
# else:
#     print('O número {} não é primo!'.format(a))

# num_max = int(input('Digite um número máximo para procurar: '))
# for a in range(num_max+1):
#     div = 0
#     for x in range(1, a + 1):
#         resto = a % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print('O número {} é primo!'.format(a))

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# nota = int(input('Digite uma nota: '))
# while not nota <= 10:
#     nota = int(input('Nota inválida! Digite uma nota: '))
# print(nota)


nota_1_bi = int(input('Nota do primeiro bimestre: '))
while not nota_1_bi <= 10:
    nota_1_bi = int(input('Nota inválida! Digite uma nota: '))

nota_2_bi = int(input('Nota do segundo bimestre: '))
while not nota_2_bi <= 10:
    nota_2_bi = int(input('Nota inválida! Digite uma nota: '))

nota_3_bi = int(input('Nota do terceiro bimestre: '))
while not nota_3_bi <= 10:
    nota_3_bi = int(input('Nota inválida! Digite uma nota: '))

nota_4_bi = int(input('Nota do quarto bimestre: '))
while not nota_4_bi <= 10:
    nota_4_bi = int(input('Nota inválida! Digite uma nota: '))

media = (nota_1_bi + nota_2_bi + nota_3_bi + nota_4_bi) / 4

print('Média: {}'.format(media))

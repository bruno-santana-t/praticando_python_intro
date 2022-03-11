a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# print(type(soma))

# print('Soma : ' + str(soma))
# print('Divisão : ' + str(int(divisao)))

# print('Soma: {}. Divisão: {}' .format(soma, divisao))
resultado = ('Soma: {sum}'
             '\nSubtração: {sub}'
             '\nMultiplicação: {mult}'
             '\nDivisão: {div}'
             '\nResto: {res}'
             .format(sum=soma,
                     sub=subtracao,
                     mult=multiplicacao,
                     div=divisao,
                     res=resto))
print(resultado)

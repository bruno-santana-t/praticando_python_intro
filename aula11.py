lista = [1, 2, 3, 4]

# hierarquia das exceções do Python
# https://docs.python.org/pt-br/3.10/library/exceptions.html


try:
    divisao = 10 / 1
    numero = lista[1]
    # x = a
    print('Se houver falha acima, essa linha não executa')

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar um índice inexistente')
except BaseException as ex:
    print('Erro desconhecido. \n Erro: {}'.format(ex))
else:
    print('Executa quando não há nenhuma exceção')
finally:
    print('Sempre executa')

# while True é apenas um laço infinito sem "condicional". O Break que vai interromper ele
# para criar uma classe de erro customizada, é preciso importar a Exception antes
class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Ditige uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('A nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('A nota não pode ser menos que 0')
        break

    except ValueError:
        print('Você digitou uma nota inválida!\n')

    except InputError as ex:
        print(ex)

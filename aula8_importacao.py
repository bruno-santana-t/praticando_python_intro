# Um módulo é um arquivo contendo definições e comandos em Python para serem usados em outros programas em Python
# Há diversos módulos do Python que fazem parte da biblioteca padrão
# Você pode importar um módulo inteiro ou apenas uma classe específica

from aula7_televisao import Televisao
from aula7 import Calculadora
from aula8_contador_letras import contador_letras

# inclusive se alguém importar esse método de fora, ele nào vai chamar esse bloco abaixo com essa proteção dos testes
if __name__ == '__main__':
    televisao = Televisao()
    # print('A televisão está ligada? {}'.format(televisao.ligada))
    #
    # televisao.power()
    # print('A televisão agora está ligada? {}'.format(televisao.ligada))
    #
    # # no caso da calculadora é uma função que já precisa iniciar com valores
    # calculadora = Calculadora(50, 5)
    # print(calculadora.adicao())

    lista = ['tigre', 'sapo']
    print(contador_letras(lista))

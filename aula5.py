lista = [1, 23, 58, 7]
lista_animal = ['cachorro', 'gato', 'elefante']

# print(lista_animal[1])

# for animal in lista_animal:
#     print(animal)
#
# print(sum(lista))
# print(max(lista))
# print(min(lista_animal))
#
# if 'gato' in lista_animal:
#     print('Existe gato na lista')
#
# print(lista_animal)
# lista_animal.pop()
# nova_lista = lista_animal * 3
# nova_lista.pop(1)
# print(nova_lista)
#
# nova_lista.append('lobo')
# print(nova_lista)
#
# nova_lista.remove('gato')
# print(nova_lista)

# lista.sort()
# lista_animal.sort()
# print(lista, lista_animal)
#
# lista.reverse()
# lista_animal.reverse()
# print(lista, lista_animal)

lista_animal[0] = 'cobra'
print(lista_animal)

tupla = (12, 34, 5, 8, 22)
print(tupla)
print(len(tupla))
print(len(lista_animal))

tupla_animal = tuple(lista_animal)
print(tupla_animal)

lista_numerica = list(tupla)
print(lista_numerica)

lista_numerica[0] = 24
print(lista_numerica)

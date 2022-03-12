# conjunto não possui duplicidade

# conjunto = {1, 3, 5, 4, 4, 3, 1, 1}
# print(conjunto)
# print(type(conjunto))
#
# conjunto.add(17)
# print(conjunto)
#
# conjunto.discard(4)
# print(conjunto)


# conjunto_1 = {1, 2, 3, 4, 5}
# conjunto_2 = {5, 6, 7, 8, 9}
# print('Conjunto 1: {}'.format(conjunto_1))
# print('Conjunto 2: {}'.format(conjunto_2))

# conjunto_uniao = conjunto_1.union(conjunto_2)
# print('União: {}'.format(conjunto_uniao))
#
# conjunto_interseccao = conjunto_1.intersection(conjunto_2)
# print('Intersecção: {}'.format(conjunto_interseccao))
#
# conjunto_diferenca_1 = conjunto_1.difference(conjunto_2)
# print('Diferença entre o conjunto_1 e o conjunto_2: {}'.format(conjunto_diferenca_1))
#
# conjunto_diferenca_2 = conjunto_2.difference(conjunto_1)
# print('Diferença entre o conjunto_2 e o conjunto_1: {}'.format(conjunto_diferenca_2))
#
# conjunto_diff_simetrica = conjunto_1.symmetric_difference(conjunto_2)
# print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

# conjunto_a = {1, 2, 3}
# conjunto_b = {1, 2, 3, 4, 5}
#
# conjunto_subset_a = conjunto_a.issubset(conjunto_b)
# print('a subconjunto em b: {}'.format(conjunto_subset_a))
#
# conjunto_subset_b = conjunto_b.issubset(conjunto_a)
# print('b subconjunto em a: {}'.format(conjunto_subset_b))
#
# conjunto_superset_a = conjunto_a.issuperset(conjunto_b)
# print('a superconjunto em b: {}'.format(conjunto_superset_a))
#
# conjunto_superset_b = conjunto_b.issuperset(conjunto_a)
# print('b superconjunto em a: {}'.format(conjunto_superset_b))


lista_animais = ['cavalo', 'onça', 'cavalo', 'rato', 'pomba']
print('Lista de animais: {}'.format(lista_animais))

conjunto_animais = set(lista_animais)
print('\nConjunto animais: {}'.format(conjunto_animais))

lista_animais_convertida = list(conjunto_animais)
print('\nConversão da lista de animais a partir do conjunto: {}'.format(lista_animais_convertida))

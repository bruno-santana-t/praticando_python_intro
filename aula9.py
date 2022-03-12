import shutil


def escrever_arquivo(texto):
    arquivo = open('arquivo_teste.txt', 'w')
    arquivo.write(texto + '\n')
    arquivo.close()


def atualizar_arquivo(texto):
    arquivo = open('arquivo_teste.txt', 'a')
    arquivo.write(texto + '\n')
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def atualizar_boletim(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto + '\n')
    arquivo.close()


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    nota_aluno = arquivo.read()
    # print(nota_aluno)

    # está usando como delimitador a própria quebra de linha para converter de string para lista
    nota_aluno = nota_aluno.split('\n')
    lista_media = []

    for x in nota_aluno:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        # print(aluno)

        # removendo a string para ser possível converter para inteiro as notas
        lista_notas.pop(0)

        media = lambda notas: sum([float(i) for i in notas]) / 5
        # print(media(lista_notas))

        lista_media.append({aluno: media(lista_notas)})

    return lista_media


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'arquivos_copias/')


def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'arquivos_copias/')


# relembrando de garantir a boa prática de testes
if __name__ == '__main__':
    # escrever_arquivo('Primeira linha')
    # atualizar_arquivo('Próxima linha')
    # ler_arquivo('arquivo_teste.txt')

    # notas = 'Bruno, 7, 8.5, 10, 8.1, 10'
    # atualizar_boletim('notas.csv', notas)

    # lista_final = media_notas('notas.csv')
    # print(lista_final)c

    copia_arquivo('notas.csv')
    # move_arquivo('arquivo_para_mover.txt')

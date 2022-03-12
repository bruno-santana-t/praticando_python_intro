import requests


def busca_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    # print(response.status_code)
    #
    # print(response.text)
    # print(type(response.text))

    # print(response.json())
    # print(type(response.json()))

    dados_cep = response.json()
    # print(dados_cep['logradouro'])
    return dados_cep


def busca_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon


def raspagem_url(url):
    response = requests.get(url)
    html_site = response.text
    return html_site


if __name__ == '__main__':
    # print(busca_cep('45028265'))
    # resultado_pokemon = busca_pokemon('pikachu')
    # print(resultado_pokemon['sprites']['front_shiny'])

    print(raspagem_url('https://www.ycombinator.com/companies/'))

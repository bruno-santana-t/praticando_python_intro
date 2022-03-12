from datetime import date, time, datetime, timedelta


# link documentação da formatação da biblioteca:
# https://docs.python.org/pt-br/3.10/library/datetime.html#strftime-and-strptime-behavior

def trabalhando_com_date():
    data_atual = date.today()
    print(type(data_atual))
    print(data_atual)

    print(data_atual.strftime('%d/%m/%Y'))

    data_atual_srt = data_atual.strftime('%d %B %Y')
    print(type(data_atual_srt))
    print(data_atual_srt)


def trabalhando_com_time():
    horario = time(hour=15, minute=27, second=10)
    print(type(horario))
    print(horario)

    print(horario.strftime('%H:%M'))


def trabalhandp_com_datetime():
    # momento_atual = datetime.now()
    # print(momento_atual)
    # print(momento_atual.strftime('%d/%m/%Y às %H:%M:%S'))
    #
    # print(momento_atual.day)
    # print(momento_atual.month)
    # print(momento_atual.year)
    # print(momento_atual.hour)
    # print(momento_atual.minute)
    # print(momento_atual.second)
    # print(momento_atual.date())
    # print(momento_atual.weekday())
    #
    # tupla_dia = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    # print(tupla_dia[momento_atual.weekday()])
    #
    # tupla_mes = (
    # 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
    # 'Dezembro')
    # print(tupla_mes[momento_atual.month])

    # data_criada = datetime(1990, 6, 30, 11, 50, 10)
    # print(data_criada)
    # print(type(data_criada))
    # print(data_criada.strftime('%c'))

    data_string = '12/04/2022 15:47:30'
    print(type(data_string))
    print(data_string)

    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(type(data_convertida))
    print(data_convertida)

    nova_data = data_convertida - timedelta(days=180, minutes=123)
    print(type(nova_data))
    print(nova_data)


if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    trabalhandp_com_datetime()

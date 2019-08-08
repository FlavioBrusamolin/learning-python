from datetime import date


def calculateDate():
    year = int(input('Entre com o ano do seu nascimento: '))
    month = int(input('Entre com o mes do seu nascimento: '))
    day = int(input('Entre com o dia do seu nascimento: '))

    dateOfBirth = date(year, month, day)
    today = date.today()
    result = today - dateOfBirth

    print('Seus dias de vida são: %d' % (result.days))


if __name__ == '__main__':
    calculateDate()

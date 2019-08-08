class Country(object):
    name = str()


def show_countries(countries):
    for country in countries:
        print(f'Id do(a) {country.name}: {id(country)}')


def create_countries(countries_quantity):
    countries = []
    for iterator in range(countries_quantity):
        new_country = Country()
        new_country.name = input(f'Entre com o nome do país {iterator + 1}: ')
        countries.append(new_country)
    return countries


def main():
    countries_quantity = int(input('Entre com o número de países que você deseja criar: '))
    countries = create_countries(countries_quantity)
    show_countries(countries)


if __name__ == "__main__":
    main()

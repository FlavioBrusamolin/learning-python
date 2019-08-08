def read_data_input():
    age_list = []
    height_list = []

    for iterator in range(5):
        age_list.append(
            int(input(f'Entre com a idade da pessoa {iterator + 1}: ')))
        height_list.append(
            int(input(f'Entre com a altura da pessoa {iterator + 1}: ')))

    return age_list, height_list


def print_reversed_lists(age_list, height_list):
    age_list.reverse()
    height_list.reverse()

    for iterator in range(5):
        print(f'Idade da pessoa {iterator + 1}: {age_list[iterator]}')
        print(f'Altura da pessoa {iterator + 1}: {height_list[iterator]}')


def main():
    age_list, height_list = read_data_input()
    print_reversed_lists(age_list, height_list)


if __name__ == "__main__":
    main()

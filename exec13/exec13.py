def write_vertically(name):
    for letter in name:
        print(letter)


def main():
    name = input('Entre com o nome do usuário: ')
    write_vertically(name)


if __name__ == "__main__":
    main()

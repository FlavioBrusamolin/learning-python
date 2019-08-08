if __name__ == "__main__":
    full_name = input('Entre com o seu nome e sobrenome separados por espaço: ')
    first_name, last_name = full_name.split()
    print('Nome: ', first_name.swapcase())
    print('Sobrenome: ', last_name.swapcase())

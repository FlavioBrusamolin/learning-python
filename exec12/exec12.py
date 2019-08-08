def init():
    file_name = input('Entre com o nome do arquivo de gravação (com extensão): ')
    user_name = input('Entre com o nome do usuário: ')
    user_cpf = input('Entre com o CPF do usuário: ')
    user_address = input('Entre com o endereço do usuário: ')
    write_data(file_name, user_name, user_cpf, user_address)

def write_data(file_name, user_name, user_cpf, user_address):
    new_file = open(file_name, 'w')
    new_file.write(f'Nome: {user_name}\n')
    new_file.write(f'CPF: {user_cpf}\n')
    new_file.write(f'Endereco: {user_address}\n')
    new_file.close()

if __name__ == "__main__":
    init()
    print('Gravação efetuada')

    

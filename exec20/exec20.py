def read_contacts_data(contacts_quantity):
    contacts = []
    for iterator in range(contacts_quantity):
        name = input(f'Entre com o nome do contato {iterator + 1}: ')
        number = input(f'Entre com o número do contato {iterator + 1}: ')
        contacts.append({"name": name, "number": number})
    return contacts


def print_all_contacts(contacts):
    print('AGENDA DE CONTATOS')
    for contact in contacts:
        print(f'Nome: {contact["name"]} / Número: {contact["number"]}')


def main():
    contacts_quantity = int(input('Entre com o número de contatos da sua agenda: '))
    contacts = read_contacts_data(contacts_quantity)
    print_all_contacts(contacts)


if __name__ == "__main__":
    main()

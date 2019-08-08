from entities import HumanResources, Accounting


def check_object_type(obj):
    if isinstance(obj, HumanResources):
        print('O objeto é do tipo Recursos Humanos')
    if isinstance(obj, Accounting):
        print('O objeto é do tipo Contabilidade')


def create_instance():
    option = int(input(
        'Entre com o tipo do setor que você deseja criar (1 - Recursos Humanos; 2 - Contabilidade): '))

    if option == 1:
        obj = HumanResources()
    elif option == 2:
        obj = Accounting()
    else:
        print('Opção inválida')
        quit()

    return obj


def main():
    obj = create_instance()
    check_object_type(obj)


if __name__ == "__main__":
    main()

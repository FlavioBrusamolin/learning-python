class Person(object):
    name = str()
    sex = str()
    age = int()

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


class Citizen(Person):
    cpf = str()

    def __init__(self, name, sex, age, cpf):
        super().__init__(name, sex, age)
        self.cpf = cpf


class UserInterface(object):
    def read_citizen_data(self):
        name = input('Entre com o nome do cidadão: ')
        sex = input('Entre com o sexo do cidadão: ')
        age = int(input('Entre com a idade do cidadão: '))
        cpf = input('Entre com o CPF do cidadão: ')
        return name, sex, age, cpf

    def show_citizen_data(self, citizen):
        print('DADOS DO CIDADÃO')
        print(f'Nome: {citizen.name}')
        print(f'Sexo: {citizen.sex}')
        print(f'Idade: {citizen.age}')
        print(f'CPF: {citizen.cpf}')

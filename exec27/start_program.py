from models import UserInterface, Citizen


def main():
    user_interface = UserInterface()
    name, sex, age, cpf = user_interface.read_citizen_data()
    new_citizen = Citizen(name, sex, age, cpf)
    user_interface.show_citizen_data(new_citizen)


if __name__ == "__main__":
    main()

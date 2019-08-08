from models import BankAccount


def create_bank_account():
    account_number = input('Entre com o número da conta: ')
    owner_name = input('Entre com o nome do correntista: ')
    option = int(input('Deseja entrar com o saldo da conta? (1 - Sim; 0 - Não) '))
    if option == 1:
        account_balance = float(input('Entre com o saldo da conta: '))
        new_bank_account = BankAccount(account_number, owner_name, account_balance)
    elif option == 0:
        new_bank_account = BankAccount(account_number, owner_name)
    else:
        print('Opção inválida')
        quit()
    return new_bank_account


def provide_account_options(bank_account):
    option = None
    while option != 0:
        option = int(input('Qual operação deseja realizar? (1 - Mudar nome do correntista; 2 - Depositar; 3 - Sacar; 0 - Sair) '))
        if option == 1:
            new_owner_name = input('Entre com o novo nome do correntista: ')
            bank_account.change_owner_name(new_owner_name)
            print(f'Novo nome: {bank_account.owner_name}')
        elif option == 2:
            value = float(input('Entre com o valor que deseja depositar: '))
            bank_account.deposit(value)
            print(f'Novo saldo: {bank_account.balance}')
        elif option == 3:
            value = float(input('Entre com o valor que deseja sacar: '))
            bank_account.cash_out(value)
            print(f'Novo saldo: {bank_account.balance}')
        elif option == 0:
            print('Obrigado, até a próxima')
        else:
            print('Opção inválida')


def main():
    new_bank_account = create_bank_account()
    provide_account_options(new_bank_account)


if __name__ == "__main__":
    main()

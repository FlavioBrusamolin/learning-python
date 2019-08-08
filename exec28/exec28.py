from abc import ABCMeta, abstractmethod


class BankAccount(metaclass=ABCMeta):
    balance = 1000

    @abstractmethod
    def update(self, value):
        pass


class CheckingAccount(BankAccount):
    def update(self, value):
        self.balance += value * 2


class SavingsAccount(BankAccount):
    def update(self, value):
        self.balance += value * 3


if __name__ == "__main__":
    checking_account = CheckingAccount()
    savings_account = SavingsAccount()
    checking_account.update(500)
    savings_account.update(500)
    print(f'Saldo da conta corrente: {checking_account.balance}')
    print(f'Saldo da conta poupança: {savings_account.balance}')

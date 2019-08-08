class BankAccount(object):
    number = str()
    owner_name = str()
    balance = float()

    def __init__(self, number, owner_name, balance = 0):
        self.number = number
        self.owner_name = owner_name
        self.balance = balance

    def change_owner_name(self, name):
        self.owner_name = name

    def deposit(self, value):
        self.balance += value

    def cash_out(self, value):
        self.balance -= value

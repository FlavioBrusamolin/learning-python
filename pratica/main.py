class Pessoa(object):
    nome: str()
    idade: int()
    peso: float()
    altura: float()

    def engordar(self, gramas):
        self.peso += gramas

    def emagrecer(self, gramas):
        self.peso -= gramas

    def crescer(self, cm):
        self.altura += cm

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(anos * 0.5)

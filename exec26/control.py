class DiscountControl(object):
    product_price = float()
    _discount_percentage = float()

    @property
    def discount_percentage(self):
        return int(self._discount_percentage)

    @discount_percentage.setter
    def discount_percentage(self, value):
        self._discount_percentage = 1 if value < 1 or value > 35 else value

    def apply_discount(self):
        return self.product_price - (self.product_price * self._discount_percentage / 100)


def create_discount_control():
    new_discount_control = DiscountControl()
    new_discount_control.product_price = float(input('Entre com o preço do produto: '))
    new_discount_control.discount_percentage = float(input('Entre com a porcentagem de desconto: '))
    return new_discount_control


def main():
    new_discount_control = create_discount_control()
    print('RESULTADO')
    print(f'Preço do produto antes do desconto: {new_discount_control.product_price}')
    print(f'Desconto aplicado: {new_discount_control.discount_percentage}%')
    print(f'Preço do produto depois do desconto: {new_discount_control.apply_discount()}')


if __name__ == "__main__":
    main()

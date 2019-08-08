from math import pow


def calculateCubeOfNumber():
    number = int(input('Entre com o número desejado: '))
    result = pow(number, 3)
    print('O cubo de %d é %d' % (number, result))


if __name__ == '__main__':
    calculateCubeOfNumber()

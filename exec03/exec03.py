number1 = int(input('Entre com um número: '))
number2 = int(input('Entre com outro número: '))
number3 = int(input('Entre com outro número: '))
number4 = int(input('Entre com outro número: '))

number1, number2, number3, number4 = number4, number3, number2, number1

print('Números invertidos: %d %d %d %d' % (number1, number2, number3, number4))

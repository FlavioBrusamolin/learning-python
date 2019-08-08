year = int(input('Entre com um ano: '))

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print(f'{year} é um ano bissexto')
else:
    print(f'{year} não é um ano bissexto')

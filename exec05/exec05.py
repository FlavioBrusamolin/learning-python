vowels = ['a', 'e', 'i', 'o', 'u']

letter = input('Entre com uma letra qualquer: ')

if letter.lower() in vowels:
    print(f'A letra {letter} é uma vogal')
else:
    print(f'A letra {letter} é uma consoante')

def division():
    try:
        number1 = int(input('Entre com um número inteiro: '))
        number2 = int(input('Entre com outro número inteiro: '))
    except ValueError:
        print('Insira somente números inteiros')
    except:
        print('Ocorreu um erro inesperado. Consulte o administrador')
    else:
        print(
            f'O resultado da divisão de {number1} por {number2} é {number1 // number2}')
    finally:
        print('Processo encerrado')


if __name__ == "__main__":
    division()

def division():
    try:
        number1 = int(input('Entre com um número inteiro: '))
        number2 = int(input('Entre com outro número inteiro: '))
        result = number1 // number2
    except ValueError:
        print('Insira somente números inteiros')
    except ZeroDivisionError:
        print('Divisão por 0 não permitida')
    except:
        print('Ocorreu um erro inesperado. Consulte o administrador')
    else:
        print(f'O resultado da divisão de {number1} por {number2} é {result}')
    finally:
        print('Processo encerrado')


if __name__ == "__main__":
    division()

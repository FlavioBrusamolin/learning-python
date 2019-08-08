def add_tax(cost, tax_rate):
    new_cost = cost + ((cost * tax_rate) / 100)
    return new_cost

if __name__ == "__main__":
    try:
        cost = float(input('Entre com o custo do item antes do imposto: '))
        tax_rate = float(input('Entre com a quantia de impostos expressa em porcentagem: '))
    except ValueError:
        print('Erro: Entre com um número')
    except:
        print('Ocorreu um erro inesperado. Consulte o administrador')
    else:
        new_cost = add_tax(cost, tax_rate)
        print(f'O novo custo é {new_cost}')

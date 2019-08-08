from models import Ball


def read_ball_data():
    new_ball = Ball()
    new_ball.color = input('Informe a cor da bola: ')
    new_ball.circumference = float(input('Informe a circunferência da bola: '))
    new_ball.brand = input('Informe a marca da bola: ')
    return new_ball


def show_ball_data(ball):
    print(f'Id da bola: {id(ball)}')
    print(f'Cor da bola: {ball.color}')
    print(f'Circunferência da bola: {ball.circumference}')
    print(f'Marca da bola: {ball.brand}')


def main():
    ball = read_ball_data()
    show_ball_data(ball)


if __name__ == "__main__":
    main()

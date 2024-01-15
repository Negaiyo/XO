from random import randint

board = list(range(1, 10))


def print_board(board):
    print("-" * 13)
    for x in range(3):
        print("|", board[0 + x * 3], "|", board[1 + x * 3], "|", board[2 + x * 3], "|")
        print("-" * 13)


def take_input(player_token):
    valid = False
    while not valid:
        player = input(f"Куда поставим {player_token} ? ")
        try:
            player = int(player)
        except ValueError:
            print("Введите корректное число!")
            continue
        if 1 <= player <= 9:
            if str(board[player - 1]) not in "XO":
                board[player - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята")
        else:
            print("Введите корректное число от 1 до 9!")
    return print_board(board)


def check_win(board):
    win = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (2, 5, 8), (4, 5, 6))
    for x in win:
        if board[x[0]] == board[x[1]] == board[x[2]]:
            return board[x[0]]
    return False


def bot_token(bot_token):
    valid = False
    while not valid:
        bot = randint(1, 9)
        if 1 <= bot <= 9:
            if str(board[bot - 1]) not in "XO":
                board[bot - 1] = bot_token
                valid = True
            else:
                valid = False


def main(board):
    counter = 0
    win = False
    while not win:
        print_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            bot_token("O")
        counter += 1

        check = check_win(board)
        if check:
            print(f"{check} победил !")
            win = True
            break
        elif counter == 9:
            print("Ничья!")
            win = True
            break
    print_board(board)

main(board)

input("Нажмите Enter для выхода!")

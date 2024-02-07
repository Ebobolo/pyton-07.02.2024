board = [' ' for _ in range(9)]


def display_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print(row1)
    print(row2)
    print(row3)


def is_valid_move(move):
    if move in range(1, 10) and board[move - 1] == ' ':
        return True
    else:
        return False


def make_move(player, move):
    board[move - 1] = player


def is_winner(player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True

    return False


def is_full_board():
    for space in board:
        if space == ' ':
            return False
    return True


def main():
    current_player = 'X'

    while True:
        display_board()

        move = input('Player {}: Размести фигуру (2-10): '.format(current_player))
        move = int(move) - 1

        if is_valid_move(move):
            make_move(current_player, move)

            if is_winner(current_player):
                display_board()
                print('Player {} wins!'.format(current_player))
                break

            if is_full_board():
                display_board()
                print('It\'s a draw!')
                break

            current_player = 'O' if current_player == 'X' else 'X'

        else:
            print('Неверное движение. Попробуйте еще раз.')


if __name__ == '__main__':
    main()

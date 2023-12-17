def display_board(board):

    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def start():

    import random
    player = ['Player 1', 'Player 2']
    started_player = random.choice(player)
    return started_player

def position_choice(field):
    while True:
        try:
            position = int(input("choose your position (1-9): "))
            if position in range(1, 10) and field[position - 1] == ' ':
                return position
            else:
                print("Invalid position or already occupied. Please select another position.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def new_game():
    while True:
        answer = input("Would you like to start a new game, [Y/N]: ").lower()
        if answer == 'yes' or answer == 'y':
            return True
        elif answer == 'no' or answer == 'n':
            return False
        else:
            print("Please answer yes or no")

def won(field, marker):

    return ((field[0] == field[1] == field[2] == marker) or
            (field[3] == field[4] == field[5] == marker) or
            (field[6] == field[7] == field[8] == marker) or
            (field[0] == field[3] == field[6] == marker) or
            (field[1] == field[4] == field[7] == marker) or
            (field[2] == field[5] == field[8] == marker) or
            (field[0] == field[4] == field[8] == marker) or
            (field[2] == field[4] == field[6] == marker))


while True:
    spielfeld = [' '] * 9
    current_player = start()

    print(f"{current_player} started!")

    while True:
        display_board(spielfeld)
        print(f"{current_player}, You are now.")
        position = position_choice(spielfeld)

        if current_player == 'Player 1':
            spielfeld[position - 1] = 'X'
            if won(spielfeld, 'X'):
                display_board(spielfeld)
                print("Glückwunsch! Player 1 has won!")
                break
            else:
                current_player = 'Player 2'
        else:
            spielfeld[position - 1] = 'O'
            if won(spielfeld, 'O'):
                display_board(spielfeld)
                print("Glückwunsch! Player 2 hat gewonnen!")
                break
            else:
                current_player = 'Player 1'

        if ' ' not in spielfeld:
            display_board(spielfeld)
            print("Match Draw!")
            break

    if not new_game():
        break

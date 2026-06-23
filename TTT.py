import random

def player_input():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input("Newbie, What will you choose? (X/O): ").upper()
    return marker, ('O' if marker == 'X' else 'X')

def position_board(board):
    print()
    print(f"  {board[1]} | {board[2]} | {board[3]} ")
    print("--- + -- + ---")
    print(f"  {board[4]} | {board[5]} | {board[6]} ")
    print("--- + -- + ---")
    print(f"  {board[7]} | {board[8]} | {board[9]} ")
    print()

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return (
        (board[7] == board[8] == board[9] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[1] == board[2] == board[3] == mark) or
        (board[7] == board[4] == board[1] == mark) or
        (board[8] == board[5] == board[2] == mark) or
        (board[9] == board[6] == board[3] == mark) or
        (board[7] == board[5] == board[3] == mark) or
        (board[9] == board[5] == board[1] == mark)
    )

def space_check(board, position):
    return board[position] == ' '

def full_boardcheck(board):
    return all(space != ' ' for space in board[1:])

def player_choice(board):
    while True:
        try:
            position = int(input("Choose your next position (1-9): "))
            if position in range(1, 10):
                if space_check(board, position):
                    return position
                else:
                    print("Position already occupied!")
            else:
                print("Enter a number between 1 and 9.")
        except ValueError:
            print("Please enter a valid number.")

def master_move(board):
    possible_moves = [i for i in range(1, 10) if space_check(board, i)]
    return random.choice(possible_moves)

def choose_first():
    return 'Newbie' if random.randint(0, 1) == 0 else 'Master'

def replay():
    return input("Do you want to play again? (y/n): ").lower().startswith('y')


print("Welcome... Let's play Tic Tac Toe!")
print("Play against the Master, Newbie!")

while True:
    board = [' '] * 10

    player_marker, bot_marker = player_input()

    turn = choose_first()
    print(f"{turn} will go first.")

    play_game = input("Are you ready to play? (y/n): ").lower()

    if play_game.startswith('y'):
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Newbie':

            position_board(board)

            position = player_choice(board)
            place_marker(board, player_marker, position)

            if win_check(board, player_marker):
                position_board(board)
                print("Congratulations! You won!")
                game_on = False

            elif full_boardcheck(board):
                position_board(board)
                print("The game is a draw!")
                break

            else:
                turn = 'Master'

        else:

            print("Master is making a move...")
            position = master_move(board)
            place_marker(board, bot_marker, position)

            if win_check(board, bot_marker):
                position_board(board)
                print("Master has won!")
                game_on = False

            elif full_boardcheck(board):
                position_board(board)
                print("The game is a draw!")
                break

            else:
                turn = 'Newbie'

    if not replay():
        break
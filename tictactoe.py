
def game_display(board_list):
    print("\n")
    print(f"  {board_list[0]}   |  {board_list[1]}   |  {board_list[2]}")
    print('-------------------')
    print(f"  {board_list[3]}   |  {board_list[4]}   |  {board_list[5]}")
    print('-------------------')
    print(f"  {board_list[6]}   |  {board_list[7]}   |  {board_list[8]}")
    print("\n")


def choose_symbol():
    while True:
        answer = input("Player 1 do you want to be X or O : ")
        if answer in ['X', 'x', 'O', 'o']:
            break
        else:
            pass
    return answer.upper()


def play_again():
    while True:
        answer = input("Want to play again Y or N : ")
        if answer in ['Y', 'y', 'N', 'n']:
            break
        else:
            pass

    # return True if answer = Y else return False
    if answer in ['Y', 'y']:
        return True
    else:
        return False


def choose_position(player_name, board_list):
    while True:
        # ask player1 to choose a position
        position = input(f"{player_name} Choose an empty position from 1 - 9 : ")

        '''check if it is a valid input'''
        if position in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:

            '''check if it the position is empty'''
            if board_list[int(position) - 1] == ' ':
                return int(position)
            else:
                print('Position Not Empty!!!\n')
            continue
        else:
            print('Invalid Input!!!\n')
            continue


def win_check(board_list, symbol):
    if board_list[0] == symbol and board_list[1] == symbol and board_list[2] == symbol:
        return True

    elif board_list[3] == symbol and board_list[4] == symbol and board_list[5] == symbol:
        return True

    elif board_list[6] == symbol and board_list[7] == symbol and board_list[8] == symbol:
        return True

    elif board_list[0] == symbol and board_list[3] == symbol and board_list[6] == symbol:
        return True

    elif board_list[1] == symbol and board_list[4] == symbol and board_list[7] == symbol:
        return True

    elif board_list[2] == symbol and board_list[5] == symbol and board_list[8] == symbol:
        return True

    elif board_list[0] == symbol and board_list[4] == symbol and board_list[8] == symbol:
        return True

    elif board_list[6] == symbol and board_list[4] == symbol and board_list[2] == symbol:
        return True

    else:
        return False


def game_start(board_list, symbol_player1, symbol_player2):

    turn = 0

    while True:
        # player 1 choose position
        p1_position = choose_position("player1! ", board_list)

        '''update display'''
        '''clear_output()'''
        board_list[p1_position - 1] = symbol_player1
        game_display(board_list)

        # check if player1 won
        if win_check(board_list, symbol_player1):
            print("Congratulations Player1 Won!!!")
            break

        # check if it's a draw - when there is no empty position left and no one has won yet
        # the check is here because only player 1 will have 5 turns if it is a draw
        turn += 1
        if turn == 5:
            print("DRAw!!! Nobody Won")
            break

        # ask player2 to choose a position
        p2_position = choose_position("player2! ", board_list)

        '''update display'''
        '''clear_output()'''
        board_list[p2_position - 1] = symbol_player2
        game_display(board_list)

        # check if player2 won
        if win_check(board_list, symbol_player2):
            print("Congratulations Player2 Won!!!")
            break


def tic_tac_toe():

    symbol_player1 = ''
    symbol_player2 = ''
    want_to_play = True

    while want_to_play:
        print("Welcome to Tic Tac Toe! \n")

        board_list = [" ", ' ', " ", ' ', " ", ' ', " ", ' ', " "]

        '''ask player1 to chose a symbol'''
        symbol_player1 = choose_symbol()

        # set player2's symbol
        if symbol_player1 == 'X':
            symbol_player2 = "O"
        else:
            symbol_player2 = "X"

        '''display game board'''
        '''clear_output()'''
        game_display(board_list)

        '''start game'''
        game_start(board_list, symbol_player1, symbol_player2)

        '''check if they still want to play'''
        want_to_play = play_again()


tic_tac_toe()

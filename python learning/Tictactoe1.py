# 1. Display game board with  9 positions for x and o
# 2 make sure the board is empty at the start of the game
# 3make numbered cells so each player can refer to it
# 4 place error messages for placing a number in a filled cell
# 5if a player a line of 3 symbols , provide you won message

theBoard ={'1':' ', '2':' ', '3':' ',
           '4':' ', '5':' ', '6':' ',
           '7':' ', '8':' ', '9':' '}
boardKeys = []
#
# for key in theBoard:
#     boardKeys.append(key)
# print(boardKeys)
print(theBoard)

#function that prints out the board
def game_board(board):
    print('  |  |  ')
    print(' ' + board['1'] + '| ' + board['2'] + '|' + board['3'])
    print('---------')
    print('  |  |  ')
    print(' ' + board['4'] + '| ' + board['5'] + '|' + board['6'])
    print('----------')
    print('  |  |  ')
    print(' ' + board['7'] + '| ' + board['8'] + '| ' + board['9'])



#now we will write the function that has the game functionality
def game():
 try:
    turn = 'X'   #player starts first
    count = 0
    print('Welcome To The TicTacToe Game')

    for i in range(10):
        game_board(theBoard)
        print(f'It is the turn of {turn}. Specify which direction you want to go')
        move = input()      #the move of the players

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count+=1
        else:
            print('The position is already filled. choose another position')
            continue
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                game_board(theBoard)
                print('Game Over')
                print(f'Game over {turn} wins the game')
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                game_board(theBoard)
                print('Game Over')
                print(f'Game over {turn} wins the game')
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                game_board(theBoard)
                print('Game Over')
                print(f'Game over {turn} wins the game')
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                game_board(theBoard)
                print('Game Over')
                print(f'Game over {turn} wins the game')
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                game_board(theBoard)
                print('Game Over')
                print(f'Game over {turn} wins the game')
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                game_board(theBoard)
                print('Game Over')
                print(f'Game over {turn} wins the game')
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                game_board(theBoard)
                print('Game Over')
                print(f'Game over {turn} wins the game')
                break
            elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
                game_board(theBoard)
                print('Game Over')
                print(f'Game over {turn} wins the game')
                break
        if count == 9:
            game_board(theBoard)
            print('Game Over')
            print('It is a Tie')
            break
        #change the turns for the players
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'



    restart = input('will you like to start agian? (y/n)')
    if restart == 'y' or restart == 'Y':
        for key in theBoard:
            theBoard[key] = " "
        print(theBoard)
        game()
 except KeyError:
    print('Input a number')






if __name__ == '__main__':
    game()







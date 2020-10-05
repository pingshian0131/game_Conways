'''
Game of Life
Martin A. Aaberge
'''

from board import Board

def main(matrix, num):
    #assume the user types in a number
#    user_rows = int(input('how many rows? '))
#    user_columns = int(input('how many columns? '))

    user_rows = len(matrix)
    user_columns = len(matrix[0])

    # create a board:
    game_of_life_board = Board(user_rows,user_columns, matrix)

    #run the first iteration of the board:
    game_of_life_board.draw_board()
    #game_of_life_board.update_board()

    for i in range(num):
        game_of_life_board.update_board()
    game_of_life_board.draw_board()

if __name__ == '__main__':
    ##### b = 2-d array 
    x = [[0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0], 
     [0, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]
    num = input("請輸入life cycle: ")
    main(x, int(num))

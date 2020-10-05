'''
Game of Life
Board Class
Martin A. Aaberge
'''

from cell import Cell
from random import randint

class Board:
    def __init__(self , rows , columns, matrix):
        '''
        constructor holds input from user and populates the grid with cells. 
        '''
        self._rows = rows
        self._columns = columns   
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]
        self._matrix = matrix 

        self._generate_board()

    def draw_board(self):
        '''
        method that draws the actual board in the terminal
        '''
        print('\n'*10)
        print('printing board')
        for row in self._matrix:
            for column in row:
                print(column, end=', ')
            print () 

    def _generate_board(self):
        '''
        method that sets the random state of all cells.
        '''

        for i, row in enumerate(self._grid):
            for j, column in enumerate(row):
                if self._matrix[i][j] == 1:
                    column = 1

    def update_board(self):
        '''
        method that updates the board based on
        the check of each cell pr. generation
        '''
        #cells list for living cells to kill and cells to resurrect or keep alive
        goes_alive = []
        gets_killed = []

        for row in range(len(self._matrix)):
            for column in range(len(self._matrix[row])):
                #check neighbour pr. square:
                check_neighbour = self.check_neighbour(row , column)
                
                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    #check live status for neighbour_cell:
                    if neighbour_cell:
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self._matrix[row][column]

                status_main_cell = cell_object

                #If the cell is alive, check the neighbour status.
                if status_main_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append([row,column])

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append([row,column])

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append([row,column])
        #sett cell statuses
        for point in goes_alive:
            [i, j] = point 
            self._matrix[i][j] = 1
        for point in gets_killed:
            [i, j] = point
            self._matrix[i][j] = 0
    
    
    def check_neighbour(self, check_row , check_column):
        '''
        method that checks all the neighbours for all the cells
        and returns the list of the valid neighbours so the update 
        method can set the new status
        '''        
        #how deep the search is:
        search_min = -1
        search_max = 2

        #empty list to append neighbours into.
        neighbour_list = []
        for row in range(search_min,search_max):
            for column in range(search_min,search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column 
                
                valid_neighbour = True

                if (neighbour_row) == check_row and (neighbour_column) == check_column:
                    valid_neighbour = False

                if (neighbour_row) < 0 or (neighbour_row) >= self._rows:
                    valid_neighbour = False

                if (neighbour_column) < 0 or (neighbour_column) >= self._columns:
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour_list.append(self._matrix[neighbour_row][neighbour_column])
        return neighbour_list

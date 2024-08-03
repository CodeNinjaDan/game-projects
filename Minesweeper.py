

import random
import re

# New board object to represent minesweeper game
class Board:
    def __init__(self, dim_size,num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        # Create board using helper function
        self.board = self.make_new_board()#plant the bombs
        self.assign_values_to_board()
        
        #initialize to keep track of locations uncovered
        #use a list of lists since this is a 2D board

        self.dug = set() #keep track of where I have dug

    def make_new_board(self):
        board =[[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        #plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1) #return a random integer N such that a <= N <= b
            row = loc // self.dim_size #no of times dim_size goes into loc to know what row to look at
            col = loc % self.dim_size #get remainder to know what index in that row to look at

            if board[row][col] == '*':
                continue #keep going because there's already a bomb

            board[row][col] = '*'
            bombs_planted += 1

        return board
    
    def assign_values_to_board(self):
        # Assign a number 0-8 for all the empty spaces which represents how many neighbouring bombs there are
        # which saves effort checking what's around the board later on
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue #if this is already a bomb, no calculation is required
                self.board[r][c] = self.get_num_neighbouring_bombs(r, c)

    def get_num_neighbouring_bombs(self, row, col):
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        num_neighbouring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1

        return num_neighbouring_bombs
    
    def dig(self, row, col):
        # dig at that location!
        # return True if successful dig, False if bomb dug

        # a few scenarios:
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> recursively dig neighbors!

        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        #self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue #don't dig twice
                self.dig(r, c)

        #if initial dig didn't hit a bomb, it shouldn't hit a bomb here 
        return True
    
    def __str__(self):
        #return a string that shows a board to the player

        #array showing what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        string_rep = ''
        #get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        #print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = ' '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += ' '.join(cells)
        indices_row += ' \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
    
#Play the game
def play(dim_size=10, num_bombs=10):
    #1. Create board and plant the bombs
    board = Board(dim_size, num_bombs)
    #2. Show the user the board and ask for input
    #3. If location is a bomb, game over message
    #3. If location isn't a bomb , dig recursively until each square is at least next to a bomb
    #4. Repeat steps until Win
    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue
        #if it's valid, dig
        safe = board.dig(row, col)
        if not safe:
            break # dug a bomb
    if safe:
        print("YOU WIN!")
    else:
        print("GAME OVER! :(")
        #Reveal whole board
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()
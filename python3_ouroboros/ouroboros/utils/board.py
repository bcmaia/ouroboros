from screen import Screen


class Board:
    def __init__(self):
        self.screen = Screen()
        self.rows = self.screen.size[0]
        self.cols = self.screen.size[1]
        self.grid = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
    
    def __str__(self):
        return ''.join(map(lambda l: ''.join(l), self.grid))
    
    def get(self, row, col):
        return self.grid[row][col]
    
    def set(self, row, col, value):
        self.grid[row][col] = value
        self.screen.addstr(row, col, str(value))

    def set_col(self, col, char):
        #col = self.__to_col(col)
        for y in range(self.cols):
            self.grid[col] = char
        self.screen.set_column(col, str(char)[0] * self.cols)

    def __to_row(self, col):
        if 0 > col: return self.cols - (abs(col) % self.cols)
        else: return col % self.cols

    def __to_col(self, row):
        if 0 > row: return self.rows - (abs(row) % self.rows)        
        else: return row % self.rows       
        
    def set_row(self, row, char): 
        #row = self.__to_row(row)   
        l = [char] * self.cols
        self.grid[row] = l
        self.screen.set_line(row, ''.join(l))


try: 
    print('aaa')
    b = Board()
    print('bb')
    b.set_row(0, '#')
    b.set_row(5, '#')
    b.screen.input()
    del b.screen
    print(b)
except e:
    print(e)

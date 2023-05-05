import curses

class Screen:
    def __init__(self):
        # initialize curses
        self.stdscr = curses.initscr()

        # turn off echoing of keys and enable cbreak mode
        curses.noecho()
        curses.cbreak()

        # clear the screen
        self.stdscr.clear()

        # hide the cursor
        curses.curs_set(0)

    def __del__(self):
        # restore the terminal to its previous state
        curses.nocbreak()
        curses.echo()
        curses.curs_set(1)
        curses.endwin()

    def addstr(self, y, x, string):
        # print a string to the screen at the specified coordinates
        self.stdscr.addstr(y, x, string)

    @property
    def size(self):
        # return the size of the terminal as a named tuple
        return self.stdscr.getmaxyx()

    def input (self):
        c = self.stdscr.getch()
        return None if curses.ERR == c else c

    def refresh(self):
        self.stdscr.refresh()

    def set_column(self, x, string):
        # set a column of the screen to be equal to some string
        i = 0
        l = len(string)
        for y in range(self.size[0]):
            if i >= l: break
            self.stdscr.addstr(y, x, str(string[i]))
            i += 1

    def set_line(self, y, string):
        # set a row of the screen to be equal to some string
        i = 0
        l = len(string)
        for x in range(self.size[1]):
            if i >= l: break
            self.stdscr.addstr(y, x, string[i])
            i += 1


# Test  
if "__main__" == __name__:    
    s = Screen()
    a = s.input()
    s.set_line(2, 'ahajdkekwkks')
    a = s.input()
    del s

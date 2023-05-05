import os
import tty
import termios
import curses


def get_term_size ():
    # get the file descriptor for the current terminal
    fd = os.open(os.ctermid(), os.O_RDONLY)
    
    # get the current terminal attributes
    old_settings = termios.tcgetattr(fd)
    
    try:
        # set the terminal attributes to raw mode
        tty.setraw(fd)
        
        # get the size of the terminal
        return os.get_terminal_size()
        
    finally:
        # restore the original terminal attributes
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
        # close the file descriptor
        os.close(fd)
    
    raise Exception('Failed to assert terminal size')
     


class screen: 
def push_screen():
    # initialize curses
    stdscr = curses.initscr()

    # turn off echoing of keys and enable cbreak mode
    curses.noecho()
    curses.cbreak()

    # clear the screen
    stdscr.clear()

    # hide the cursor
    curses.curs_set(0)

    # return the stdscr object for the new screen
    return stdscr


def pop_screen(stdscr):
    # restore the terminal to its previous state
    curses.nocbreak()
    curses.echo()
    curses.curs_set(1)
    curses.endwin()







# push a new screen
new_screen = push_screen()

# print some output
new_screen.addstr(5, 10, "Hello, new screen!")
new_screen.addstr(7, 10, "Press any key to go back...")

# wait for a keypress
new_screen.getch()

# pop the new screen and restore the previous state
pop_screen(new_screen)

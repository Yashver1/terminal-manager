import curses


class TerminalUI():
    def __init__(self,height,width,y,x):
        self.screen = None 
        self.height = height
        self.width = width 
        self.y = y 
        self.x = x
        self.options = ["Start New Session","View Current Sessions","Delete Session"]
        self.first_height = None
        self.last_height = None

    def start_ui(self):
        self.ui_init()
        self.screen.clear()
        self.render_menu()
        self.screen.move(1,0)
        self.screen.refresh()


    def read_menu_input(self):
        key = self.screen.getch()
        return key
    def read_key(self):
        key = self.screen.getkey()
        return key

    def get_cursor_pos(self):
        position = self.screen.getyx()
        return position
    
    def ui_init(self):
        self.screen = curses.initscr()
        self.screen = curses.newwin(self.height,self.width,self.y,self.x)
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)

    def end_ui(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()
        self.screen.refresh()

    def render_menu(self):
        self.screen.addstr(0,0,"-"*(self.width-1))
        i = 1
        for j in range(len(self.options)): 
            height = i
            if self.first_height is None:
                self.first_height = height
            self.screen.addstr(i,0,f"{i//2}: {self.options[i//2]}")
            i+=2
        self.screen.addstr(height + 1,0,"-"*(self.width-1))
        self.last_height = height

    def check_mov(self,key):
        if key == curses.KEY_UP or key==curses.KEY_DOWN:
            return True
        return 

    def mov_cursor(self,key):
        position = self.get_cursor_pos()
        if len(position) != 2:
            raise ValueError("Missing pos value")
        y,x = position[0],position[1]
        if key == curses.KEY_UP:
            y = y-2
            y,x = self.boundary_check(y,x)
            self.screen.move(y,0)
        elif key == curses.KEY_DOWN:
            y = y+2
            y,x = self.boundary_check(y,x)
            self.screen.move(y,0)
        self.screen.refresh()

    def boundary_check(self,y,x):
        if y >= self.last_height:
            y = self.last_height
        elif y<= self.first_height:
            y = self.first_height
        #implement x not needed as nav is up down. But leave for future proof
        return y,x


    def check_confirm(self,command): 
        if command == curses.KEY_ENTER:
            return True
        return

    def check_quit(self,command):
        if command == ord('q'):
            return True
        return

    def render_cli(self):
        self.end_ui()
        self.screen = curses.initscr()
        curses.echo()
        curses.cbreak()
        self.screen.keypad(True)

        


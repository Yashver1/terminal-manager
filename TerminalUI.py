import curses


class TerminalUI():
    def __init__(self,height,width,y,x):
        self.screen = None 
        self.height = height
        self.width = width 
        self.y = y 
        self.x = x

    def start_ui(self):
        self.ui_init()
        self.screen.clear()
        self.render_menu()
        self.screen.move(1,0)
        self.screen.refresh()
    
    def read_input(self):
        key = self.screen.getch()
        return key

    def get_curr_pos(self):
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

    def render_menu(self):
        num_options = 5
        height = 0
        i = 1
        self.screen.addstr(0,0,"-"*(self.width-1))
        
        while i < self.height - 2: 
            self.screen.addstr(i,0,f"Option {i//2}: This is a dummy option\n")
            height = i
            i+=2
            
        self.screen.addstr(height + 1,0,"-"*(self.width-1))

    def mov_cursor(self,position,key):
        y,x = position[0],position[1]

        if key == curses.KEY_UP:
            return y-2,x
        elif key == curses.KEY_DOWN:
            return y+2,x
        elif key:
            return y,x

    def confirm(self,command): 
        if command == KEY_ENTER:
            return True
        return

    def end(self,command):
        if command == ord('q'):
            return 'q'
        return
        

ui = TerminalUI(20,40,20,40)
ui.start_ui()
ui.ui_end()


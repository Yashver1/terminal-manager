from terminal_model import TerminalModel
from terminal_ui import TerminalUI
import os
import curses
import time

class TerminalController():
    def __init__(self,view):
        self.model = TerminalModel()
        self.view = view
        self.model_interface = None

    def start(self):
       parent = self.model.spawn_shell()
       self.view.start_ui()
       self.model_interface = parent
       self.menu_read_loop()
       self.terminal_read_loop()

    def exit(self):
        self.model.close_shell()
        self.view.end_ui()

    def load_option(self):
        pass


    def menu_read_loop(self):
        while True: 
            key = self.view.read_menu_input()
            if self.view.check_mov(key) :
                self.view.mov_cursor(key)
            if self.view.check_quit(key):
                self.exit()
                return
            ##if self.view.check_confirm(key):
                #option = self.view.read_option()
            if key == ord('\n'):
                self.view.render_cli()
                return


    def terminal_read_loop(self):
        command = ""
        while True:
            key = self.view.read_key()
            if key == '\n':
                break
            if key == curses.KEY_BACKSPACE:
                command = command[:-2]
                self.view.screen.refresh()
            command+=key
        os.write(self.model_interface,command.encode('utf-8'))
        time.sleep(0.2)
        output = os.read(self.model_interface,1024)
        self.view.screen.clear()
        if not output:
            raise ValueError("output not generated")
        self.view.screen.addstr(0,0,output)
        self.view.screen.refresh()
    

            
        
       
       

from terminal_model import TerminalModel
from terminal_ui import TerminalUI
import os
import curses
import time

class TerminalController():
    def __init__(self,view):
        self.model = TerminalModel()
        self.view = view

    def start(self):
        self.model.spawn_shell()
        self.view.start_ui()
        self.menu_read_loop()
        while True:
            self.terminal_read_loop()
            self.model.spawn_shell()



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
                command+=key
                break
            if key == curses.KEY_BACKSPACE:
                command = comman[:-1]
                continue
            command+=key
        self.model.write(command)
        time.sleep(0.2)
        output = self.model.read()
        self.view.screen.clear()
        self.view.screen.addstr(0,0,output)
    

            
        
       
       

import os
import subprocess
import pty




class TerminalModel():

    def __init__(self):
        self.shell = os.environ["SHELL"].split('/')[-1]
        self.master,self.slave = pty.openpty()
        

    def spawn_shell(self):
        subprocess.Popen([self.shell],stdin=self.slave,stdout=self.slave,stderr=self.slave)
    
    def spawn_terminal(self):
        return subprocess.Popen(['kitty','@','launch','--type','overlay','bash'],stdin=self.master,stdout=self.master,stderr=self.master)
        





terminal = TerminalModel()
terminal.spawn_shell()
print(terminal.spawn_terminal())

    


import os
import subprocess
import pty




class TerminalModel():

    def __init__(self):
        self.shell = os.environ["SHELL"].split('/')[-1]
        self.master,self.slave = pty.openpty()
        

    def spawn_shell(self):
        subprocess.Popen([self.shell],stdin=self.slave,stdout=self.slave,stderr=self.slave)



    


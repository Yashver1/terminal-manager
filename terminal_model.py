import os
import subprocess
import pty
import pickle




class TerminalModel():

    def __init__(self):
        self.shell = None
        self.parent = None
        self.slave = None

    def spawn_shell(self):
        self.master,self.slave = pty.openpty()
        shell = os.environ["SHELL"].split('/')[-1]
        self.shell = subprocess.Popen([shell],stdin=self.slave,stdout=self.slave,stderr=self.slave)
        print(f"Shell({shell}) Start")
        return self.master

    def close_shell(self):
        if self.shell:
            self.shell.kill()
        else:
            raise ValueError("Shell already closed or does not exist")
        if self.master and self.slave:
            os.close(self.master)
            os.close(self.slave)
        else:
            raise ValueError("PTY already closed or does not exist")
        print("Shell Closed")
    

    def save_shell(self):
        pass


    def load_shell(self):
        pass




    

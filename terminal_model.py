import os
import subprocess
import pickle




class TerminalModel():

    def __init__(self):
        self.shell = None

    def spawn_shell(self):
        shell = os.environ["SHELL"].split('/')[-1]
        self.shell = subprocess.Popen([shell],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print(f"Shell({shell}) Start")

    def close_shell(self):
        if self.shell:
            self.shell.stdin.close()
            self.shell.terminate()
            self.shell.wait()
        else:
            raise ValueError("Shell already closed or does not exist")
    
    def write(self,command):
        command_encoded = command.encode()
        self.shell.stdin.write(command_encoded)

    def read(self):
        output,err = self.shell.communicate()
        if err:
            raise ValueError(f"{err}")
        output_decoded = output.decode()
        return output_decoded


    def save_shell(self):
        pass


    def load_shell(self):
        pass




    

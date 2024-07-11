import os
import pty
import subprocess
import select

class TerminalModel:
    def __init__(self):
        self.master_fd = None
        self.slave_fd = None
        self.process = None

    def spawn_shell(self):
        self.master_fd, self.slave_fd = pty.openpty()
        shell = os.environ.get("SHELL", "/bin/bash")
        self.process = subprocess.Popen(
            [shell], stdin=self.slave_fd, stdout=self.slave_fd, stderr=self.slave_fd, text=True
        )
        print(f"Shell ({shell}) started")

    def run_program(self, program):
        if self.process:
            os.write(self.master_fd, (program + '\n').encode())

    def interact(self):
        try:
            buffer = bytearray()  # Accumulate bytes read from the pty
            while True:
                r, w, e = select.select([self.master_fd], [], [])
                if self.master_fd in r:
                    data = os.read(self.master_fd, 1024)
                    if data:
                        buffer.extend(data)
                        try:
                            output = buffer.decode('utf-8')
                            print(output, end='', flush=True)
                            buffer.clear()  # Clear the buffer if decoding is successful
                        except UnicodeDecodeError:
                            # If decoding fails, keep the bytes in the buffer for the next read
                            pass
                    else:
                        break
        except KeyboardInterrupt:
            print("\nExiting interaction mode")

    def close_shell(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        if self.master_fd:
            os.close(self.master_fd)
        if self.slave_fd:
            os.close(self.slave_fd)
        print("Shell closed")

# Example usage
if __name__ == "__main__":
    terminal = TerminalModel()
    terminal.spawn_shell()
    terminal.run_program("nvim test.py")
    terminal.interact()
    terminal.close_shell()


import os
import pty
import select
import subprocess
import sys
import tty
import termios

def set_raw(fd):
    old_settings = termios.tcgetattr(fd)
    tty.setraw(fd)
    return old_settings

def main():
    # Create a new pseudo-terminal pair
    master_fd, slave_fd = pty.openpty()

    # Fork the process
    pid = os.fork()

    if pid == 0:
        # Child process
        os.close(master_fd)
        
        # Set the controlling terminal
        os.setsid()
        os.dup2(slave_fd, 0)  # stdin
        os.dup2(slave_fd, 1)  # stdout
        os.dup2(slave_fd, 2)  # stderr
        if os.isatty(slave_fd):
            tty.setraw(slave_fd)
        
        # Run the shell
        shell = os.environ.get("SHELL", "/bin/bash")
        subprocess.run([shell])
    else:
        # Parent process
        os.close(slave_fd)
        
        old_settings = set_raw(sys.stdin.fileno())

        try:
            while True:
                r, w, e = select.select([sys.stdin, master_fd], [], [])
                if sys.stdin in r:
                    input_data = os.read(sys.stdin.fileno(), 1024)
                    os.write(master_fd, input_data)
                if master_fd in r:
                    output_data = os.read(master_fd, 1024)
                    os.write(sys.stdout.fileno(), output_data)
        except OSError as e:
            print(f"Error: {e}")
        finally:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)
            os.close(master_fd)
            os.waitpid(pid, 0)

if __name__ == "__main__":
    main()


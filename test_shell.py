import os
import pty
import subprocess

def read_shell_output(master_fd):
    output = os.read(master_fd, 1024)
    return output.decode()

def write_to_shell(master_fd, data):
    os.write(master_fd, data.encode())

# Create a pseudoterminal
master_fd, slave_fd = pty.openpty()

# Create a shell process and connect it to the slave file descriptor
shell_process = subprocess.Popen(["bash"], stdin=slave_fd, stdout=slave_fd, stderr=slave_fd, close_fds=True)

# Write a command to the shell
import time

# Write a command to the shell
command = "ls -l\n"
write_to_shell(master_fd, command)

# Add a small delay to allow the shell to process the command
time.sleep(0.1)

# Read the output of the shell
output = read_shell_output(master_fd)
print(output)

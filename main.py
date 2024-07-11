from terminal_controller import TerminalController
from terminal_ui import TerminalUI



def main():
    view = TerminalUI(8,40,20,40)
    controller = TerminalController(view)
    controller.start()





if __name__ == '__main__':
    main()

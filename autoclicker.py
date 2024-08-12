from time import sleep
from keyboard import add_hotkey
from mouse import click

class AutoClicker:
    def __init__(self, time: float):
        self.__is_on = True
        self.__is_paused = True
        self.__time_between_clicks = time

    def start_program(self):
        """
        method that starts the program and check if its is paused
        if isn't, calls the left_click method.
        """
        print("starting program...")
        while self.__is_on:
            if not self.__is_paused:
                self.left_click()
            sleep(self.__time_between_clicks)

    def end_program(self):
        """
        method that updates the is_on atribute to false,
        making the program end.
        """
        print("ending program...")
        self.__is_on = False

    def pause_and_unpause_program(self):
        """
        method that pause and unpause the program,
        alerting the user about the updated status.
        """
        self.__is_paused = not self.__is_paused
        status = "paused" if self.__is_paused else "running"
        print(f"The program is now {status}.")

    def left_click(self):
        """
        method that simulates the mouse left click.
        """
        click()

    def set_hotkeys(self, keys: dict):
        """
        method that set the hotkeys to end, pause and unpause the program
        """
        add_hotkey(keys['end program'],
                   auto_clicker.end_program)
        add_hotkey(keys['pause/unpause'],
                   auto_clicker.pause_and_unpause_program)

    def get_hotkeys(self):
        """
        method that get the hotkeys to end, pause and unpause the program
        """
        end_program_hotkey = input(
            'Type the hotkey to end the program: ')
        pause_unpause_program = input(
            'Type the hotkey to pause/unpause the program: ')
        return {'end program': end_program_hotkey,
                'pause/unpause': pause_unpause_program}

auto_clicker = AutoClicker(0.01)
auto_clicker.set_hotkeys(auto_clicker.get_hotkeys())
auto_clicker.start_program()

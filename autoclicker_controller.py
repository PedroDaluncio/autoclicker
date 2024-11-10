from time import sleep
import json
from keyboard import add_hotkey
from mouse import click


class AutoClicker:
    def __init__(self):
        self.__is_on = True
        self.__is_paused = True
        self.__data = self.__read_file()

    def __read_file(self):
        with open("config.json", "r", encoding="UTF-8") as file:
            data = json.load(file)
            return data

    def __write_file(self, data_json: dict):
        with open("config.json", "w", encoding="UTF-8") as file:
            json.dump(data_json, file, indent=4, ensure_ascii=False)

    def start_program(self):
        """
        method that starts the program and check if its is paused
        if isn't, calls the left_click method.
        """
        print("starting program...")
        self.set_hotkeys()
        while self.__is_on:
            if not self.__is_paused:
                self.left_click()
            sleep(self.__data["time_between_clicks"])

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

    def set_hotkeys(self):
        """
        method that set the hotkeys to end, pause and unpause the program
        """
        add_hotkey(self.__data['end_program_hotkey'],
                   self.end_program)
        add_hotkey(self.__data['pause_unpause_program'],
                   self.pause_and_unpause_program)

    def get_hotkeys(self):
        """
        method that get the hotkeys to end, pause and unpause the program
        """
        self.__data["end_program_hotkey"] = input(
            'Type the hotkey to end the program: ')
        self.__data["pause_unpause_program"] = input(
            'Type the hotkey to pause/unpause the program: ')
        self.set_hotkeys()
        self.__write_file(self.__data)


if __name__ == '__main__':
    auto_clicker = AutoClicker()
    auto_clicker.start_program()

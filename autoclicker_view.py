import tkinter as tk
from tkinter import messagebox


class AutoClickerView():

    def __init__(self):
        self.values = []

    def main_screen(self):

        main_screen = tk.Tk()
        main_screen.title("AutoClicker")
        main_screen.geometry("900x700")

        start_button = tk.Button(main_screen, text="Start", command=self.start_program)
        start_button.pack(pady=10)

        end_button = tk.Button(main_screen, text="End", command=lambda: self.end_program(main_screen))
        end_button.pack(pady=10)

        config_button = tk.Button(main_screen, text="Config", command=lambda: print(self.open_config(main_screen)))
        config_button.pack(pady=10)

        main_screen.mainloop()

    def start_program(self):
        return True

    def end_program(self, screen):
        screen.destroy()

    def open_config(self, main_screen: tk.Frame, click_interval: float = 0.1, unpause_pause_key: str = "F7", end_key:str = "F8"):
        # Criando uma nova janela de configurações
        config_screen = tk.Toplevel(main_screen)
        config_screen.title("Configs")
        config_screen.geometry("600x500")

        # Widgets dentro da janela de configurações
        label = tk.Label(config_screen, text="Opções de Configurações")
        label.pack(pady=20)

        # salvar_btn = tk.Button(config_screen, text="Salvar", command=salvar_config)
        # salvar_btn.pack(pady=10)

        # Criar entradas com valores padrões
        label1 = tk.Label(config_screen, text="Click Interval: ")
        label1.pack(pady=5)
        input1 = tk.Entry(config_screen)
        input1.pack(pady=5)
        input1.insert(0, click_interval)  # Definindo valor padrão

        label2 = tk.Label(config_screen, text="Pause/Unpause key: ")
        label2.pack(pady=5)
        input2 = tk.Entry(config_screen)
        input2.pack(pady=5)
        input2.insert(0, unpause_pause_key)  # Definindo valor padrão

        label3 = tk.Label(config_screen, text="end program key: ")
        label3.pack(pady=5)
        input3 = tk.Entry(config_screen)
        input3.pack(pady=5)
        input3.insert(0, end_key)  # Definindo valor padrão

        # Botão para salvar as configurações
        save_button = tk.Button(config_screen, text="Salvar", command=lambda: self.destroy_window(config_screen, [click_interval, unpause_pause_key, end_key]))
        save_button.pack(pady=10)

    def destroy_window(self, window, values):
        self.values = values
        print(self.values)
        window.destroy()

import tkinter as tk
from tkinter import messagebox


class AutoClickerView():

    def main_screen(self):

        main_screen = tk.Tk()
        main_screen.title("AutoClicker")
        main_screen.geometry("900x700")

        start_button = tk.Button(main_screen, text="Start", command=self.start_program)
        start_button.pack(pady=10)

        end_button = tk.Button(main_screen, text="End", command=lambda: self.end_program(main_screen))
        end_button.pack(pady=10)

        config_button = tk.Button(main_screen, text="Config", command=lambda: self.open_config(main_screen))
        config_button.pack(pady=10)

        main_screen.mainloop()

    def start_program(self):
        return True

    def end_program(self, screen):
        screen.destroy()

    def open_config(self, main_screen):
        # Criando uma nova janela de configurações
        config_screen = tk.Toplevel(main_screen)
        config_screen.title("Configs")
        config_screen.geometry("600x500")

        # Widgets dentro da janela de configurações
        label = tk.Label(config_screen, text="Opções de Configurações")
        label.pack(pady=20)

        def salvar_config():
            messagebox.showinfo("Configurações", "Configurações salvas!")
            config_screen.destroy()

        salvar_btn = tk.Button(config_screen, text="Salvar", command=salvar_config)
        salvar_btn.pack(pady=10)
    def abrir_configuracoes(self, val1, val2, val3):
        # Criar a janela de configurações
        janela_configuracoes = tk.Toplevel(self.main_screen)
        janela_configuracoes.title("Configurações")
        janela_configuracoes.geometry("300x200")

        # Criar entradas com valores padrões
        label1 = tk.Label(janela_configuracoes, text="Config 1")
        label1.pack(pady=5)
        input1 = tk.Entry(janela_configuracoes)
        input1.pack(pady=5)
        input1.insert(0, val1)  # Definindo valor padrão

        label2 = tk.Label(janela_configuracoes, text="Config 2")
        label2.pack(pady=5)
        input2 = tk.Entry(janela_configuracoes)
        input2.pack(pady=5)
        input2.insert(0, val2)  # Definindo valor padrão

        label3 = tk.Label(janela_configuracoes, text="Config 3")
        label3.pack(pady=5)
        input3 = tk.Entry(janela_configuracoes)
        input3.pack(pady=5)
        input3.insert(0, val3)  # Definindo valor padrão

        # Botão para salvar as configurações
        save_button = tk.Button(janela_configuracoes, text="Salvar",
                                command=lambda: self.salvar_config(input1.get(), input2.get(), input3.get()))
        save_button.pack(pady=10)


a = AutoClickerView()
a.main_screen()
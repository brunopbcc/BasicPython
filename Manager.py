import os
import subprocess
import tkinter as tk
from tkinter import ttk, scrolledtext

class ScriptRunnerApp:
    def __init__(self, root, scripts_path):
        self.root = root
        self.root.title("Script Runner")
        self.scripts_path = scripts_path
        self.scripts = self.get_scripts()

        # Lista de scripts
        self.script_list = ttk.Combobox(root, values=self.scripts, state="readonly")
        self.script_list.grid(row=0, column=0, padx=10, pady=10)
        self.script_list.bind("<<ComboboxSelected>>", self.load_script)

        # Botão para executar o script
        self.run_button = tk.Button(root, text="Run Script", command=self.run_script)
        self.run_button.grid(row=0, column=1, padx=10, pady=10)

        # Área de entrada para o usuário (se necessário)
        self.input_label = tk.Label(root, text="Input:")
        self.input_label.grid(row=1, column=0, sticky="w", padx=10)
        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.grid(row=1, column=1, padx=10, pady=5)

        # Área de saída do terminal
        self.output_text = scrolledtext.ScrolledText(root, width=80, height=20)
        self.output_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def get_scripts(self):
        # Busca scripts Python no diretório especificado
        return [f for f in os.listdir(self.scripts_path) if f.endswith('.py')]

    def load_script(self, event):
        # Limpa a área de saída ao carregar um novo script
        self.output_text.delete(1.0, tk.END)

    def run_script(self):
        # Obtém o nome do script selecionado e o input do usuário
        script_name = self.script_list.get()
        user_input = self.input_entry.get()

        if not script_name:
            self.output_text.insert(tk.END, "Please select a script.\n")
            return

        # Constrói o comando para executar o script
        script_path = os.path.join(self.scripts_path, script_name)
        command = f"python {script_path}"

        # Executa o script com o input do usuário, se houver
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        stdout, stderr = process.communicate(input=user_input)

        # Exibe a saída no terminal
        self.output_text.insert(tk.END, f"Output of {script_name}:\n")
        self.output_text.insert(tk.END, stdout if stdout else stderr)
        self.output_text.insert(tk.END, "\n" + "="*50 + "\n")

# Caminho do diretório dos scripts
scripts_directory = "C:/Users/bruno/PycharmProjects/BasicPythonProjects"

# Configuração da interface
root = tk.Tk()
app = ScriptRunnerApp(root, scripts_directory)
root.mainloop()

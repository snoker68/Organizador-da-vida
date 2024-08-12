import tkinter as tk

tarefa = ()

def abrir_tarefa():
    print("abrir tarefas")

def abrir_calendario():
    print("Abrir Calendario")

def abrir_configuração():
    print("abrir configuração")

def obter_ultima_tarefa_criada():
    return tarefa [-1] if tarefa else "Nenhuma tarefa disponivel"

root = tk.Tk()
root.title ("menu principal")

tk.Label(root,text="Menu principal", font=("Ariel", 16)).pack(pady=10)

tk.Button(root,text="Tarefas", font=("Ariel",20)).pack(pady=5)
tk.Button(root,text="Calendario", font=("Ariel",20)).pack(pady=5)
tk.Button(root,text="Configuração", font=("Ariel",20)).pack(pady=5)

ultima_tarefa_criada = obter_ultima_tarefa_criada()
tk.Label(root,text= f"Ultima tarefa: {ultima_tarefa_criada}", font=("Ariel", 12)), fg= "blue".pack(side='botton', pady=20)

root.mainloop()
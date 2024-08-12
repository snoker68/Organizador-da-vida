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

def preciso_ajuda():
    print("Abrir preciso de Ajuda")

#Menu pricipal 
root = tk.Tk()
root.title ("menu principal")
root.geometry("1980x1020")


tk.Label(root,text="Menu principal", font=("Ariel", 16)).pack(pady=10)

tk.Button(root,text="Tarefas", command=abrir_tarefa, width=20, bg="lightblue", fg="darkblue").pack(pady=5)
tk.Button(root,text="Calendario", command=abrir_calendario, width=20, bg="lightgreen", fg="darkgreen").pack(pady=5)
tk.Button(root,text="Configuração", command=abrir_configuração, width=20, bg="lightgrey", fg="black").pack(pady=5)
tk.Button(root, text="Ajuda", command=preciso_ajuda, width=20).pack(pady=5)

ultima_tarefa_criada = obter_ultima_tarefa_criada()
tk.Label(root, text=f"Ultima tarefa: {ultima_tarefa_criada}", font=("Arial", 12), fg="blue").pack(side='bottom', pady=20)

root.mainloop()
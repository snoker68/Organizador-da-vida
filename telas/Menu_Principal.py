import tkinter as tk
from telas.Tarefas import abrir_tarefas

 
def abri_menu_principal(root):
    root.title ("menu principal")
    root.geometry("1980x1020")

# Título
    tk.Label(root, text="Menu Principal", font=("Arial", 16)).pack(pady=10)

    # Botões do menu principal
    tk.Button(root, text="Tarefas", command=lambda: abrir_tarefas(root), width=20).pack(pady=5)
    tk.Button(root, text="Calendário", command=lambda: print("Abrir Calendário"), width=20).pack(pady=5)
    tk.Button(root, text="Configurações", command=lambda: print("Abrir Configurações"), width=20).pack(pady=5)

    # Exibição da última tarefa na parte inferior
    ultima_tarefa = "Estudar Python"
    tk.Label(root, text=f"Última Tarefa: {ultima_tarefa}", font=("Arial", 12), fg="blue").pack(side="bottom", pady=20)

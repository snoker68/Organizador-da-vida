
import tkinter as tk

def abrir_tarefas(root):
    # Esconde a janela principal
    root.withdraw()
    
    # Cria a nova janela para as tarefas
    tarefas_window = tk.Toplevel(root)
    tarefas_window.title("Tarefas")

    # Botões para as funcionalidades de tarefas
    tk.Button(tarefas_window, text="Criar Nova Tarefa", command=lambda: print("Criar nova tarefa"), width=30).pack(pady=10)
    tk.Button(tarefas_window, text="Ver Tarefas Concluídas", command=lambda: print("Ver tarefas concluídas"), width=30).pack(pady=10)
    tk.Button(tarefas_window, text="Ver Tarefas Pendentes", command=lambda: print("Ver tarefas pendentes"), width=30).pack(pady=10)
    
    # Botão para voltar ao menu principal
    tk.Button(tarefas_window, text="Voltar ao Menu Principal", command=lambda: voltar_ao_menu_principal(tarefas_window, root), width=30).pack(pady=10)

def voltar_ao_menu_principal(tarefas_window, root):
    # Fecha a janela de tarefas
    tarefas_window.destroy()
    # Reexibe a janela principal
    root.deiconify()
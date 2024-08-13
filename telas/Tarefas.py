import tkinter as tk
from tkinter import ttk

def abrir_tarefas(root):
   
    root.withdraw()
    
    tarefas_window = tk.Toplevel(root)
    tarefas_window.title("Tarefas")
    root.geometry("1980x1020")


    list_frame = tk.Frame(tarefas_window)
    list_frame.pack(padx=10, pady= 10, fill='both', expand= True)

    tarefas_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE)
    tarefas_listbox.pack(side=tk.LEFT, fill='both', expand=True)

    #scrollbar = tk.Scrollbar(list_frame, orient=tk.vertical, command=tarefas_listbox.yview)
    #scrollbar.pack(side=tk.RIGHT, fill='y')
    #tarefas_listbox.config(yscrollcommand=scrollbar.set)

    form_frame = tk.Frame(tarefas_window)
    form_frame.pack(padx=10, pady=10, fill='x')

    tk.Label(form_frame, text="Descrição da tarefa:").pack()
    descricao_entry = tk.Entry(form_frame, width=40)
    descricao_entry.pack(pady=5)

    def adicinar_tarefa():
        descricao = descricao_entry.get()
        if descricao:
            tarefas_listbox.insert(tk.END, descricao)
            descricao_entry.delete(0, tk.END)
    
    adicinar_button = tk.Button(form_frame, text="adicinar Tarefa", command=adicinar_tarefa)
    adicinar_button.pack(pady=5)

    def editar_tarefa():
        try:
            selectd_index = tarefas_listbox.curselection()[0]
            descricao =  descricao_entry.get()
            if descricao:
                tarefas_listbox.delete(selectd_index)
                tarefas_listbox.insert(selectd_index, descricao)
                descricao_entry.delete(0, tk.END)
        except IndexError:
            pass
    
    def excluir_tarefa():
        try:
            selected_index = tarefas_listbox.curselection()[0]
            tarefas_listbox.delete(selected_index)
        except IndexError:
            pass
        
    editar_button = tk.Button(form_frame, text="editar tarefa", command=editar_tarefa)
    editar_button.pack(pady=5, side=tk.LEFT, padx=5)

    excluir_button = tk.Button(form_frame, text="excluir tarefa", command=excluir_tarefa)
    excluir_button.pack(pady=5, side=tk.LEFT, padx=5)
    
    # Botão para voltar ao menu principal
    tk.Button(tarefas_window, text="Voltar ao Menu Principal", command=lambda: voltar_ao_menu_principal(tarefas_window, root), width=30).pack(pady=10)

def voltar_ao_menu_principal(tarefas_window, root):
    # Fecha a janela de tarefas
    tarefas_window.destroy()
    # Reexibe a janela principal
    root.deiconify()
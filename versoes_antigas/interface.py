import tkinter as tk
from tkinter import messagebox

usuarios = []

def cadastrar_usuario():
    nome = entry_nome.get().strip()
    idade = entry_idade.get().strip()

    if nome == "":
        messagebox.showwarning("Aviso", "O nome não pode estar vazio.")
        return

    if not idade.isdigit():
        messagebox.showwarning("Aviso", "A idade deve ser um numero inteiro.")
        return

    usuario = {
        "nome": nome,
        "idade": idade

    }
   usuarios.append(usuario)
   messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")

   entry_nome.delete(0, tk.END)
   entry_idade.delete(0, tk.END)
   entry_nome.focus()

def listar_usuarios():
    resultado.delete("1.0", tk.END)

    if len(usuarios) == 0:
        resultado.insert(tk.END, "Nenhum usuário cadastrado.\n")
        return

    resultado.insert(tk.END, "=== USUÁRIOS CADASTRADOS ===\n")
    for i, usuario in enumerate(usuarios, start=1):
        resultado.insert(
            tk.END,
            f"{i}. Nome:{usuario['nome']} | idade:{usuario['idade']}\n"
)

def buscar_usuario():
    nome_busca = entry_nome.get().strip().lower()
    resultado.delete("1.0", tk.END)

   if nome_busca == "":
       messagebox.showwarning("Aviso", "Digite um nome para buscar.")
       return

   for usuario in usuarios:
       if usuario["nome"].lower() == nome_busca:
           resultado.insert(
               tk.END,
               f"Usuário encontrado:\nNome: {usuario['nome']} | idade: {usuario['idade']}\n"
)
return

  resultado.insert(tk.END, "Usuário não encontrado.\n")

janela = tk.Tk()
janela.title("Sistema de cadastro Quinelas")
janela.geometry("500x400")

label_titulo = tk.label(janela, text="Sistema de cadastro Quinelas", font=("arial, 17))
label_titulo.pack(pady=10)

label_nome = tk.label(janela, text="Nome:")
label_nome.pack()

entry_nome = tk.entry(janela, width=40)
entry_nome.pack(pady=5)

label_idade = tk.label(janela, text="idade:")
label_idade.pack()

entry_idade = tk.entry(janela, width=40)
entry_idade.pack(pady=5)

frame_botoes = tk.frame(janela)
frame_botoes.pack(pady=10)

btn_cadastrar = tk.button(frame_botoes, text="cadastrar", command=cadastrar_usuario)
btn_cadastrar.grid(row=0, column=0, padx=5)

btn_listar = tk.button(frame_botoes, text="Listar", command=listar_usuarios)
btn_listar.grid(row=0, column=1, padx=5)

btn_buscar = tk.button(frame_botoes, text="Buscar", command=buscar_usuario)
btn_buscar.grid(row=0, column=2, padx=5)

resutado = tk.text(janela, height=12, width=55)
resultado.pack(pady=10)

janela.mainloop()

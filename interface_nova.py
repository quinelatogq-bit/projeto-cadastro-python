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
        messagebox.showwarning("Aviso", "A idade deve ser um número inteiro.")
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
            f"{i}. Nome: {usuario['nome']} | Idade: {usuario['idade']}\n"
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
                f"Usuário encontrado:\nNome: {usuario['nome']} | Idade: {usuario['idade']}\n"
            )
            return

    resultado.insert(tk.END, "Usuário não encontrado.\n")


def remover_usuario():
    nome_busca = entry_nome.get().strip().lower()
    resultado.delete("1.0", tk.END)

    if nome_busca == "":
        messagebox.showwarning("Aviso", "Digite um nome para remover.")
        return

    for usuario in usuarios:
        if usuario["nome"].lower() == nome_busca:
            usuarios.remove(usuario)
            resultado.insert(tk.END, f"Usuário '{usuario['nome']}' removido com sucesso.\n")
            entry_nome.delete(0, tk.END)
            entry_idade.delete(0, tk.END)
            entry_nome.focus()
            return

    resultado.insert(tk.END, "Usuário não encontrado para remoção.\n")

def editar_usuario():
    nome_busca = entry_nome.get().strip().lower()
    nova_idade = entry_idade.get().strip()
    resultado.delete("1.0", tk.END)

    if nome_busca == "":
        messagebox.showwarning("Aviso", "Digite o nome do usuário para editar.")
        return

    if not nova_idade.isdigit():
        messagebox.showwarning("Aviso", "Digite uma nova idade válida.")
        return

    for usuario in usuarios:
        if usuario["nome"].lower() == nome_busca:
            usuario["idade"] = nova_idade
            resultado.insert(
                tk.END,
                f"Usuário '{usuario['nome']}' atualizado com sucesso para idade {nova_idade}.\n"
            )
            entry_nome.delete(0, tk.END)
            entry_idade.delete(0, tk.END)
            entry_nome.focus()
            return

    resultado.insert(tk.END, "Usuário não encontrado para edição.\n")

def limpar_resultado():
    resultado.delete("1.0", tk.END)


janela = tk.Tk()
janela.title("Sistema de Cadastro")
janela.geometry("550x420")

label_titulo = tk.Label(janela, text="Sistema de Cadastro", font=("Arial", 16))
label_titulo.pack(pady=10)

label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()

entry_nome = tk.Entry(janela, width=40)
entry_nome.pack(pady=5)

label_idade = tk.Label(janela, text="Idade:")
label_idade.pack()

entry_idade = tk.Entry(janela, width=40)
entry_idade.pack(pady=5)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

btn_cadastrar = tk.Button(frame_botoes, text="Cadastrar", command=cadastrar_usuario)
btn_cadastrar.grid(row=0, column=0, padx=5, pady=5)

btn_listar = tk.Button(frame_botoes, text="Listar", command=listar_usuarios)
btn_listar.grid(row=0, column=1, padx=5, pady=5)

btn_buscar = tk.Button(frame_botoes, text="Buscar", command=buscar_usuario)
btn_buscar.grid(row=0, column=2, padx=5, pady=5)

btn_remover = tk.Button(frame_botoes, text="Remover", command=remover_usuario)
btn_remover.grid(row=0, column=3, padx=5, pady=5)

btn_editar = tk.Button(frame_botoes, text="Editar", command=editar_usuario)
btn_editar.grid(row=0, column=4, padx=5, pady=5)

btn_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar_resultado)
btn_limpar.grid(row=0, column=5, padx=5, pady=5)

resultado = tk.Text(janela, height=12, width=60)
resultado.pack(pady=10)

janela.mainloop()

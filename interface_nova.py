from dados import carregar_dados, salvar_dados
import tkinter as tk
from tkinter import messagebox
from usuarios import cadastrar_usuario, listar_usuarios, buscar_usuario, remover_usuario, editar_usuario

dados = carregar_dados()

def acao_cadastrar():
    nome = entry_nome.get().strip()
    idade = entry_idade.get().strip()

    if nome == "":
        messagebox.showwarning("Aviso", "O nome não pode estar vazio.")
        return

    if not idade.isdigit():
        messagebox.showwarning("Aviso", "A idade deve ser um número inteiro.")
        return

    mensagem = cadastrar_usuario(nome, idade)
    messagebox.showinfo("Sucesso", mensagem)
    atualizar_lista()

    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)


def acao_listar():
    mensagem = listar_usuarios()
    resultado.insert(tk.END, mensagem + "\n")


def acao_buscar():
    nome = entry_nome.get().strip()
    mensagem = buscar_usuario(nome)
    resultado.insert(tk.END, mensagem + "\n")


def acao_remover():
    nome = entry_nome.get().strip()
    mensagem = remover_usuario(nome)
    resultado.insert(tk.END, mensagem + "\n")



def acao_editar():
    nome_antigo = entry_nome_antigo.get().strip()
    novo_nome = entry_nome.get().strip()
    nova_idade = entry_idade.get().strip()

    if nome_antigo == "" or novo_nome == "" or nova_idade == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos para editar.")
        return

    if not nova_idade.isdigit():
        messagebox.showwarning("Aviso", "A idade deve ser um número inteiro.")
        return

    mensagem = editar_usuario(nome_antigo, novo_nome, nova_idade)
    resultado.insert(tk.END, mensagem + "\n")

    entry_nome_antigo.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)

def limpar_resultado():
    resultado.delete("1.0", tk.END)


janela = tk.Tk()
janela.title("Sistema de Cadastro")
janela.geometry("550x420")

label_titulo = tk.Label(janela, text="Sistema de Cadastro", font=("Arial", 16))
label_titulo.pack(pady=10)

label_nome_antigo = tk.Label(janela, text="Nome antigo:")
label_nome_antigo.pack()

entry_nome_antigo = tk.Entry(janela, width=40)
entry_nome_antigo.pack(pady=5)

label_nome = tk.Label(janela, text="Novo nome:")
label_nome.pack()

entry_nome = tk.Entry(janela, width=40)
entry_nome.pack(pady=5)

label_idade = tk.Label(janela, text="Nova idade:")
label_idade.pack()

entry_idade = tk.Entry(janela, width=40)
entry_idade.pack(pady=5)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

btn_cadastrar = tk.Button(frame_botoes, text="Cadastrar", command=acao_cadastrar)
btn_cadastrar.grid(row=0, column=0, padx=5, pady=5)

btn_listar = tk.Button(frame_botoes, text="Listar", command=acao_listar)
btn_listar.grid(row=0, column=1, padx=5, pady=5)

btn_buscar = tk.Button(frame_botoes, text="Buscar", command=acao_buscar)
btn_buscar.grid(row=0, column=2, padx=5, pady=5)

btn_remover = tk.Button(frame_botoes, text="Remover", command=acao_remover)
btn_remover.grid(row=0, column=3, padx=5, pady=5)

btn_editar = tk.Button(frame_botoes, text="Editar", command=acao_editar)
btn_editar.grid(row=0, column=4, padx=5, pady=5)

btn_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar_resultado)
btn_limpar.grid(row=0, column=5, padx=5, pady=5)

resultado = tk.Text(janela, height=12, width=60)
resultado.pack(pady=10)

janela.mainloop()

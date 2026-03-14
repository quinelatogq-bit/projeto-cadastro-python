usuarios = []

def mostrar_menu():
    print("\n== SISTEMA DE CADASTRO ==")
    print("1 - cadastrar usuário")
    print("2 - lista de usuário")
    print("3 - buscar usuário")
    print("4 - Sair")

def  cadastrar_usuario():
     nome = input("digite o nome: ").strip()
     idade = input("digite a idade: ").strip()

     usuario = {
         "nome": nome,
         "idade": idade
}

     usuarios.append(usuario)
     print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    if len(usuarios)== 0:
        print("Nenhum usuário cadastrado.")
        return

    print ("\n=== USUÁRIOS CADASTRADOS ===")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. Nome: {usuario['nome']} | idade: {usuario['idade']}")

def buscar_usuario():
    nome_busca = input("Digite o nome para buscar: ").strip().lower()

    for usuario in usuarios:
        if usuario["nome"].lower() == nome_busca:
            print(f"Usuário encontrado: Nome: {usuario['nome']} | idade: {usuario['idade']}")
            return
    print("Usuário não encontrado.")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_usuario()
        elif opcao == "4":
            print("Encerrando o sistema...")
        else:
            print("opção inválida. Tente novamente.")
            break
main()

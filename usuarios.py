from dados import carregar_dados, salvar_dados


def cadastrar_usuario(nome, idade):
    usuarios = carregar_dados()

    usuario = {
        "nome": nome,
        "idade": idade
    }

    usuarios.append(usuario)
    salvar_dados(usuarios)
    return "Usuário cadastrado com sucesso!"


def listar_usuarios():
    usuarios = carregar_dados()

    if len(usuarios) == 0:
        return "Nenhum usuário cadastrado."

    texto = "\n=== USUÁRIOS CADASTRADOS ===\n"
    for i, usuario in enumerate(usuarios, start=1):
        texto += f"{i}. Nome: {usuario['nome']} | Idade: {usuario['idade']}\n"

    return texto


def buscar_usuario(nome_busca):
    usuarios = carregar_dados()
    nome_busca = nome_busca.strip().lower()

    for usuario in usuarios:
        if usuario["nome"].strip().lower() == nome_busca:
            return f"Usuário encontrado: Nome: {usuario['nome']} | Idade: {usuario['idade']}"

    return "Usuário não encontrado."


def remover_usuario(nome_remover):
    usuarios = carregar_dados()

    for usuario in usuarios:
        if usuario["nome"].strip().lower() == nome_remover.strip().lower():
            usuarios.remove(usuario)
            salvar_dados(usuarios)
            return "Usuário removido com sucesso!"

    return "Usuário não encontrado."


def editar_usuario(nome_antigo, novo_nome, nova_idade):
    usuarios = carregar_dados()
    nome_antigo = nome_antigo.strip().lower()

    for usuario in usuarios:
        if usuario["nome"].strip().lower() == nome_antigo:
            usuario["nome"] = novo_nome
            usuario["idade"] = nova_idade
            salvar_dados(usuarios)
            return "Usuário editado com sucesso!"

    return "Usuário não encontrado para edição."

class Usuario:
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    @classmethod
    def cadastrar(cls):
        print("\n=== CADASTRAR USUÁRIO ===")

        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")

        return cls(nome, email, senha)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome.strip() != "":
            self.__nome = nome
        else:
            print("Nome inválido.")

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if email.strip() != "":
            self.__email = email
        else:
            print("Email inválido.")

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        if senha.strip() != "":
            self.__senha = senha
        else:
            print("Senha inválida.")

    def alterar(self):
        print("\n=== ALTERAR USUÁRIO ===")

        novo_nome = input("Novo nome (ENTER para manter): ").strip()
        if novo_nome != "":
            self.set_nome(novo_nome)

        novo_email = input("Novo email (ENTER para manter): ").strip()
        if novo_email != "":
            self.set_email(novo_email)

        nova_senha = input("Nova senha (ENTER para manter): ").strip()
        if nova_senha != "":
            self.set_senha(nova_senha)

        print("Usuário alterado com sucesso.")

    def exibir_dados(self):
        return f"Nome: {self.__nome} | Email: {self.__email} | Senha: {self.__senha}"



class Jogo:

    def __init__(self, titulo, descricao, preco, empresa):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__preco = preco
        self.__empresa = empresa


    @classmethod
    def cadastrar(cls):
        print("\n=== CADASTRAR JOGO ===")

        titulo = input("Título: ")
        descricao = input("Descrição: ")
        preco = input("Preço: ")
        empresa = input("Empresa: ")

        return cls(titulo, descricao, preco, empresa)


    def get_titulo(self):
        return self.__titulo


    def set_titulo(self, titulo):
        if titulo.strip() != "":
            self.__titulo = titulo
        else:
            print("Título inválido.")


    def get_descricao(self):
        return self.__descricao


    def set_descricao(self, descricao):
        if descricao.strip() != "":
            self.__descricao = descricao
        else:
            print("Descrição inválida.")


    def get_preco(self):
        return self.__preco


    def set_preco(self, preco):
        if preco.strip() != "":
            self.__preco = preco
        else:
            print("Preço inválido.")


    def get_empresa(self):
        return self.__empresa


    def set_empresa(self, empresa):
        if empresa.strip() != "":
            self.__empresa = empresa
        else:
            print("Empresa inválida.")


    def alterar(self):
        print("\n=== ALTERAR JOGO ===")

        novo_titulo = input("Novo título (ENTER para manter): ")
        if novo_titulo != "":
            self.set_titulo(novo_titulo)

        nova_descricao = input("Nova descrição (ENTER para manter): ")
        if nova_descricao != "":
            self.set_descricao(nova_descricao)

        novo_preco = input("Novo preço (ENTER para manter): ")
        if novo_preco != "":
            self.set_preco(novo_preco)

        nova_empresa = input("Nova empresa (ENTER para manter): ")
        if nova_empresa != "":
            self.set_empresa(nova_empresa)


        print("Jogo alterado com sucesso.")


    def exibir_dados(self):
        return f"Título: {self.__titulo} | Descrição: {self.__descricao} | Preço: {self.__preco} | Empresa: {self.__empresa}"

class Biblioteca:

    def __init__(self, donousu):
        self.__donousu = donousu


    @classmethod
    def cadastrar(cls):
        print("\n=== CADASTRAR BIBLIOTECA ===")

        donousu = input("Dono da biblioteca: ")

        return cls(donousu)


    def get_donousu(self):
        return self.__donousu


    def set_donousu(self, donousu):
        if donousu.strip() != "":
            self.__donousu = donousu
        else:
            print("Dono inválido.")


    def alterar(self):
        print("\n=== ALTERAR BIBLIOTECA ===")

        novo_donousu = input("Novo dono (ENTER para manter): ")

        if novo_donousu != "":
            self.set_donousu(novo_donousu)

        print("Biblioteca alterada com sucesso.")


    def exibir_dados(self):
        return f"Dono da Biblioteca: {self.__donousu}"



class Jogo_Biblioteca:

    def __init__(self, jogoBIB):
        self.__jogoBIB = jogoBIB


    @classmethod
    def cadastrar(cls):
        print("\n=== ADICIONAR JOGO NA BIBLIOTECA ===")

        jogoBIB = input("Nome do jogo: ")

        return cls(jogoBIB)


    def get_jogoBIB(self):
        return self.__jogoBIB


    def set_jogoBIB(self, jogoBIB):
        if jogoBIB.strip() != "":
            self.__jogoBIB = jogoBIB
        else:
            print("Jogo inválido.")


    def alterar(self):
        print("\n=== ALTERAR JOGO DA BIBLIOTECA ===")

        novo_jogo = input("Novo jogo (ENTER para manter): ")

        if novo_jogo != "":
            self.set_jogoBIB(novo_jogo)

        print("Jogo alterado com sucesso.")


    def exibir_dados(self):
        return f"Jogo na Biblioteca: {self.__jogoBIB}"



class Carrinho:

    def __init__(self, usuario, jogoad, total):
        self.__usuario = usuario
        self.__jogoad = jogoad
        self.__total = total


    @classmethod
    def cadastrar(cls):
        print("\n=== CADASTRAR CARRINHO ===")

        usuario = input("Usuário: ")
        jogoad = input("Jogo adicionado: ")
        total = input("Total: ")

        return cls(usuario, jogoad, total)


    def get_usuario(self):
        return self.__usuario


    def set_usuario(self, usuario):
        if usuario.strip() != "":
            self.__usuario = usuario
        else:
            print("Usuário inválido.")


    def get_jogoad(self):
        return self.__jogoad


    def set_jogoad(self, jogoad):
        if jogoad.strip() != "":
            self.__jogoad = jogoad
        else:
            print("Jogo inválido.")


    def get_total(self):
        return self.__total


    def set_total(self, total):
        if total.strip() != "":
            self.__total = total
        else:
            print("Total inválido.")


    def alterar(self):

        print("\n=== ALTERAR CARRINHO ===")

        novo_usuario = input("Novo usuário (ENTER para manter): ")
        if novo_usuario != "":
            self.set_usuario(novo_usuario)


        novo_jogo = input("Novo jogo (ENTER para manter): ")
        if novo_jogo != "":
            self.set_jogoad(novo_jogo)


        novo_total = input("Novo total (ENTER para manter): ")
        if novo_total != "":
            self.set_total(novo_total)


        print("Carrinho alterado com sucesso.")


    def exibir_dados(self):
        return f"Usuário: {self.__usuario} | Jogo: {self.__jogoad} | Total: {self.__total}"

class Avaliacao:

    def __init__(self, avaliacao):
        self.__avaliacao = avaliacao

    @classmethod
    def cadastrar(cls):
        print("\n=== CADASTRAR AVALIAÇÃO ===")

        avaliacao = input("Digite sua avaliação (0 a 5): ")

        return cls(avaliacao)

    def get_avaliacao(self):
        return self.__avaliacao

    def set_avaliacao(self, avaliacao):
        if avaliacao.strip() != "":
            self.__avaliacao = avaliacao
        else:
            print("Avaliação inválida.")

    def alterar(self):
        print("\n=== ALTERAR AVALIAÇÃO ===")

        nova_avaliacao = input("Nova avaliação (ENTER para manter): ")

        if nova_avaliacao != "":
            self.set_avaliacao(nova_avaliacao)

        print("Avaliação alterada com sucesso.")

    def exibir_dados(self):
        return f"Minha avaliação: {self.__avaliacao}"



class Amigo:

    def __init__(self, emailamigo, nomeamigo):
        self.__emailamigo = emailamigo
        self.__nomeamigo = nomeamigo

    @classmethod
    def cadastrar(cls):
        print("\n=== CADASTRAR AMIGO ===")

        emailamigo = input("Email do amigo: ")
        nomeamigo = input("Nome do amigo: ")

        return cls(emailamigo, nomeamigo)

    def get_emailamigo(self):
        return self.__emailamigo

    def set_emailamigo(self, emailamigo):
        if emailamigo.strip() != "":
            self.__emailamigo = emailamigo
        else:
            print("Email inválido.")

    def get_nomeamigo(self):
        return self.__nomeamigo

    def set_nomeamigo(self, nomeamigo):
        if nomeamigo.strip() != "":
            self.__nomeamigo = nomeamigo
        else:
            print("Nome inválido.")

    def alterar(self):
        print("\n=== ALTERAR AMIGO ===")

        novo_email = input("Novo email (ENTER para manter): ")
        if novo_email != "":
            self.set_emailamigo(novo_email)

        novo_nome = input("Novo nome (ENTER para manter): ")
        if novo_nome != "":
            self.set_nomeamigo(novo_nome)

        print("Amigo alterado com sucesso.")

    def exibir_dados(self):
        return f"Email do Amigo: {self.__emailamigo} | Nome do Amigo: {self.__nomeamigo}"



class Transacao:

    def __init__(self, transacao, jogocomprado):
        self.__transacao = transacao
        self.__jogocomprado = jogocomprado

    @classmethod
    def cadastrar(cls):
        print("\n=== CADASTRAR TRANSAÇÃO ===")

        transacao = input("Tipo de transação: ")
        jogocomprado = input("Jogo comprado: ")

        return cls(transacao, jogocomprado)

    def get_transacao(self):
        return self.__transacao

    def set_transacao(self, transacao):
        if transacao.strip() != "":
            self.__transacao = transacao
        else:
            print("Transação inválida.")

    def get_jogocomprado(self):
        return self.__jogocomprado

    def set_jogocomprado(self, jogocomprado):
        if jogocomprado.strip() != "":
            self.__jogocomprado = jogocomprado
        else:
            print("Jogo inválido.")

    def alterar(self):
        print("\n=== ALTERAR TRANSAÇÃO ===")

        nova_transacao = input("Nova transação (ENTER para manter): ")
        if nova_transacao != "":
            self.set_transacao(nova_transacao)

        novo_jogo = input("Novo jogo comprado (ENTER para manter): ")
        if novo_jogo != "":
            self.set_jogocomprado(novo_jogo)

        print("Transação alterada com sucesso.")

    def exibir_dados(self):
        return f"Transação: {self.__transacao} | Jogo comprado: {self.__jogocomprado}"

usuarios = []
jogos = []
bibliotecas = []
jogos_biblioteca = []
carrinhos = []
avaliacoes = []
amigos = []
transacoes = []

def menu_usuario():
    while True:
        print("\n" + "="*40)
        print("           MENU USUÁRIOS")
        print("="*40)
        print("1 - Cadastrar Usuário")
        print("2 - Alterar usuário")
        print("3 - Listar usuários")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = Usuario.cadastrar()
            usuarios.append(usuario)
            print("Usuário cadastrado com sucesso.")

        elif opcao == "2":
            if len(usuarios) > 0:
                for i, usuario in enumerate(usuarios):
                    print(i, "-", usuario.exibir_dados())

                escolha = int(input("Escolha o usuário: "))
                usuarios[escolha].alterar()

            else:
                print("Nenhum usuário cadastrado.")

        elif opcao == "3":
            if len(usuarios) > 0:
                print("\n=== USUÁRIOS CADASTRADOS ===")

                for usuario in usuarios:
                    print(usuario.exibir_dados())

            else:
                print("Nenhum usuário cadastrado.")

        elif opcao == "0":
            print("Voltando...")
            break

        else:
            print("Opção inválida.")



def main():
    while True:
        print("\n" + "="*40)
        print("       SISTEMA DE GESTÃO")
        print("="*40)

        print("1 - Usuários")
        print("2 - Jogos")
        print("3 - Biblioteca")
        print("4 - Carrinho")
        print("5 - Avaliações")
        print("6 - Amigos")
        print("7 - Transações")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_usuario()

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Essa função ainda será implementada.")


if __name__ == "__main__":
    main()

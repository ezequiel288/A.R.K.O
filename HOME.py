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

    def __str__(self):
        return self.exibir_dados()

    @staticmethod
    def listar(lista_usuarios):
        """
        Lista todos os usuários cadastrados.

        CONCEITO: POLIMORFISMO
        --------------------------------------------------------
        A lista pode conter objetos Usuario e suas subclasses.
        Quando usamos print(usuario), cada objeto executa sua própria
        versão de exibir_dados() através do método __str__.
        """
        print("\n=== LISTAR USUÁRIOS ===")

        if len(lista_usuarios) == 0:
            print("Nenhum usuário cadastrado.")
            return

        for usuario in lista_usuarios:
            print(usuario)

    def remover_usuario(self):
        """
        Remove um usuário pelo e-mail.
        """

        print("\n=== REMOVER USUÁRIO ===")

        email = input("Digite o e-mail: ").strip()

        usuario = self.buscar_por_email(email)

        if usuario is None:
            print ("Usuário não encontrado.")
            return

        self.__usuarios.remove(usuario)
        self.salvar_dados()

        print("Usuário removido com sucesso.")


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

    def __str__(self):
        return self.exibir_dados()

    @staticmethod
    def listar(lista_jogos):
        """
        Lista todos os jogos cadastrados.
        """
        print("\n=== LISTAR JOGOS ===")

        if len(lista_jogos) == 0:
            print("Nenhum jogo cadastrado.")
            return

        for jogo in lista_jogos:
            print(jogo)

    def remover_jogo(self):
        """
        Remove um jogo pelo título.
        """

        print("\n=== REMOVER JOGO ===")

        titulo = input("Digite o título: ").strip()

        jogo = self.buscar_por_titulo(titulo)

        if jogo is None:
            print("Jogo não encontrado.")
            return

        self.__jogos.remove(jogo)
        self.salvar_dados()

    print("Jogo removido com sucesso.")

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

    def __str__(self):
        return self.exibir_dados()

    @staticmethod
    def listar(lista_bibliotecas):
        """
        Lista todas as bibliotecas cadastradas.
        """
        print("\n=== LISTAR BIBLIOTECAS ===")

        if len(lista_bibliotecas) == 0:
            print("Nenhuma biblioteca cadastrada.")
            return

        for biblioteca in lista_bibliotecas:
            print(biblioteca)

    def remover_biblioteca(self):
        """
        Remove um item da biblioteca.
        """

        print("\n=== REMOVER ITEM DA BIBLIOTECA ===")

        item = input("Digite o nome do item: ").strip()

        biblioteca = self.buscar_por_item(item)

        if biblioteca is None:
            print("Item não encontrado.")
            return

        self.__bibliotecas.remove(biblioteca)
        self.salvar_dados()

    print("Item removido com sucesso.")


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

    def __str__(self):
        return self.exibir_dados()

    @staticmethod
    def listar(lista_jogos_biblioteca):
        """
        Lista todos os jogos da biblioteca.
        """
        print("\n=== LISTAR JOGOS DA BIBLIOTECA ===")

        if len(lista_jogos_biblioteca) == 0:
            print("Nenhum jogo cadastrado na biblioteca.")
            return

        for item in lista_jogos_biblioteca:
            print(item)

    def remover_jogo_biblioteca(self):
        """
        Remove um jogo da biblioteca.
        """

        print("\n=== REMOVER JOGO ===")

        nome = input("Digite o nome do jogo: ").strip()

        item = self.buscar_por_nome(nome)

        if item is None:
            print("Jogo não encontrado.")
            return

        self.__itens.remove(item)
        self.salvar_dados()

    print("Jogo removido com sucesso.")


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

    def __str__(self):
        return self.exibir_dados()

    @staticmethod
    def listar(lista_carrinhos):
        """
        Lista todos os carrinhos cadastrados.
        """
        print("\n=== LISTAR CARRINHOS ===")

        if len(lista_carrinhos) == 0:
            print("Nenhum carrinho cadastrado.")
            return

        for carrinho in lista_carrinhos:
            print(carrinho)

    def remover_carrinho(self):
        """
        Remove um jogo do carrinho.
        """

        print("\n=== REMOVER JOGO DO CARRINHO ===")

        titulo = input("Digite o título do jogo: ").strip()

        carrinho = self.buscar_por_titulo(titulo)

        if carrinho is None:
            print("Jogo não encontrado no carrinho.")
            return

        self.__carrinhos.remove(carrinho)
        self.salvar_dados()

    print("Jogo removido do carrinho com sucesso.")


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

    def __str__(self):
        return self.exibir_dados()

    @staticmethod
    def listar(lista_avaliacoes):
        """
        Lista todas as avaliações cadastradas.
        """
        print("\n=== LISTAR AVALIAÇÕES ===")

        if len(lista_avaliacoes) == 0:
            print("Nenhuma avaliação cadastrada.")
            return

        for avaliacao in lista_avaliacoes:
            print(avaliacao)

    def remover_avaliacao(self):
        """
        Remove uma avaliação.
        """

        print("\n=== REMOVER AVALIAÇÃO ===")

        id_avaliacao = input("Digite o ID da avaliação: ").strip()

        avaliacao = self.buscar_por_id(id_avaliacao)

        if avaliacao is None:
            print("Avaliação não encontrada.")
            return

        self.__avaliacoes.remove(avaliacao)
        self.salvar_dados()

    print("Avaliação removida com sucesso.")


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

    def __str__(self):
        return self.exibir_dados()

    @staticmethod
    def listar(lista_amigos):
        print("\n=== LISTAR AMIGOS ===")
        if len(lista_amigos) == 0:
            print("Nenhum amigo cadastrado.")
            return
        for amigo in lista_amigos:
            print(amigo)

    @staticmethod
    def remover_amigo(lista_amigos, email_alvo):
        print("\n=== REMOVER AMIGO ===")
        for amigo in lista_amigos:
            if amigo.get_emailamigo() == email_alvo:
                lista_amigos.remove(amigo)
                print(f"Amigo {amigo.get_nomeamigo()} removido com sucesso.")
                return
        print("Amigo não encontrado na lista.")


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

    def __str__(self):
        return self.exibir_dados()

    @staticmethod
    def listar(lista_transacoes):
        """
        Lista todas as transações cadastradas.
        """
        print("\n=== LISTAR TRANSAÇÕES ===")

        if len(lista_transacoes) == 0:
            print("Nenhuma transação cadastrada.")
            return

        for transacao in lista_transacoes:
            print(transacao)
    
    def remover_transacao(self):
        """
        Remove uma transação pelo ID.
        """

        print("\n=== REMOVER TRANSAÇÃO ===")

        id_transacao = input("Digite o ID da transação: ").strip()

        transacao = self.buscar_por_id(id_transacao)

        if transacao is None:
            print("Transação não encontrada.")
            return

        self.__transacoes.remove(transacao)
        self.salvar_dados()

    print("Transação removida com sucesso.")


# ──────────────────────────────────────────
#  LISTAS DE ARMAZENAMENTO GLOBAL
# ──────────────────────────────────────────
usuarios = []
jogos = []
bibliotecas = []
jogos_biblioteca = []
carrinhos = []
avaliacoes = []
amigos = []
transacoes = []


# ──────────────────────────────────────────
#  SUBMENU — USUÁRIOS
# ──────────────────────────────────────────
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
                    print(i, "-", usuario)

                escolha = int(input("Escolha o usuário: "))
                usuarios[escolha].alterar()

            else:
                print("Nenhum usuário cadastrado.")

        elif opcao == "3":
            print("Entrou na opção 3")
            print("Quantidade de usuários:", len(usuarios))

            for usuario in usuarios:
                print(usuario)

            input("\nPressione ENTER para voltar...")

        elif opcao == "0":
            print("Voltando...")
            break

        else:
            print("Opção inválida.")

# ──────────────────────────────────────────
#  SUBMENU — JOGOS
# ──────────────────────────────────────────
def menu_jogo():
    while True:
        print("\n" + "="*40)
        print("           MENU JOGOS")
        print("="*40)
        print("1 - Cadastrar Jogos")
        print("2 - Alterar Jogos")
        print("3 - Listar Jogos")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            jogo = Jogo.cadastrar()
            jogos.append(jogo)
            print("Jogo cadastrado com sucesso.")

        elif opcao == "2":
            if len(jogos) > 0:
                for i, jogo in enumerate(jogos):
                    print(i, "-", jogo)

                escolha = int(input("Escolha o jogo: "))
                jogos[escolha].alterar()

            else:
                print("Nenhum jogo cadastrado.")

        elif opcao == "3":
            print("Entrou na opção 3")
            print("Quantidade de jogos:", len(jogos))

            for jogo in jogos:
                print(jogo)

            input("\nPressione ENTER para voltar...")

        elif opcao == "0":
            print("Voltando...")
            break

        else:
            print("Opção inválida.")

# ──────────────────────────────────────────
#  SUBMENU — BIBLIOTECA
# ──────────────────────────────────────────
def menu_biblioteca():
    while True:
        print("\n" + "="*40)
        print("           MENU BIBLIOTECA")
        print("="*40)
        print("1 - Cadastrar Biblioteca")
        print("2 - Alterar Biblioteca")
        print("3 - Listar Bibliotecas")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            biblioteca = Biblioteca.cadastrar()
            bibliotecas.append(biblioteca)
            print("Biblioteca cadastrada com sucesso.")

        elif opcao == "2":
            if len(bibliotecas) > 0:
                for i, biblioteca in enumerate(bibliotecas):
                    print(i, "-", biblioteca)

                escolha = int(input("Escolha a biblioteca: "))
                bibliotecas[escolha].alterar()

            else:
                print("Nenhuma biblioteca cadastrada.")

        elif opcao == "3":
            print("Entrou na opção 3")
            print("Quantidade de bibliotecas:", len(bibliotecas))

            for biblioteca in bibliotecas:
                print(biblioteca)

            input("\nPressione ENTER para voltar...")

        elif opcao == "0":
            print("Voltando...")
            break

        else:
            print("Opção inválida.")
        print("2 - Alterar biblioteca")
        print("3 - Listar bibliotecas")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            biblioteca = Biblioteca.cadastrar()
            bibliotecas.append(biblioteca)
            print("Biblioteca cadastrada com sucesso.")

        elif opcao == "2":
            if len(bibliotecas) > 0:
                for i, biblioteca in enumerate(bibliotecas):
                    print(i, "-", biblioteca)

                escolha = int(input("Escolha a biblioteca: "))
                bibliotecas[escolha].alterar()

            else:
                print("Nenhuma biblioteca cadastrada.")

        elif opcao == "3":
            print("Entrou na opção 3")
            print("Quantidade de bibliotecas:", len(bibliotecas))

            for biblioteca in bibliotecas:
                print(biblioteca)

            input("\nPressione ENTER para voltar...")

        elif opcao == "0":
            print("Voltando...")
            break

        else:
            print("Opção inválida.")

# ──────────────────────────────────────────
#  SUBMENU — CARRINHO
# ──────────────────────────────────────────
def menu_carrinho():
    while True:
        print("\n" + "="*40)
        print("           MENU CARRINHO")
        print("="*40)
        print("1 - Adicionar ao Carrinho")
        print("2 - Remover do Carrinho")
        print("3 - Listar Itens no Carrinho")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            carrinho = Carrinho.cadastrar()
            carrinho.append(carrinho)
            print("Carrinho adicionado ao carrinho com sucesso.")

        elif opcao == "2":
            if len(carrinho) > 0:
                for i, carrinho in enumerate(carrinho):
                    print(i, "-", carrinho)

                escolha = int(input("Escolha o carrinho: "))
                carrinho.pop(escolha)
                print("Carrinho removido do carrinho com sucesso.")

            else:
                print("Nenhum carrinho no carrinho.")

        elif opcao == "3":
            print("Entrou na opção 3")
            print("Quantidade de carrinhos:", len(carrinho))

            for carrinho in carrinho:
                print(carrinho)

            input("\nPressione ENTER para voltar...")

        elif opcao == "0":
            print("Voltando...")
            break

        else:
            print("Opção inválida.")
        print("2 - Alterar Carrinho")
        print("3 - Listar Carrinhos")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            carrinho = Carrinho.cadastrar()
            carrinho.append(carrinho)
            print("Carrinho cadastrado com sucesso.")

        elif opcao == "2":
            if len(carrinho) > 0:
                for i, carrinho in enumerate(carrinho):
                    print(i, "-", carrinho)

                escolha = int(input("Escolha o carrinho: "))
                carrinho[escolha].alterar()

            else:
                print("Nenhum carrinho cadastrado.")

        elif opcao == "3":
            print("Entrou na opção 3")
            print("Quantidade de carrinhos:", len(carrinho))

            for carrinho in carrinho:
                print(carrinho)

            input("\nPressione ENTER para voltar...")

        elif opcao == "0":
            print("Voltando...")
            break

        else:
            print("Opção inválida.")


# ──────────────────────────────────────────
#  SUBMENU — AVALIAÇÕES
# ──────────────────────────────────────────
def menu_avaliacoes():
    while True:
        print("\n" + "="*40)
        print("           MENU AVALIAÇÕES")
        print("="*40)
        print("1 - Cadastrar Avaliação")
        print("2 - Alterar avaliação")
        print("3 - Listar avaliações")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            avaliacao = Avaliacao.cadastrar()
            avaliacoes.append(avaliacao)
            print("Avaliação cadastrada com sucesso.")

        elif opcao == "2":
            if len(avaliacoes) > 0:
                for i, avaliacao in enumerate(avaliacoes):
                    print(i, "-", avaliacao)

                escolha = int(input("Escolha a avaliação: "))
                avaliacoes[escolha].alterar()

            else:
                print("Nenhuma avaliação cadastrada.")

        elif opcao == "3":
            print("Entrou na opção 3")
            print("Quantidade de avaliações:", len(avaliacoes))

            for avaliacao in avaliacoes:
                print(avaliacao)

            input("\nPressione ENTER para voltar...")

        elif opcao == "0":
            print("Voltando...")
            break

        else:
            print("Opção inválida.")

# ──────────────────────────────────────────
#  SUBMENU — AMIGOS
# ──────────────────────────────────────────
def menu_amigos():
    while True:
        print("\n" + "="*40)
        print("           MENU AMIGOS")
        print("="*40)
        print("1 - Cadastrar Amigo")
        print("2 - Alterar Amigo")
        print("3 - Listar Amigos")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            amigo = Amigo.cadastrar()
            amigos.append(amigo)
            print("Amigo cadastrado com sucesso.")

        elif opcao == "2":
            if len(amigos) > 0:
                for i, amigo in enumerate(amigos):
                    print(i, "-", amigo)

                escolha = int(input("Escolha o amigo: "))
                amigos[escolha].alterar()

            else:
                print("Nenhum amigo cadastrado.")

        elif opcao == "3":
            print("Entrou na opção 3")
            print("Quantidade de amigos:", len(amigos))

            for amigo in amigos:
                print(amigo)

            input("\nPressione ENTER para voltar...")

        elif opcao == "0":
            print("Voltando...")
            break

        else:
            print("Opção inválida.")

# ──────────────────────────────────────────
#  SUBMENU — TRANSAÇÕES
# ──────────────────────────────────────────
def menu_transacoes():
    while True:
        print("\n" + "="*40)
        print("           MENU TRANSAÇÕES")
        print("="*40)
        print("1 - Cadastrar Transação")
        print("2 - Alterar Transação")
        print("3 - Listar Transações")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            transacao = Transacao.cadastrar()
            transacoes.append(transacao)
            print("Transação cadastrada com sucesso.")

        elif opcao == "2":
            if len(transacoes) > 0:
                for i, transacao in enumerate(transacoes):
                    print(i, "-", transacao)

                escolha = int(input("Escolha a transação: "))
                transacoes[escolha].alterar()

            else:
                print("Nenhuma transação cadastrada.")

        elif opcao == "3":
            print("Entrou na opção 3")
            print("Quantidade de transações:", len(transacoes))

            for transacao in transacoes:
                print(transacao)

            input("\nPressione ENTER para voltar...")

        elif opcao == "0":
            print("Voltando...")
            break

        else:
            print("Opção inválida.")


# ──────────────────────────────────────────
#  MENU PRINCIPAL
# ──────────────────────────────────────────
def main():
    while True:
        print("\n" + "="*40)
        print("       SISTEMA DE DISTRIBUIÇÃO DE JOGOS A.R.K.O")
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
        
        elif opcao == "2":
            menu_jogo()
        
        elif opcao == "3":
            menu_biblioteca()

        elif opcao == "4":
            menu_carrinho() 

        elif opcao == "5":
            menu_avaliacoes()

        elif opcao == "6":
            menu_amigos()

        elif opcao == "7":
            menu_transacoes()

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Função não implementada ou inválida.")


if __name__ == "__main__":
    main()

class Usuario:
    def __init__(self, nome, email, senha, amigos, saldo = 0, biblioteca = 0):
        self.__nome = nome
        self.__email = email
        self.__amigos = amigos
        self.__senha = senha
        self.__saldo = 0
        self.__biblioteca = 0
  
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome.strip() != "":
            self.__nome = nome
        else:
            print("nome inválido.")

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if email.strip() != "":
            self.__email = email
        else:
            print("email inválido.")

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        if senha.strip() != "":
            self.__senha = senha
        elif len(senha) > 8:
            print("senha inválido.")
        else:
            print("senha correta.")

    def get_amigos(self):
        return self.__amigos

    def set_nome(self, amigos):
        if amigos.strip() != "":
            self.__amigos = amigos
        else:
            print("amigos inválido.")


    def exibir_dados(self):
        """
        CONCEITO: ABSTRAÇÃO

        Este método representa uma ação geral:
        exibir os dados de uma pessoa.

        A classe Pessoa define que toda pessoa deve conseguir
        exibir seus dados, mas cada classe filha pode fazer isso
        de um jeito próprio.

        Aqui deixamos uma versão genérica.
        """
        return f"nome: {self.__nome} | email: {self.__email} | senha: {self.__senha} | saldo: {self.__saldo} | biblioteca: {self.__biblioteca} | amigos: {self.__amigos}"
    

"=============================================================================="

class Jogo:

    def __init__ (self, titulo, descricao, preco, empresa):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__preco = preco
        self.__empresa = empresa
     
    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        if titulo.strip() != "":
            self.__titulo = titulo
        else:
            print("titulo inválido.")

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        if descricao.strip() != "":
            self.__descricao = descricao
        else:
            print("descricao inválido.")

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco.strip() != "":
            self.__preco = preco
        else:
            print("preco correta.")

    def get_empresa(self):
        return self.__empresa

    def set_empresa(self, empresa):
        if empresa.strip() != "":
            self.__empresa = empresa
        else:
            print("empresa inválido.")


    def exibir_dados(self):
        """
        CONCEITO: ABSTRAÇÃO

        Este método representa uma ação geral:
        exibir os dados de uma pessoa.

        A classe Pessoa define que toda pessoa deve conseguir
        exibir seus dados, mas cada classe filha pode fazer isso
        de um jeito próprio.

        Aqui deixamos uma versão genérica.
        """
        return f"titulo: {self.__titulo} | descricao: {self.__descricao} | preco: {self.__preco} | empresa: {self.__empresa}"
    
    "=============================================================================="

class Empresa:

    def __init__(self, nomeEMP, games):
        self.__nomeEMP = nomeEMP
        self.__games = games
     
    def get_nomeEMP(self):
        return self.__nomeEMP

    def set_nomeEMP(self, nomeEMP):
        if nomeEMP.strip() != "":
            self.__nomeEMP = nomeEMP
        else:
            print("nomeEMP inválido.")

    def get_games(self):
        return self.__games

    def set_games(self, games):
        if games.strip() != "":
            self.__games = games
        else:
            print("game inválido.")


    def exibir_dados(self):
        """
        CONCEITO: ABSTRAÇÃO

        Este método representa uma ação geral:
        exibir os dados de uma pessoa.

        A classe Pessoa define que toda pessoa deve conseguir
        exibir seus dados, mas cada classe filha pode fazer isso
        de um jeito próprio.

        Aqui deixamos uma versão genérica.
        """
        return f"nomeEMP: {self.__nomeEMP} | games: {self.__games}"
    
    
"=============================================================================="

class Biblioteca:

    def __init__(self, donousu, item):
        self.__donousu = donousu
        self.__item = item
     
    def get_donousu(self):
        return self.__donousu

    def set_donousu(self, donousu):
        if donousu.strip() != "":
            self.__donousu = donousu
        else:
            print("donousu inválido.")

    def get_item(self):
        return self.__item

    def set_item(self, item):
        if item.strip() != "":
            self.__item = item
        else:
            print("item inválido.")


    def exibir_dados(self):
        """
        CONCEITO: ABSTRAÇÃO

        Este método representa uma ação geral:
        exibir os dados de uma pessoa.

        A classe Pessoa define que toda pessoa deve conseguir
        exibir seus dados, mas cada classe filha pode fazer isso
        de um jeito próprio.

        Aqui deixamos uma versão genérica.
        """
        return f"donousu: {self.__donousu} | item: {self.__item}"

"=============================================================================="

class Carrinho:

    def __init__(self,usuario, jogoad, total):
        self.__usuario = usuario
        self.__jogoad = jogoad
        self.__total = total
     
    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        if usuario.strip() != "":
            self.__usuario = usuario
        else:
            print("usuario inválido.")

    def get_jogoad(self):
        return self.__jogoad

    def set_jogoad(self, jogoad):
        if jogoad.strip() != "":
            self.__jogoad = jogoad
        else:
            print("jogoad inválido.")
            
    def get_total(self):
        return self.__jogoad

    def set_total(self, total):
        if total.strip() != "":
            self.__total = total
        else:
            print("total inválido.")
            
    def exibir_dados(self):
        """
        CONCEITO: ABSTRAÇÃO

        Este método representa uma ação geral:
        exibir os dados de uma pessoa.

        A classe Pessoa define que toda pessoa deve conseguir
        exibir seus dados, mas cada classe filha pode fazer isso
        de um jeito próprio.

        Aqui deixamos uma versão genérica.
        """
        return f"usuario: {self.__usuario} | jogoad: {self.__jogoad} | total: {self.__total}  "

"=============================================================================="

class Jogo_Biblioteca:

    def _init_(self, meusjogos):
        self.__meusjogos = meusjogos
  
    def get_meusjogos(self):
        return self.__meusjogos

    def set_meusjogos(self, meusjogos):
        if meusjogos.strip() != "":
            self.__meusjogos = meusjogos
        else:
            print("nome inválido.")

    def exibir_dados(self):
        """
        CONCEITO: ABSTRAÇÃO

        Este método representa uma ação geral:
        exibir os dados de uma pessoa.

        A classe Pessoa define que toda pessoa deve conseguir
        exibir seus dados, mas cada classe filha pode fazer isso
        de um jeito próprio.

        Aqui deixamos uma versão genérica.
        """
        return f"meusjogos: {self._meusjogos}"
    
"=============================================================================="

class Avaliação:

    def _init_(self,avaliação ):
        self.__avaliação = avaliação
  
    def get_avaliação(self):
        return self.__avaliação

    def set_avaliação(self, avaliação):
        if avaliação.strip() != "":
            self.__avaliação = avaliação
        elif avaliação > 5:
            print("avaliação invalida.")
        else:
            print("avaliação valida.")

    def exibir_dados(self):
        """
        CONCEITO: ABSTRAÇÃO

        Este método representa uma ação geral:
        exibir os dados de uma pessoa.

        A classe Pessoa define que toda pessoa deve conseguir
        exibir seus dados, mas cada classe filha pode fazer isso
        de um jeito próprio.

        Aqui deixamos uma versão genérica.
        """
        return f"Minha avaliação : {self._avaliação}"
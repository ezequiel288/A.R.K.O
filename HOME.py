class Usuario:
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
  
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

    def exibir_dados(self):
        
        return f"nome: {self.__nome} | email: {self.__email} | senha: {self.__senha}"
    

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

        return f"titulo: {self.__titulo} | descricao: {self.__descricao} | preco: {self.__preco} | empresa: {self.__empresa}"
    
    "=============================================================================="

class Biblioteca:

    def __init__(self, donousu):
        self.__donousu = donousu
     
    def get_donousu(self):
        return self.__donousu

    def set_donousu(self, donousu):
        if donousu.strip() != "":
            self.__donousu = donousu
        else:
            print("donousu inválido.")


    def exibir_dados(self):

        return f"Dono da Biblioteca: {self.__donousu}"

"=============================================================================="

class Jogo_Biblioteca:

    def __init__(self, jogoBIB):
        self.__jogoBIB = jogoBIB
     
    def get_jogoBIB(self):
        return self.__jogoBIB

    def set_jogoBIB(self, jogoBIB):
        if jogoBIB.strip() != "":
            self.__jogoBIB = jogoBIB
        else:
            print("Jogo adicionado inválido.")


    def exibir_dados(self):

        return f"Jogo adicionado a Biblioteca: {self.__jogoBIB}"

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
    
        return f"usuario: {self.__usuario} | jogoad: {self.__jogoad} | total: {self.__total}  "

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
 
        return f"Minha avaliação : {self._avaliação}"

"=============================================================================="

class Amigo:

    def __init__(self, emailamigo, nomeamigo):
        self.__emailamigo = emailamigo
        self.__nomeamigo = nomeamigo
     
    def get_emailamigo(self):
        return self.__emailamigo
    
    def set_emailamigo(self, emailamigo):
        if emailamigo.strip() != "":
            self.__emailamigo = emailamigo
        else:
            print("Email do amigo inválido.")

    def get_nomeamigo(self):
        return self.__item

    def set_nomeamigo(self, nomeamigo):
        if nomeamigo.strip() != "":
            self.__nomeamigo = nomeamigo
        else:
            print("Nome do amigo inválido.")

    def exibir_dados(self):

        return f"Email do Amigo: {self.__emailamigo} | Nome do Amigo: {self.__nomeamigo}"

"=============================================================================="

class Transação:

    def __init__(self, transacao, jogocomprado):
        self.__transacao = transacao
        self.__jogocomprado = jogocomprado

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
            print("Jogo a ser comprado inválido.")

    def exibir_dados(self):

        return f"Transação: {self.__transacao} | Jogo comprado: {self.__jogocomprado}"

"=============================================================================="
    
# ──────────────────────────────────────────
#  SUBMENU — USUÁRIOS
# ──────────────────────────────────────────
def menu_usuario():
    while True:                                    
        print("\n" + "="*40)
        print("           MENU USUÁRIOS")
        print("="*40)
        print("1 - Cadastrar Usuário")
        print("2 - Alterar cliente")
        print("3 - Deletar cliente")
        print("4 - Listar clientes")
        print("0 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if   opcao == "1": print("Método Cadastrar Cliente") 
        elif opcao == "2": print("Método Alterar Cliente") 
        elif opcao == "3": print("Método Deletar Cliente") 
        elif opcao == "4": print("Método Listar Cliente")
        elif opcao == "0":
            print("Voltando ao menu principal...")
            break                                   
        else:
            print("Opção inválida. Tente novamente.")


# ──────────────────────────────────────────
#  MENU PRINCIPAL
# ──────────────────────────────────────────
def main():
    while True:                                     
        print("\n" + "="*40)
        print("       SISTEMA DE GESTÃO")
        print("="*40)
        print("1 - Clientes")
        print("2 - Produtos")
        print("3 - Pedidos")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if   opcao == "1": menu_usuario()         
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break                                
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
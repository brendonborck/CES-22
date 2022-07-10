from abc import ABC

class Livaria(ABC):

    def __init__(self, produtos = [], clientes = [], compras = []):
        self._produtos = produtos
        self._clientes = clientes
        self._compras = compras

    def inserir(self, type, value):
        if type == "livro":
            self._produtos.append(value)
        elif type == "cliente":
            self._clientes.append(value)
        elif type == "compra":
            self._compras.append(value)
        else:
            print("Inválido.")

    def remover(self, type, value):
        if not self.consultar(self, type, value):
            print("Impossível alterar elemento inexistente.")
        elif type == "livro":
            self._produtos.remove(value)
        elif type == "cliente":
            self._clientes.remove(value)
        elif type == "compra":
            self._compras.remove(value)
        else:
            print("Inválido.")

    def consultar(self, type, value, autor = None):
        if type == "livro":
            if value == None:
                lista = []
                for produto in self._produtos:
                    if not produto.is_book():
                        continue
                    else:
                        if produto._autor == autor:
                            lista.append(produto)
                if not lista:
                    print("Consulta não encontra nada.")
                else:
                    print("Consulta encontra seguintes livros publicados pelo autor:")
                    for livro in lista:
                        print(livro._titulo)
            elif value in self._produtos:
                print("Consulta encontra produto.")
                return True
            else:
                print("Consulta não encontra nada.")
                return False
        elif type == "cliente":
            if value in self._clientes:
                print("Consulta encontra cliente.")
                return True
            else:
                print("Consulta não encontra nada.")
                return False
        elif type == "compra":
            if value in self._compras:
                print("Consulta encontra ordem de compra.")
                return True
            else:
                print("Consulta não encontra nada.")
                return False
        else:
            print("Inválido.")
            return False
    
    def alterar(self, type, previous, after):
        if not self.consultar(self, type, previous):
            print("Impossível alterar elemento inexistente.")
        elif type == "livro" or type == "cliente" or type == "compra":
            self.remover(previous)
            self.inserir(after)
        else:
            print("Inválido.")


class Produto(ABC):
    #poderia ser construída uma subclasse para os produtos da cafeteria

    def __init__(self, nome, venda, compra, impostos):
        self._nome = nome
        self._venda = venda
        self._compra = compra
        self.diferenca = venda - compra
        self.impostos = impostos

    def is_book(self):
        return False

    def mudar_imposto(self, novo_imposto):
        self.impostos = novo_imposto


class Livro(Produto):
    def __init__(self, titulo, autor, genero, edicao, editora, venda, compra, impostos):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._edicao = edicao
        self._editora = editora
        self._venda = venda
        self._compra = compra
        self.diferenca = venda - compra
        self.impostos = impostos

    def is_book(self):
        return True


class Autor(ABC):
    def __init__(self, nome, email, titulos = []):
        self._nome = nome
        self._email = email
        self._titulos = titulos

    def alterar_titulos(self, novos_titulos):
        self._titulos = novos_titulos


class Cliente(ABC):
    def __init__(self, nome, email, compras = []):
        self._nome = nome
        self._email = email
        self._compras = compras

    def alterar_compras(self, novas_compras):
        self._compras = novas_compras


class Compra(ABC):
    def __init__(self, produtos, quantidade, valores):
        self._produtos = produtos
        self._quantidade = quantidade
        self._valores = valores


# Main --------------------------------------------------------------------------------------------------------------

def main():



if __name__ == "__main__":
    main()
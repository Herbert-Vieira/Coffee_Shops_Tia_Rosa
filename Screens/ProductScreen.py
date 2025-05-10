from Entities.Product import Product
from Repository.ProductRepository import ProductRepository
import os


class ProductScreen:
    def __init__(self):
        self.repository = ProductRepository()

    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        text = """
        Bem vindo ao gerenciamento de produtos

        O que deseja fazer?
        1 - Cadastrar produto
        2 - Listar produtos
        3 - Atualizar produto
        4 - Remover produto
        5 - Voltar
        """

        print(text)

        self.get_options()

    def get_options(self):
        selection = input('Selecione uma opção: ')

        match selection:
            case '1':
                self.create_product()
            case '2':
                self.list_products()
            case '3':
                self.update_product()
            case '4':
                self.delete_product()
            case '5':
                from Screens.MainScreen import MainScreen
                MainScreen.start()
            case _:
                print('Opção inválida')

    def create_product(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Cadastro de produto')
        print('--------------------------')

        id = int(input('Digite o id do produto: '))
        name = input('Digite o nome do produto: ')
        price = float(input('Digite o preço do produto: '))

        try:
            product = Product(id, name, price)

            self.repository.create(product)

            print('Produto cadastrado com sucesso')
            input("Pressione Enter para continuar...")

        except Exception as e:
            print(e)
            input("Pressione Enter para continuar...")

        self.start()

    def list_products(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Lista de produtos')
        print('--------------------------')
        self.repository.read()
        print()
        input("Pressione Enter para continuar...")
        self.start()

    def update_product(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Atualização de produto')
        print('--------------------------')
        print('Lista de produtos')
        print()
        self.repository.read()
        print()
        id = input('Digite o id do produto que deseja atualizar: ')

        name = input('Digite o nome do produto: ')
        price = input('Digite o preço do produto: ')
        print()

        try:
            product = Product(int(id), name, float(price))

            self.repository.update(int(id), product)

            print('Produto atualizado com sucesso')

            input("Pressione Enter para continuar...")

        except Exception as e:
            print(e)
            input("Pressione Enter para continuar...")
            return

        self.start()

    def delete_product(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Remoção de produto')
        print('--------------------------')
        print('Lista de produtos')
        print()
        self.repository.read()
        print()
        id = int(input('Digite o id do produto que deseja remover: '))

        if isinstance(id, int) is False:
            print('Id inválido')
            input("Pressione Enter para continuar...")
            return

        self.repository.delete(id)

        print('Produto removido com sucesso')
        self.start()

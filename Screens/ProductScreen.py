from Entities.Product import Product
from Repository.ProductRepository import ProductRepository
from Screens.MainScreen import MainScreen
import keyboard
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

        keyboard.add_hotkey('esc', lambda: MainScreen.start())

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

        if id == '' or name == '' or price == '':
            print('Campos obrigatórios vazios')
            keyboard.wait()
            return

        if isinstance(id, int) is False or isinstance(name, str) is False or isinstance(price, float) is False:
            print('Campos inválidos')
            keyboard.wait()
            return

        product = Product(id, name, price)

        self.repository.create(product)

        print('Produto cadastrado com sucesso')
        self.start()

    def list_products(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Lista de produtos')
        print('--------------------------')
        self.repository.read()
        print()
        keyboard.wait()
        self.start()

    def update_product(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Atualização de produto')
        print('--------------------------')
        print('Lista de produtos')
        print()
        self.repository.read()
        print()
        id = int(input('Digite o id do produto que deseja atualizar: '))

        if isinstance(id, int) is False:
            print('Id inválido')
            keyboard.wait()
            return
        print()

        name = input('Digite o nome do produto: ')
        price = float(input('Digite o preço do produto: '))
        print()

        if id == '' or name == '' or price == '':
            print('Campos obrigatórios vazios')
            keyboard.wait()
            return

        if isinstance(name, str) is False or isinstance(price, float) is False:
            print('Campos inválidos')
            keyboard.wait()
            return

        product = Product(id, name, price)

        self.repository.update(id, product)

        print('Produto atualizado com sucesso')
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
            keyboard.wait()
            return

        self.repository.delete(id)

        print('Produto removido com sucesso')
        self.start()

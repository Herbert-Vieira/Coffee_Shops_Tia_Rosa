"""
Tela de gerenciamento de pedidos.
"""
import os
from datetime import datetime
from Entities.Order import Order
from Entities.OrderItem import OrderItem
from Repositories.OrderRepository import OrderRepository
from Repositories.ProductRepository import ProductRepository
from Repositories.CustomerRepository import CustomerRepository


class OrderScreen:
    """
    Tela de gerenciamento de pedidos.
    """
    def __init__(self):
        self.repository = OrderRepository()
        self.product_repository = ProductRepository()
        self.customer_repository = CustomerRepository()

    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        text = """
        Bem vindo ao gerenciamento de pedidos

        O que deseja fazer?
        1 - Cadastrar pedido
        2 - Listar pedidos
        3 - Atualizar pedido
        4 - Remover pedido
        5 - Voltar
        """

        print(text)

        self.get_options()

    def get_options(self):
        selection = input('Selecione uma opção: ')

        match selection:
            case '1':
                self.create_order()
            case '2':
                self.list_orders()
            case '3':
                self.update_order()
            case '4':
                self.delete_order()
            case '5':
                from Screens.MainScreen import MainScreen
                MainScreen.start()
            case _:
                print('Opção inválida')
                input("Pressione Enter para continuar...")
                self.start()

    def create_order(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Cadastro de pedido')
        print('--------------------------')
        print('Lista de clientes')
        print()
        self.customer_repository.read()
        print()
        customer_id = input('Digite o id do cliente: ')
        customer = self.customer_repository.get_customer_by_id(int(customer_id))
        print()
        print('Lista de produtos')
        print()
        self.product_repository.read()
        print()

        order = Order(
            order_id=0,
            customer=customer,
            moment=datetime.now()
        )

        while True:
            product_id = input('Digite o id do produto: ')
            quantity = input('Digite a quantidade: ')
            print()

            product = self.product_repository.get_product_by_id(int(product_id))
            order_item = OrderItem(
                product=product,
                quantity=int(quantity)
            )

            order.add_order_item(order_item)

            another_item = input('Deseja adicionar outro item? (s/n): ')
            if another_item.lower() == 'n':
                break

        try:
            print(f'Total: {order.total()}')
            self.repository.create(order)
            print('Pedido cadastrado com sucesso!')
            input("Pressione Enter para continuar...")

        except Exception as e:
            print(e)
            input("Pressione Enter para continuar...")

        self.start()

    def list_orders(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Lista de pedidos')
        print('--------------------------')
        self.repository.read_all()
        input("Pressione Enter para continuar...")
        self.start()

    def update_order(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Atualização de pedido')
        print('--------------------------')
        print('Lista de pedidos')
        print()
        self.repository.read_all()
        print()
        order_id = input('Digite o id do pedido que deseja atualizar: ')
        try:
            order = self.repository.get_order_by_id(int(order_id))
            if order is None:
                print('Pedido não encontrado.')
                input("Pressione Enter para continuar...")
                self.start()
                return

            print('\nItens do pedido atual:')
            for item in order.order_itens:
                print(f"- Produto: {item.product.name}, Quantidade: {item.quantity}")

            confirm = input('\nDeseja alterar os produtos deste pedido? (s/n): ')
            if confirm.lower() != 's':
                print('Atualização cancelada.')
                input("Pressione Enter para continuar...")
                self.start()
                return

            order.order_itens.clear()  # Remove os itens antigos

            print('\nLista de produtos:')
            self.product_repository.read()
            print()

            while True:
                product_id = input('Digite o id do produto: ')
                quantity = input('Digite a quantidade: ')
                print()

                product = self.product_repository.get_product_by_id(int(product_id))
                order_item = OrderItem(
                    product=product,
                    quantity=int(quantity)
                )
                order.add_order_item(order_item)

                another_item = input('Deseja adicionar outro item? (s/n): ')
                if another_item.lower() == 'n':
                    break

            print(f'\nTotal atualizado: {order.total()}')
            self.repository.update(order)
            print('Pedido atualizado com sucesso!')
            input("Pressione Enter para continuar...")

        except Exception as e:
            print(f"Erro ao atualizar pedido: {e}")
            input("Pressione Enter para continuar...")

        self.start()

    def delete_order(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Remoção de pedido')
        print('--------------------------')
        print('Lista de pedidos')
        print()
        self.repository.read_all()
        print()
        order_id = input('Digite o id do pedido que deseja remover: ')
        try:
            self.repository.delete(int(order_id))
            print('Pedido removido com sucesso!')
            input("Pressione Enter para continuar...")
        except Exception as e:
            print(e)
            input("Pressione Enter para continuar...")
        self.start()

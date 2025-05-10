"""
Tela de gerenciamento de clientes
"""
import os
from Entities.Customer import Customer
from Repositories.CustomerRepository import CustomerRepository


class CustomerScreen:
    def __init__(self):
        self.repository = CustomerRepository()

    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        text = """
        Bem vindo ao gerenciamento de clientes

        O que deseja fazer?
        1 - Cadastrar cliente
        2 - Listar clientes
        3 - Atualizar cliente
        4 - Remover cliente
        5 - Voltar
        """

        print(text)

        self.get_options()

    def get_options(self):
        """
        Funcao que mostra as opções e Direciona para as telas do sistema.
        """
        selection = input('Selecione uma opção: ')

        match selection:
            case '1':
                self.create_customer()
            case '2':
                self.list_customers()
            case '3':
                self.update_customer()
            case '4':
                self.delete_customer()
            case '5':
                from Screens.MainScreen import MainScreen
                MainScreen.start()
            case _:
                print('Opção inválida')
                input("Pressione Enter para continuar...")
                self.start()

    def create_customer(self):
        """
        Funcao que cria um novo cliente.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Cadastro de cliente')
        print('--------------------------')
        print()
        customer_id = input('Digite o Id do cliente: ')
        name = input('Digite o nome do cliente: ')
        email = input('Digite o email do cliente: ')
        print()
        try:
            customer = Customer(
                int(customer_id),
                name,
                email
            )

            self.repository.create(customer)
            print('Cliente cadastrado com sucesso')
            input("Pressione Enter para continuar...")

        except Exception as e:
            print(e)
            input("Pressione Enter para continuar...")

        self.start()

    def list_customers(self):
        """
        Funcao que lista todos os clientes.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Lista de clientes')
        print('--------------------------')
        print()

        self.repository.read()

        print()
        input("Pressione Enter para continuar...")
        self.start()

    def update_customer(self):
        """
        Funcao que atualiza um cliente.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Atualização de cliente')
        print('--------------------------')
        print('Lista de clientes')
        print()
        self.repository.read()
        print()
        customer_id = input('Digite o id do cliente que deseja atualizar: ')

        name = input('Digite o nome do cliente: ')
        email = input('Digite o email do cliente: ')
        print()

        try:
            customer = Customer(
                int(customer_id),
                name,
                email
            )

            self.repository.update(int(customer_id), customer)

            print('Cliente atualizado com sucesso')
            input("Pressione Enter para continuar...")

        except Exception as e:
            print(e)
            input("Pressione Enter para continuar...")

        self.start()

    def delete_customer(self):
        """
        Funcao que deleta um cliente.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Remoção de cliente')
        print('--------------------------')
        print('Lista de clientes')
        print()
        self.repository.read()
        print()

        try:
            customer_id = int(input('Digite o id do cliente que deseja remover: '))

            self.repository.delete(int(customer_id))

            print('Cliente removido com sucesso')
            input("Pressione Enter para continuar...")

        except Exception as e:
            print(e)
            input("Pressione Enter para continuar...")

        self.start()

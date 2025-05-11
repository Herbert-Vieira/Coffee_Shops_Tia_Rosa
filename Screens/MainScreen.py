"""
Tela principal do sistema.
"""
import os
from Screens.OrderScreen import OrderScreen
from Screens.CustomerScreen import CustomerScreen
from Screens.ProductScreen import ProductScreen


class MainScreen:
    """
    Classe que representa a Tela principal do sistema.
    """
    @staticmethod
    def start() -> None:
        """
        Inicializa a tela principal.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

        text = """
        Bem vindo ao Coffee Shops Tia Rosa

        O que deseja fazer?
        1 - Gerenciar produtos
        2 - Gerenciar clientes
        3 - Gerenciar pedidos
        4 - Sair
        """

        print(text)
        MainScreen.get_options()

    @staticmethod
    def get_options() -> None:
        """
        Funcao que mostra as opcoes e Direciona para as telas do sistema.
        """
        selection = input('Selecione uma opção: ')

        match selection:
            case '1':
                ProductScreen().start()
            case '2':
                CustomerScreen().start()
            case '3':
                OrderScreen().start()
            case '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()
            case _:
                print('Opção inválida')

import os


class MainScreen:
    @staticmethod
    def start():
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
    def get_options():
        selection = input('Selecione uma opção: ')

        match selection:
            case '1':
                self.screen_manager.current = 'product_screen'
            case '2':
                self.screen_manager.current = 'costumer_screen'
            case '3':
                self.screen_manager.current = 'order_screen'
            case '4':
                exit()
            case _:
                print('Opção inválida')

        return selection

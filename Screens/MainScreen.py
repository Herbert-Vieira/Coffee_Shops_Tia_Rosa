class MainScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
    
    def start(self):
        self.screen_manager.current = 'main_screen'

        texto = 'Bem vindo ao Coffee Shops Tia Rosa'
        
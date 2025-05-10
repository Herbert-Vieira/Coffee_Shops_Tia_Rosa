class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.id} | {self.name} | {self.price:.2f}'

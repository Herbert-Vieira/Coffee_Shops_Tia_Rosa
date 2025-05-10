class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.product_id} | {self.name} | {self.price:.2f}'

from Entities.Product import Product


class OrderItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return (
            f'Produto: {self.product.name} | Preço: {self.product.price:.2f} | '
            f'Quantidade: {self.quantity} | Subtotal: {self.sub_total():.2f}'
        )

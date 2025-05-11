"""
Representa um item de pedido em um pedido,
com informações sobre o produto e quantidade.

Esta classe gerencia operações relacionadas aos itens de pedido.

Atributos:
    product (Product): O produto associado ao item de pedido.
    quantity (int): A quantidade do produto no item de pedido.
"""

from Entities.Product import Product


class OrderItem:
    """
    Inicializa um novo objeto OrderItem.

    Args:
        product (Product): O produto associado ao item de pedido.
        quantity (int): A quantidade do produto no item de pedido.
    """
    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity

    def sub_total(self) -> float:
        """Calcula o subtotal do item de pedido."""
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return (
            f'Produto: {self.product.name} | Preço: {self.product.price:.2f} | '
            f'Quantidade: {self.quantity} | Subtotal: {self.sub_total():.2f}'
        )

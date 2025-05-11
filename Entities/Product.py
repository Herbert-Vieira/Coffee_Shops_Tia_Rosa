"""
Representa um produto no sistema, com nome e preço.

Esta classe gerencia operações relacionadas aos produtos.

Atributos:
    product_id (int): Identificador único para o produto.
    name (str): Nome do produto.
    price (float): Preço do produto.
"""


class Product:
    """
    Inicializa um novo objeto Product.

    Args:
        product_id (int): Identificador único para o produto.
        name (str): Nome do produto.
        price (float): Preço do produto.
    """
    def __init__(self, product_id: int, name: str, price: float) -> None:
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.product_id} | {self.name} | {self.price:.2f}'

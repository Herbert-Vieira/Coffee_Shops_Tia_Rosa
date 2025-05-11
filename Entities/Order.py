"""
Representa um pedido no sistema, com detalhes do pedido,
informações do cliente, e itens de pedido associados.

Esta classe gerencia operações relacionadas a pedidos,
como adicionar/remover itens de pedido e calcular o valor total.

Atributos:
    order_id (int): Identificador único para o pedido.
    customer (Customer): O cliente que fez o pedido.
    moment (datetime): Timestamp de quando o pedido foi criado.
    order_itens (list[OrderItem]): Lista de itens no pedido.
"""

from datetime import datetime
from Entities.OrderItem import OrderItem
from Entities.Customer import Customer


class Order:
    """
    Inicializa um novo objeto Order.

    Args:
        order_id (int): Identificador único para o pedido.
        customer (Customer): O cliente que fez o pedido.
        moment (datetime): Timestamp de quando o pedido foi criado.
    """
    def __init__(
        self,
        order_id: int,
        customer: Customer,
        moment: datetime
    ) -> None:
        self.order_id = order_id
        self.customer = customer
        self.moment = moment
        self.order_itens: list[OrderItem] = []

    def add_order_item(self, order_item: OrderItem) -> None:
        """
        Adiciona um item de pedido ao pedido.
        """
        self.order_itens.append(order_item)

    def remove_order_item(self, order_item: OrderItem) -> None:
        """
        Remove um item de pedido do pedido.
        """
        self.order_itens.remove(order_item)

    def total(self) -> float:
        """
        Calcula o valor total do pedido.
        """
        total = 0
        for order_item in self.order_itens:
            total += order_item.sub_total()
        return total

    def __str__(self) -> str:
        itens_str = '\n\t'.join(str(item) for item in self.order_itens)
        return (
            f'Ordem: {self.order_id}, Cliente: {self.customer.name}, '
            f'Momento: {self.moment}, Total: {self.total():.2f}\n'
            f'Itens:\n\t{itens_str}'
            f'\n{"-" * 90}'
        )

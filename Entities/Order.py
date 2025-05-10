from OrderItem import OrderItem
from Entities.Customer import Customer
from datetime import datetime


class Order:
    def __init__(
        self,
        order_id: int,
        customer: Customer,
        moment: datetime
    ):
        self.order_id = order_id
        self.customer = customer
        self.moment = moment
        self.order_itens: list[OrderItem] = []

    def add_order_item(self, order_item: OrderItem):
        self.order_itens.append(order_item)

    def remove_order_item(self, order_item: OrderItem):
        self.order_itens.remove(order_item)

    def total(self):
        total = 0
        for order_item in self.order_itens:
            total += order_item.sub_total()
        return total

    def __str__(self):
        return (
            f'Order: {self.order_id}, Client: {self.customer.name}, '
            f'Moment: {self.moment}, Total: {self.total()}'
        )

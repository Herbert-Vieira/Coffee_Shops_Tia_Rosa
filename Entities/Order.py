from Client import Client
from OrderItem import OrderItem
from datetime import datetime

class Order:
    def __init__(
        self,
        order_id: int,
        client: Client,
        moment: datetime
    ):
        self.order_id = order_id
        self.client = client
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
        return f'Order: {self.order_id}, Client: {self.client.name}, Moment: {self.moment}, Total: {self.total()}'
        
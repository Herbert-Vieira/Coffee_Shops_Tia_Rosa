"""
Esta classe gerencia o acesso aos dados dos pedidos.

Atributos:
    repository: (str) Caminho para o arquivo de dados dos pedidos.
"""
from datetime import datetime
import json
from Entities.Order import Order
from Entities.OrderItem import OrderItem
from Entities.Customer import Customer
from Entities.Product import Product


class OrderRepository:
    """
    Repositorio de Pedidos
    Cadastra, atualiza, deleta e lista pedidos a partir de um arquivo .json
    """
    def __init__(self):
        self.repository = 'src/Database/orders.json'

    def create(self, order: Order) -> None:
        """
        Cria um novo pedido
        """
        try:
            with open(self.repository, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        last_id = 0
        for o in data:
            if o['order_id'] > last_id:
                last_id = o['order_id']

        order.order_id = last_id + 1

        data.append(
            {
                'order_id': order.order_id,
                'customer': order.customer.__dict__,
                'moment': order.moment.strftime('%d/%m/%Y %H:%M:%S'),
                'order_itens': [
                    {
                        'product': item.product.__dict__,
                        'quantity': item.quantity
                    }
                    for item in order.order_itens
                ]
            }
        )
        with open(self.repository, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def read_all(self) -> None:
        """
        Lista todos os pedidos
        """
        with open(self.repository, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            order_id = item['order_id']
            customer = Customer(
                item['customer']['customer_id'],
                item['customer']['name'],
                item['customer']['email']
            )
            order_itens = [
                OrderItem(
                    Product(
                        item['order_itens'][i]['product']['product_id'],
                        item['order_itens'][i]['product']['name'],
                        item['order_itens'][i]['product']['price']
                    ),
                    item['order_itens'][i]['quantity']
                )
                for i in range(len(item['order_itens']))
            ]
            moment = datetime.strptime(
                item['moment'], '%d/%m/%Y %H:%M:%S'
            )
            order = Order(order_id, customer, moment)
            for order_item in order_itens:
                order.add_order_item(order_item)
            print(order)
            print()

    def get_order_by_id(self, order_id: int) -> Order:
        with open(self.repository, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            if item['order_id'] == order_id:
                customer = Customer(
                    item['customer']['customer_id'],
                    item['customer']['name'],
                    item['customer']['email']
                )
                order_itens = [
                    OrderItem(
                        Product(
                            item['order_itens'][i]['product']['product_id'],
                            item['order_itens'][i]['product']['name'],
                            item['order_itens'][i]['product']['price']
                        ),
                        item['order_itens'][i]['quantity']
                    )
                    for i in range(len(item['order_itens']))
                ]
                moment = datetime.strptime(
                    item['moment'], '%d/%m/%Y %H:%M:%S'
                )
                order = Order(
                    order_id,
                    customer,
                    moment
                )
                for item in order_itens:
                    order.add_order_item(item)
                return order

        raise ValueError(f'Pedido com id {order_id} não encontrado.')

    def update(self, order: Order) -> None:
        """
        Atualiza um pedido
        """
        with open(self.repository, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for idx, item in enumerate(data):
            if item['order_id'] == order.order_id:
                data[idx] = {
                    'order_id': order.order_id,
                    'customer': order.customer.__dict__,
                    'moment': order.moment.strftime('%d/%m/%Y %H:%M:%S'),
                    'order_itens': [
                        {
                            'product': item.product.__dict__,
                            'quantity': item.quantity
                        }
                        for item in order.order_itens
                    ]
                }
                break

        with open(self.repository, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def delete(self, order_id: int) -> None:
        """
        Deleta um pedido pelo id
        """
        with open(self.repository, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for idx, item in enumerate(data):
            if item['order_id'] == order_id:
                data.pop(idx)
                break

        with open(self.repository, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

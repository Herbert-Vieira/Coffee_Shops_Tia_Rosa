"""
Esta classe gerencia o acesso aos dados dos clientes.

Atributos:
    repository: (str) Caminho para o arquivo de dados dos clientes.
"""

import json
from Entities.Customer import Customer


class CustomerRepository:
    """
    Repositorio de clientes
    cadastra, atualiza, deleta e lista clientes a partir de um arquivo .json
    """
    def __init__(self) -> None:
        self.repository = 'src/Database/costumers.json'

    def create(self, costumer: Customer) -> None:
        """
        Cria um novo cliente
        """
        try:
            with open(self.repository, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        last_id = 0
        for c in data:
            if c['id'] > last_id:
                last_id = c['id']

        costumer.customer_id = last_id + 1

        data.append({
            'id': costumer.customer_id,
            'name': costumer.name,
            'email': costumer.email
        })

        with open(self.repository, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def read_all(self) -> None:
        """
        Lista todos os clientes
        """
        with open(self.repository, 'r', encoding='utf-8') as f:
            data = json.load(f)

            for c in data:
                costumer = Customer(
                    int(c['id']),
                    c['name'],
                    c['email'],
                )
                print(costumer)

    def get_customer_by_id(self, customer_id: int) -> Customer:
        """
        Retorna um cliente pelo id
        """
        with open(self.repository, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for c in data:
            if c['id'] == customer_id:
                customer = Customer(
                    int(c['id']),
                    c['name'],
                    c['email'],
                )
                return customer

        raise ValueError(f"Cliente com Id {customer_id} não encontrado")

    def update(self, customer_id: int, customer: Customer) -> None:
        """
        Atualiza um cliente pelo id
        """
        with open(self.repository, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for idx, c in enumerate(data):
            if c['id'] == customer_id:
                data[idx] = {
                    'id': customer.customer_id,
                    'name': customer.name,
                    'email': customer.email
                }
                break

        with open(self.repository, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def delete(self, customer_id: int) -> None:
        """
        Deleta um cliente pelo id
        """
        with open(self.repository, 'r', encoding='utf-8') as f:
            data = json.load(f)

        data = [c for c in data if c['id'] != customer_id]

        with open(self.repository, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

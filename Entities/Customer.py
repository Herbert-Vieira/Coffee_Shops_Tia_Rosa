"""
Entidade do cliente
"""


class Customer:
    """
    Classe que representa um cliente

    Atributos:
        name: str
        email: str
    """
    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self):
        return f'{self.customer_id} | {self.name} | {self.email}'

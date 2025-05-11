"""
Representa um cliente no sistema, com nome e email.

Esta classe gerencia operações relacionadas a clientes.

Atributos:
    customer_id (int): Identificador único para o cliente.
    name (str): Nome do cliente.
    email (str): Email do cliente.
"""


class Customer:
    """
    Inicializa um objeto cliente

    Atributos:
        customer_id: int
        name: str
        email: str
    """
    def __init__(self, customer_id: int, name: str, email: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f'{self.customer_id} | {self.name} | {self.email}'

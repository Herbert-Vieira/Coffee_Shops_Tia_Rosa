"""
Repositorio de clientes
cadastra, atualiza, deleta e lista clientes a partir de um arquivo .json
"""

import os
import json
from Entities.Customer import Customer


class CustomerRepository:
    """
    Repositorio de clientes
    cadastra, atualiza, deleta e lista clientes a partir de um arquivo .json
    """
    def __init__(self):
        self.file = 'src/Database/costumers.json'

    def create(self, costumer: Customer):
        """
        Cria um novo cliente
        """
        # Carrega os dados existentes
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []  # Se o arquivo não existir, cria uma lista vazia

        # Verifica se o ID já existe
        for c in data:
            if c['id'] == costumer.customer_id:
                os.system('cls' if os.name == 'nt' else 'clear')
                raise ValueError('Erro: ID já existe')

        # Adiciona o novo cliente
        data.append({
            'id': costumer.customer_id,
            'name': costumer.name,
            'email': costumer.email
        })

        # Salva os dados atualizados de volta no arquivo
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def read(self):
        """
        Lista todos os clientes
        """
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)

            for c in data:
                costumer = Customer(
                    int(c['id']),
                    c['name'],
                    c['email'],
                )
                print(costumer)

    def update(self, customer_id: int, customer: Customer):
        """
        Atualiza um cliente
        """
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Atualiza o cliente com o id especificado
        for idx, c in enumerate(data):
            if c['id'] == customer_id:
                data[idx] = {
                    'id': customer.customer_id,
                    'name': customer.name,
                    'email': customer.email
                }
                break

        # Salva os dados atualizados de volta no arquivo
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def delete(self, customer_id: int):
        """
        Deleta um cliente
        """
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Remove o cliente com o id especificado
        data = [c for c in data if c['id'] != customer_id]

        # Salva os dados atualizados de volta no arquivo
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

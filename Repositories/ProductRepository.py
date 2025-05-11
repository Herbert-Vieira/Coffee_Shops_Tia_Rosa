import os
import json
from Entities.Product import Product


class ProductRepository:
    def __init__(self):
        self.file = 'src/Database/products.json'

    def create(self, product: Product):
        # Carrega os dados existentes
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []  # Se o arquivo não existir, cria uma lista vazia

        # Verifica o último ID cadastrado
        last_id = 0
        for p in data:
            if p['id'] > last_id:
                last_id = p['id']

        product.product_id = last_id + 1

        # Adiciona o novo produto
        data.append({
            'id': product.product_id,
            'name': product.name,
            'price': product.price
        })

        # Salva os dados atualizados de volta no arquivo
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def read(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)

            for p in data:
                product = Product(
                    int(p['id']),
                    p['name'],
                    float(p['price']),
                )
                print(product)

    def get_product_by_id(self, product_id: int) ->  Product:
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for p in data:
            if p['id'] == product_id:
                product = Product(
                    int(p['id']),
                    p['name'],
                    float(p['price']),
                )
                return product

    def update(self, product_id: int, product: Product):
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Atualiza o produto com o id especificado
        for idx, p in enumerate(data):
            if p['id'] == product_id:
                data[idx] = {
                    'id': product.product_id,
                    'name': product.name,
                    'price': product.price
                }
                break

        # Salva os dados atualizados de volta no arquivo
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def delete(self, product_id: int):
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Remove o produto com o id especificado
        for idx, p in enumerate(data):
            if p['id'] == product_id:
                data.pop(idx)
                break

        # Salva os dados atualizados de volta no arquivo
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

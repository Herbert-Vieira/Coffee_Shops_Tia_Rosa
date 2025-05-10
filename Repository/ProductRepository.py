from Entities.Product import Product
import json
import os


class ProductRepository:
    def __init__(self):
        self.file = 'src/Database/products.json'

    def create(self, product: Product):
        # Carrega os dados existentes
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []  # Se o arquivo não existir, cria uma lista vazia

        # Verifica se o ID já existe
        for p in data:
            if p['id'] == product.id:
                os.system('cls' if os.name == 'nt' else 'clear')
                raise Exception('Erro: ID já existe')

        # Adiciona o novo produto
        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price
        })

        # Salva os dados atualizados de volta no arquivo
        with open(self.file, 'w') as f:
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

    def update(self, id: int, product: Product):
        with open(self.file, 'r') as f:
            data = json.load(f)

        # Atualiza o produto com o id especificado
        for idx, p in enumerate(data):
            if p['id'] == id:
                data[idx] = {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price
                }
                break

        # Salva os dados atualizados de volta no arquivo
        with open(self.file, 'w') as f:
            json.dump(data, f, indent=4)

    def delete(self, id: int):
        with open(self.file, 'r') as f:
            data = json.load(f)

        # Remove o produto com o id especificado
        data = [p for p in data if p['id'] != id]

        # Salva os dados atualizados de volta no arquivo
        with open(self.file, 'w') as f:
            json.dump(data, f, indent=4)

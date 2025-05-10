from Entities.Product import Product
import json


class ProductRepository:
    def __init__(self):
        self.file = 'src/Database/products.json'

    def create(self, product: Product):
        with open(self.file, 'w') as f:
            json.dump(product, f, indent=4)

    def read(self):
        with open(self.file, 'r') as f:
            data = json.load(f)

            for key, value in data.items():
                print(key, value)

    def update(self, id: int, product: Product):
        with open(self.file, 'w') as f:
            data = json.load(f)
            data[id] = product

    def delete(self, id: int):
        with open(self.file, 'w') as f:
            data = json.load(f)
            data.pop(id)

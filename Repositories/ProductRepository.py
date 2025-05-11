"""
Esta classe gerencia o acesso aos dados dos produtos.

Atributos:
    repository: (str) Caminho para o arquivo de dados dos produtos.
"""
import json
from Entities.Product import Product


class ProductRepository:
    """
    Repositorio de produtos
    Cadastra, atualiza, deleta e lista produtos a partir de um arquivo .json
    """
    def __init__(self):
        self.file = 'src/Database/products.json'

    def create(self, product: Product) -> None:
        """
        Cria um novo produto
        """
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        last_id = 0
        for p in data:
            if p['id'] > last_id:
                last_id = p['id']

        product.product_id = last_id + 1

        data.append({
            'id': product.product_id,
            'name': product.name,
            'price': product.price
        })

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def read(self) -> None:
        """
        Lista todos os produtos
        """
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)

            for p in data:
                product = Product(
                    int(p['id']),
                    p['name'],
                    float(p['price']),
                )
                print(product)

    def get_product_by_id(self, product_id: int) -> Product:
        """
        Retorna um produto pelo id
        """
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
        raise ValueError(f'Produto com id {product_id} não encontrado.')

    def update(self, product_id: int, product: Product) -> None:
        """
        Atualiza um produto pelo id
        """
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for idx, p in enumerate(data):
            if p['id'] == product_id:
                data[idx] = {
                    'id': product.product_id,
                    'name': product.name,
                    'price': product.price
                }
                break

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def delete(self, product_id: int) -> None:
        """
        Deleta um produto pelo id
        """
        with open(self.file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for idx, p in enumerate(data):
            if p['id'] == product_id:
                data.pop(idx)
                break

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

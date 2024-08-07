import json

from src.category import Category
from src.product import Product


def get_products_of_json(file: str) -> list:
    """
    Считывание данных из json-файла по переданному пути и конвертация их в экземпляры классов
    """

    with open(f"../data/{file}", encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories

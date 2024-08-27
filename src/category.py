from typing import Any

from src.product import Product


class Category:
    """
    Класс категорий продуктов интернет магазина
    """

    name: str
    description: str
    __products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """
        Конструктор объектов
        """
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """
        Формирует отображение информации об объекте класса для пользователей
        """
        all_products_quantity = sum(product.quantity for product in self.products_list)
        return f"{self.name}, количество продуктов: {all_products_quantity} шт."

    @property
    def products(self) -> str:
        result = ""
        for el in self.__products:
            result += f"{el.name}, {el.price} руб. Остаток: {el.quantity} шт.\n"
        return result

    @property
    def products_list(self) -> list:
        """
        Геттер атрибута __products - вовзращает список продуктов в виде списка
        """
        return self.__products

    def add_product(self, new_product: Product) -> None:
        """
        Добавляем новый продукт в список продуктов
        """
        self.__products.append(new_product)
        Category.category_count += 1

    def middle_price(self) -> Any:
        """
        подсчитывает средний ценник всех товаров
        """

        try:
            result = round(sum([el.price for el in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            result = 0
        return result

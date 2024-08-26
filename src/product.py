from abc import ABC, abstractmethod
from typing import Any

from src.mixin_log import MixinLog


class BaseProduct(ABC):
    """
    Абстрактный класс для всех продуктов
    """

    @classmethod
    @abstractmethod
    def new_product(cls, *args: list, **kwargs: dict) -> None:
        """
        Создает новый продукт
        """
        pass


class Product(BaseProduct, MixinLog):
    """
    Класс продуктов интернет магазина
    """

    name: str
    description: str
    __price: float
    quantity: int
    products_list: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Конструктор объектов
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products_list.append(self)
        super().__init__()

    def __str__(self) -> str:
        """
        Формирует отображение информации об объекте класса для пользователей
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Возвращает полную стоимость всех товаров на складе для складываемых объектов
        """
        if type(other) is Product:
            return self.quantity * self.price + other.quantity * other.price

        raise TypeError("Можно складывать товары только одного класса")

    @classmethod
    def new_product(cls, product: dict) -> Any:
        for prod in cls.products_list:
            if prod.name == product["name"]:
                prod.price = max(prod.price, product["price"])
                prod.quantity += product["quantity"]
                return prod
            else:
                new_prod = cls(product["name"], product["description"], product["price"], product["quantity"])
                return new_prod

    @property
    def price(self) -> float:
        """
        Геттер атрибута __price - возвращает цену продукта
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер атрибута __price - обновляет цену продукта, если новая цена ниже старой запрашивается подтверждение
        """
        if new_price > 0:
            if new_price < self.__price:
                if input("Вы уверены, что хотите снизить цену? Введите 'y' - если да, 'n' - если нет: ") == "y":
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Smartphone") -> float:  # type: ignore[override]
        """
        Возвращает полную стоимость всех товаров на складе для складываемых объектов
        """
        if type(other) is Smartphone:
            return self.quantity * self.price + other.quantity * other.price

        raise TypeError("Можно складывать товары только одного класса")


class LawnGrass(Product):

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: str,
            color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "LawnGrass") -> float:  # type: ignore[override]
        """
        Возвращает полную стоимость всех товаров на складе для складываемых объектов
        """
        if type(other) is LawnGrass:
            return self.quantity * self.price + other.quantity * other.price

        raise TypeError("Можно складывать товары только одного класса")

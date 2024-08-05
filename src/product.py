class Product:
    """
    Класс продуктов интернет магазина
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Конструктор объектов
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

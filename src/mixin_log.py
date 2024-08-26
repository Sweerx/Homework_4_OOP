class MixinLog:
    """
    Миксин для вывода в консоль информации о том, от какого класса и с какими параметрами был создан объект.
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self) -> None:
        """
        Конструктор объектов
        """
        print(repr(self))

    def __repr__(self) -> str:
        """
        Формирует строковое представление объекта в режиме отладки
        """
        return f"{self.__class__.__name__}({self.name}, {self.description}," f" {self.price}, {self.quantity})"

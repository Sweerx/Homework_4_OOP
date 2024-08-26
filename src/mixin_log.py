class MixinLog:
    """
    Миксин для вывода в консоль информацию о том, от какого класса и с какими параметрами был создан объекта.
    """
    def __init__(self) -> None:
        """
        Конструктор объектов
        """
        print(repr(self))

    def __repr__(self) -> str:
        """
        Формирует строковое представление объекта в режиме отладки
        """
        return (f"{self.__class__.__name__}({self.name}, {self.description},"  # type: ignore[attr-defined]
                f" {self.price}, {self.quantity})")  # type: ignore[attr-defined]

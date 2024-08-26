from typing import Any

from src.product import LawnGrass, Product, Smartphone


def test_print_mixin_product(capsys: Any, first_product: Product) -> None:
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Iphone 15, Apple Iphone 15, 1500, 10)"


def test_print_mixin_smartphone(capsys: Any, first_smartphone_prod: Smartphone) -> None:
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"


def test_print_mixin_lawn_grass(capsys: Any, first_lawn_grass_prod: LawnGrass) -> None:
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"

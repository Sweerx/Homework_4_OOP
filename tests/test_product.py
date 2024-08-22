from typing import Any
from unittest.mock import patch

import pytest

from src.product import LawnGrass, Product, Smartphone


def test_product_init(first_product: Product) -> None:
    assert first_product.name == "Iphone 15"
    assert first_product.description == "Apple Iphone 15"
    assert first_product.price == 1500
    assert first_product.quantity == 10


def test_product_new_product_duplication(first_product: Product, new_prod_dupl: dict) -> None:
    second_prod = Product.new_product(new_prod_dupl)
    assert second_prod.price == 1500
    assert second_prod.quantity == 35


def test_product_new_product(first_product: Product, new_prod: dict) -> None:
    second_prod = Product.new_product(new_prod)
    assert second_prod.price == 800
    assert second_prod.quantity == 10


def test_product_price(first_product: Product, capsys: Any) -> None:
    assert first_product.price == 1500
    first_product.price = 1700
    assert first_product.price == 1700
    first_product.price = 0
    capture = capsys.readouterr()
    assert capture.out == "Цена не должна быть нулевая или отрицательная\n"
    assert first_product.price == 1700
    first_product.price = -100
    capture = capsys.readouterr()
    assert capture.out == "Цена не должна быть нулевая или отрицательная\n"
    assert first_product.price == 1700

    with patch("builtins.input") as mock_input:
        mock_input.return_value = "y"
        first_product.price = 1300
        assert first_product.price == 1300

    with patch("builtins.input") as mock_input:
        mock_input.return_value = "n"
        first_product.price = 1000
        assert first_product.price == 1300


def test_product_str(first_product: Product) -> None:
    assert str(first_product) == "Iphone 15, 1500 руб. Остаток: 10 шт."


def test_product_add(first_product: Product, second_product: Product) -> None:
    assert first_product + second_product == 33_000


def test_smartphone_init(first_smartphone_prod: Smartphone) -> None:
    assert first_smartphone_prod.name == "Samsung Galaxy S23 Ultra"
    assert first_smartphone_prod.description == "256GB, Серый цвет, 200MP камера"
    assert first_smartphone_prod.price == 180000.0
    assert first_smartphone_prod.quantity == 5
    assert first_smartphone_prod.efficiency == 95.5
    assert first_smartphone_prod.model == "S23 Ultra"
    assert first_smartphone_prod.memory == 256
    assert first_smartphone_prod.color == "Серый"


def test_smartphone_add(first_smartphone_prod: Smartphone, second_smartphone_prod: Smartphone) -> None:
    assert first_smartphone_prod + second_smartphone_prod == 2_580_000.0


def test_smartphone_add_error(first_smartphone_prod: Smartphone) -> None:
    with pytest.raises(TypeError):
        first_smartphone_prod + 1  # type: ignore


def test_lawn_grass_init(first_lawn_grass_prod: LawnGrass) -> None:
    assert first_lawn_grass_prod.name == "Газонная трава"
    assert first_lawn_grass_prod.description == "Элитная трава для газона"
    assert first_lawn_grass_prod.price == 500.0
    assert first_lawn_grass_prod.quantity == 20
    assert first_lawn_grass_prod.country == "Россия"
    assert first_lawn_grass_prod.germination_period == "7 дней"
    assert first_lawn_grass_prod.color == "Зеленый"


def test_lawn_grass_add(first_lawn_grass_prod: LawnGrass, second_lawn_grass_prod: LawnGrass) -> None:
    assert first_lawn_grass_prod + second_lawn_grass_prod == 16_750.0


def test_lawn_grass_add_error(first_lawn_grass_prod: LawnGrass) -> None:
    with pytest.raises(TypeError):
        first_lawn_grass_prod + 1  # type: ignore

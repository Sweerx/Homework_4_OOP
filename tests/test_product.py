from src.product import Product


def test_initialization(product: Product) -> None:
    assert product.name == "Ноутбук"
    assert product.description == "Высокопроизводительный ноутбук"
    assert product.price == 1500.0
    assert product.quantity == 10


def test_price_update(product: Product) -> None:
    product.price = 1400.0
    assert product.price == 1400.0


def test_quantity_update(product: Product) -> None:
    product.quantity = 5
    assert product.quantity == 5


def test_description_update(product: Product) -> None:
    product.description = "Ноутбук средней ценовой категории"
    assert product.description == "Ноутбук средней ценовой категории"

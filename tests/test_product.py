from src.product import Product


def test_product_init(first_product: Product) -> None:
    assert first_product.name == "Iphone 15"
    assert first_product.description == "Apple Iphone 15"
    assert first_product.price == 1500
    assert first_product.quantity == 10
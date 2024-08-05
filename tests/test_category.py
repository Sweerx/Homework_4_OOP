from src.category import Category


def test_category_init(first_cat: Category, second_cat: Category) -> None:
    assert first_cat.name == "Apple"
    assert first_cat.description == "Смартфоны  компании Apple"
    assert len(first_cat.products) == 2
    assert Category.category_count == 2
    assert Category.product_count == 4

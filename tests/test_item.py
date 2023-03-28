"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone

import pytest


@pytest.fixture
def item():
    return Item('test', 8000, 2)

def test_item_init(item):
    """
    Тест класса
    """
    assert type(item.name) == str
    assert type(item.price) == int
    assert type(item.quantity) == int

def test_repr(item):
    assert repr(item) == "Item('test', 8000, 2)"

def test_str(item):
    assert str(item) == 'test'

def test_item_init_2(item):
    """
    Тест значений класса
    """
    assert item.name == 'test'
    assert item.price == 8000
    assert item.quantity == 2

def test_calculate_total_price(item):
    """
    Тест общей стоимости конкретного товара в магазине
    """
    assert item.calculate_total_price() == 16000

def test_apply_discount(item):
    """
    Тест применения установленной скидки для конкретного товара
    """
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 4000

def test_name_1(item):
    """
    Тест функции name
    """
    item.name = "test"
    assert item.name == "test"

def test_name_3(item):
    """
    Тест функции name
    """
    with pytest.raises(ValueError, match="Длина наименования товара превышает 10 символов."):
        item.name = "test_for_ten_symbols"

def test_string_to_number(item):
    """
    Тест статического метода
    """
    assert item.string_to_number("5.0") == 5

def test_instantiate_from_csv():
    """
    Тест класс-метода, инициализирующего экземпляры класса
    """
    Item.instantiate_from_csv(csv_path='./tests/items.csv')
    assert type(Item.all) is not None

def test_instantiate_from_csv_2():
    """
    Тест класс-метода, инициализирующего экземпляры класса
    """
    Item.instantiate_from_csv(csv_path='/tests/items.csv')
    with pytest.raises(FileNotFoundError):
        raise FileNotFoundError("Отсутствует файл item.csv")

def test_instantiate_from_csv_3():
    """
    Тест класс-метода, инициализирующего экземпляры класса
    """
    Item.instantiate_from_csv(csv_path='./tests/items.csv')
    with pytest.raises(FileNotFoundError):
        raise FileNotFoundError("Отсутствует файл item.csv")


def test__add__(item):
    """
    Тест функции проверки допустимости операции
    """
    with pytest.raises(ValueError, match="Складывать можно только объекты Item и дочерние от них."):
        Item.__add__(item, Phone)

def test__add__2(item):
    """
    Тест функции проверки допустимости операции
    """
    item1 = Item('test', 8000, 10)
    item2 = Item('test2', 4000, 10)
    assert item1 + item2 == 20
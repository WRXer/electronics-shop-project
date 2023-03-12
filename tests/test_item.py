"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

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

#def test_name_2(item):
    #"""
    #Тест функции name
    #"""
    #item.name = "test_for_ten_symbols"
    #assert item.name != "test_for_ten_symbols"

def test_name_3(item):
    """
    Тест функции name
    """
    item.name = "test_for_ten_symbols"
    with pytest.raises(ValueError, match="Длина наименования товара превышает 10 символов."):
        item.name()

def test_string_to_number(item):
    """
    Тест статического метода
    """
    assert item.string_to_number("5.0") == 5


from src.phone import Phone
from src.item import Item

import pytest


@pytest.fixture
def phone():
    return Phone('test', 8000, 20, 2)

def test_phone_init(phone):
    """
    Тест класса
    """
    assert type(phone.name) == str
    assert type(phone.price) == int
    assert type(phone.quantity) == int
    assert type(phone.number_of_sim) == int

def test_item_init_2(phone):
    """
    Тест значений класса
    """
    assert phone.name == 'test'
    assert phone.price == 8000
    assert phone.quantity == 20
    assert phone.number_of_sim == 2

def test_repr(phone):
    assert repr(phone) == "Phone('test', 8000, 20, 2)"

def test_number_of_sim_1(phone):
    """
    Тест функции number_of_sim
    """
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2

def test_number_of_sim_3(phone):
    """
    Тест функции number_of_sim
    """
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        phone.number_of_sim = 0

def test__add__(phone):
    """
    Тест функции проверки допустимости операции
    """
    with pytest.raises(ValueError, match="Складывать можно только объекты Phone."):
        Phone.__add__(Item, Phone)

def test__add__2(phone):
    """
    Тест функции проверки допустимости операции
    """
    phone1 = Phone('test', 8000, 20, 2)
    phone2 = Phone('test2', 4000, 10, 2)
    assert phone1 + phone2 == 30
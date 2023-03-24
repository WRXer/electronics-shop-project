from src.keyboard import Keyboard
from src.item import Item

import pytest


@pytest.fixture
def kb():
    return Keyboard('test', 8000, 20)

def test_keyboard_init(kb):
    """
    Тест класса
    """
    assert type(kb.name) == str
    assert type(kb.price) == int
    assert type(kb.quantity) == int

def test_str(kb):
    assert str(kb) == 'test'

from src.keyboard import MixinKeyBoard
from src.keyboard import Keyboard

import pytest


@pytest.fixture
def kb():
    return Keyboard('test', 8000, 20)

def test_mixin_init(kb):
    assert kb.language == "EN"

def test_language(kb):
    """
    Тест функции language
    """
    kb.language = "RU"
    assert kb.language == "RU"

def test_language_2(kb):
    """
    Тест функции language
    """
    with pytest.raises(AttributeError, match="property 'language' of 'KeyBoard' object has no setter"):
        kb.language = "CH"

def test_change_lang(kb):
    """
    Тест функции смены языка
    """
    kb.change_lang()
    assert kb.language == "RU"

def test_change_lang_2(kb):
    """
    Тест функции смены языка
    """
    kb.change_lang().change_lang()
    assert kb.language == "EN"
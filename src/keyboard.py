from src.item import Item
from src.MixinKeyBoard import MixinKeyBoard


class Keyboard(Item, MixinKeyBoard):
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.language = language

    def __str__(self):
        return f"{self.name}"

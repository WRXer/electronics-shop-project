import csv
from src.instantiate_csv_error import InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        """
        Функция магического метода отображения информации об объекте класса в режиме отладки
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Функция магического метода отображения информации об объекте класса для пользователей
        """
        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = int(self.price * self.pay_rate)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise ValueError("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls, csv_path="../src/items.csv"):
        """
        класс-метод, инициализирующий экземпляры класса
        """
        try:
            with open(csv_path, 'r', newline='') as csvfile:
                file = csv.reader(csvfile, delimiter=',')
                for i in file:
                    if len(i) == 3:
                        cls.all.append(i)
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
             print("Отсутствует файл item.csv")


    @staticmethod
    def string_to_number(quantity):
        """
        статический метод, возвращающий число из числа-строки
        """
        try:
            return int(quantity)
        except ValueError:
            return int(quantity[0: quantity.find('.')])

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

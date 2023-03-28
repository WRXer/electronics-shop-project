class InstantiateCSVError(Exception):
    """
    Исключение, выбрасываемое при ошибке чтения CSV-файла.
    """
    def __init__(self, *args):
        self.message = args[0] if args else 'Файл item.csv поврежден'
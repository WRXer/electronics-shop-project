class MixinKeyBoard:
    def __init__(self):
        self.__language = None

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, select_language):
        if select_language == "RU" or select_language == "EN":
            self.__language = select_language
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

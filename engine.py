import dictinary
import pyperclip
import pyautogui


class Convertator:
    __DICTIONARY = dictinary.en_ru

    def __init__(self, dict='en-ru'):
        self.__string = ''
        if dict == 'en-ru':
            Convertator.__DICTIONARY = dictinary.en_ru
        else:
            raise ValueError(f'Словаря {dict} не существует!')

    def activate_convert(self):
        pyautogui.hotkey('command', 'c')
        self.__string = pyperclip.paste()
        converted = self.convert(self.__string)
        pyperclip.copy(converted)
        pyautogui.hotkey('command', 'v')

    @staticmethod
    def convert(text):
        converted = ""
        for letter in range(len(text)):
            if text[letter].lower() in Convertator.__DICTIONARY:
                if text[letter].lower() == ',' and text[letter + 1] == ' ':
                    converted += text[letter]
                elif text[letter].lower() == ',' and text[letter + 1] != ' ':
                    converted += Convertator.__DICTIONARY[text[letter].lower()]
                else:
                    converted += Convertator.__DICTIONARY[text[letter].lower()]
            else:
                converted += text[letter]

        return converted

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, text: str):
        converted = self.convert(text)
        self.__string = converted

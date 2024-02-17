import dictinary
import pyperclip
import pyautogui
import pymorphy2


class Convertator:
    __DICTIONARY = dictinary.en_ru
    __THRESHOLD = 0.75

    def __init__(self, dict='en-ru', string=""):
        self.__string = string
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
            if text[letter] in Convertator.__DICTIONARY:
                try:
                    if text[letter] in ',.' and text[letter + 1] == ' ':
                        converted += text[letter]
                    # elif f"{text[letter]}{text[letter + 1]}{text[letter + 2]}" == '...':
                    #     raise ValueError
                    # elif f"{text[letter]}{text[letter + 1]}" == '..':
                    #     raise ValueError
                    else:
                        converted += Convertator.__DICTIONARY[text[letter]]
                except IndexError:
                    converted += text[letter]
            else:
                converted += text[letter]

        return converted

    @staticmethod
    def is_space(letter_1, letter_2):
        if letter_1 in (".", ",") and letter_2 == " ":
            return True
        else:
            return False

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, text: str):
        converted = self.convert(text)
        self.__string = converted

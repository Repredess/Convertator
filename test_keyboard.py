import keyboard


class KeyboardTest:

    def on_press(self, key):
        print(f'Нажата клавиша {key.name}')

    def on_release(self, key):
        print(f'Отжата клавиша {key.name}')

    def start_tracking(self):
        keyboard.on_press(self.on_press)
        keyboard.on_release(self.on_release)
        keyboard.wait()

from engine import Convertator
import keyboard


def main():
    user = Convertator('en-ru')
    keyboard.add_hotkey('command+ь', user.activate_convert)
    keyboard.wait()


if __name__ == "__main__":
    main()

# Ghbdtn, rfr ltkf? Xnj ltkftim?

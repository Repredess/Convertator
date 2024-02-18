from engine import Convertator
import keyboard
import os
from elevate import elevate


def is_root():
    return os.getuid() == 0


def main():
    # print('before ', is_root())
    # elevate()
    # print('after ', is_root())

    user = Convertator('en-ru')
    keyboard.add_hotkey('command+ь', user.activate_convert)
    keyboard.wait()


if __name__ == "__main__":
    main()

# Ghbdtn, rfr ltkf? Xnj ltkftim?
# Lf, pfdnhf z ghbqle r nt,t. Ns ,eltim ljvf? Z - lf!
# <skj bkb yt ,skj?
# "nb[ ,fhfyjd pltcm ghjcnj lj[ez b ,jkmit...
# Leitue, ns
# lzlz ns t,kfy yf[eq rnj nt,t hekenm yfexbk?

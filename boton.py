

import pyautogui as bot

def main():
    SI='si'
    NO='no'

    opt = bot.confirm(
            'Texto Principal',
            'Titulo de la ventana',
            [SI, NO]
)

    if opt == SI:
        print('se escogio si')

    elif opt == NO:
        print('se escogio no')


if __name__ == '__main__':
    main()


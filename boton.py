

import pyautogui as bot

def main():
    SI='si'
    NO='no'

    opt = bot.confirm(
            'Quiere la pregunta',
            'Titulos jajaja',
            [SI, NO]
)

    if opt == SI:
        print('Sisa mi perro')

    elif opt == NO:
        print('Nocas loca')


if __name__ == '__main__':
    main()


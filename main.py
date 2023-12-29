from os import system
from random import choice

from colorama import Fore, init

from constants import GALLOWS, WORDS

init(autoreset=True)
word = choice(WORDS)
word_ = ['__'] * len(word)
letters = []
color = Fore.RED
gal_index = 0
while True:
    system('cls')
    print(Fore.LIGHTGREEN_EX + '== Виселица ==')
    print(Fore.BLUE + GALLOWS[gal_index])
    print(f'Буквы: {",".join(letters)}')
    if gal_index > 5:
        print('Игра окончена! Вы проиграли.')
        break
    print(Fore.GREEN + ' '.join(word_))
    if ''.join(word_) == word.upper():
        print('Вы выиграли!')
        break
    letter = input('Введите букву: ').lower()
    if letter in word:
        color = Fore.GREEN
        for j in [i for i, l in enumerate(word) if l == letter]:
            word_[j] = letter.upper()
    else:
        gal_index += 1
        color = Fore.RED
    letters.append(color + letter.upper())

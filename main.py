from os import system
from random import choice

from colorama import Fore, init

from constants import GALLOWS, WORDS


def make_a_word(words_list):
    word = choice(words_list).upper()
    word_ = ['__'] * len(word)
    return word, word_


def start_game():
    letters = []
    gal_index = 0
    word, word_ = make_a_word(WORDS)
    main_loop(gal_index, letters, word, word_)


def main_loop(gal_index, letters, word, word_):
    while True:
        system('cls')
        print(Fore.LIGHTGREEN_EX + '== Виселица ==')
        print(Fore.BLUE + GALLOWS[gal_index])
        print(f'Буквы: {",".join(letters)}')

        if gal_index > 5:
            print(f'Вы проиграли! Слово: {word}')
            break
        print(Fore.GREEN + ' '.join(word_))

        if ''.join(word_) == word:
            print(f'Вы выиграли! Слово: {word}')
            break

        letter = input('Введите букву: ').upper()

        if letter in word:
            color = Fore.GREEN
            for j in [i for i, let in enumerate(word) if let == letter]:
                word_[j] = letter
        else:
            gal_index += 1
            color = Fore.RED

        letters.append(color + letter)


if __name__ == '__main__':
    init(autoreset=True)
    while True:
        start_game()
        ans = input('Сыграем еще? Д - да, Н - нет\n')
        if ans.lower() == 'н':
            print('Пока!')
            break

from random import choice

from constants import GALLOWS, WORDS

print('== Виселица ==')
word = choice(WORDS)
word_ = '__ ' * len(word)
gal_index = 0
while True:
    print(GALLOWS[gal_index])
    if gal_index > 5:
        break
    print(word_)
    letter = input('Введите букву: ')
    if letter in word:
        print(word.index(letter))
    else:
        gal_index += 1

print('Игра окончена! Вы проиграли.')

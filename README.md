# TheGallowsGame on Python 3

Этот репозиторий содержит игру "Виселица", написанную на Python 3.
Виселица - это классическая игра, в которой игроку нужно угадать слово, выбранное компьютером.
В игре у игрока есть ограниченное количество попыток, чтобы угадать буквы слова, иначе "виселица" рисуется постепенно.

![Screenshot 00](img/scr_00.png)

## Запуск игры в консоли

> python main.py

## Файлы игры

![Screenshot 01](img/scr_01.png)

В репозитории вы найдете файлы, необходимые для запуска игры:

- _main.py_ - главный файл, содержащий основной код игры.
- _word_list.txt_ - текстовый файл, содержащий список слов для игры. Вы можете изменить или расширить этот список,
  добавляя слова по одному на каждой новой строке.
- _constants.py_ - файл со списком строк, представляющих разные стадии рисования "виселицы". Каждая строка соответствует
  определенному количеству неправильных попыток игрока.
- _requirements.txt_ - файл со списком библиотек, которые нужны для запуска.

## Сторонние библиотеки

Была использована библиотека _colorama_ для придания игре красок.

## Послесловие

![Screenshot 02](img/scr_02.png)

У этой игры есть потенциал для дальнейшего развития, таких как добавление возможности выбора категории слов или
добавление графического интерфейса.
Если вы хотите внести изменения или улучшить игру, не стесняйтесь создавать ветви и вносить свои предложения.
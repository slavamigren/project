from utils import *
from players import Player
from basic_word import BasicWord


url = 'https://www.jsonkeeper.com/b/Q21Z/'
player = Player(input('Ввведите имя игрока\n'))
word = load_random_word(url)
guessed_word = None #слово, вводимое пользователем

print(f'''\nПривет, {player}!
Составьте {word.get_options_amount()} слов из слова {word}
Слова должны быть не короче 3 букв
Чтобы закончить игру, угадайте все слова или напишите "stop"
Поехали, ваше первое слово?\n''')

while player.get_used_words() != word.get_options_amount():
    guessed_word = input().lower()
    if guessed_word in ('stop', 'стоп'):
        print(get_statistic(player))
        quit()
    elif (err := check_word(guessed_word, player, word)):
        print(err + '\n')
    else:
        player.set_used_words(guessed_word)
        print('верно\n')

print(get_statistic(player))
# 1. Напишите программу, удаляющую из текста все слова содержащие "абв".
my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'
my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
my_text = " ".join(my_text)
print(my_text)

# 2. Игра с конфетами. Дано N конфет. Каждый игрок за каждый ход может взять не более M конфет.
# Побеждает игрок,забравший последнюю конфету.

import random

def play_game(n, m, players):
    count = random.randint(0, 1)
    while n > 0:
        print(f'{players[count % 2]}, сколько конфет возьмёте?')
        move = int(input())
        if move > n or move > m:
            print(f'Это слишком много, можно взять не более {m} конфет, у нас всего {n} конфет')
            attempt = 0
            while attempt == 0:
                if n >= move <= m:
                    attempt = 1
                    break
                print(f'{players[count % 2]}, сколько конфет возьмёте?')
                move = int(input())
        n = n - move
        if n > 0:
            print(f'Осталось {n} конфет{letter}')
        else:
            print('Конфеты закончились')
        count += 1
    return players[not count % 2]

player1 = input('Первый игрок, назовите свое имя? ')
player2 = input('Второй игрок, назовите свое имя ')
players = [player1, player2]

col_conf = int(input('Сколько конфет разыгрывается? '))
max_chag = int(input('Сколько максимально можно брать конфет за один ход? '))

winer = play_game(col_conf, max_chag, players)
if not winer:
    print('У нас нет победителя.')
else:
    print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')


# 3. Создайте программу для игры в "Крестики-нолики"
print("*", " Правила игры крестики - нолики: ", "*")
print("*", " вам необходимо последовательно вводить ячейку куда вы хотите поставить Х или О ", "*")

# игровое поле
board = list(range(1, 10))

# вывод поля
def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

# ввод данных пользователем
def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      # проверка, что введено число
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      # проверка, что не вышли за рамки поля
      if player_answer >= 1 and player_answer <= 9:
          # проверка, что клетка не занята
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

# проверка игрового поля
def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "Выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
my_text = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
my_text2 = '12W1B12W3B24W1B14W'
def encode_rle(stroka):
    str_code = ''
    i = 0
    while i < len(stroka):
        count = 1
        while i + 1 < len(stroka) and stroka[i] == stroka[i + 1]:
            count = count + 1
            i = i + 1
        # добавляет к результату текущий символ и его количество
        str_code += str(count) + stroka[i]
        i = i + 1
    return str_code

def decoding_rle(stroka:str):
    count = ''
    str_decode = ''
    for char in stroka:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_code = encode_rle(my_text)
print(str_code)

str_decode = decoding_rle(my_text2)
print(str_decode)

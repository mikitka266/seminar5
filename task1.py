#Создайте программу для игры с конфетами человек против человека.
#словие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#Все конфеты оппонента достаются сделавшему последний ход. 
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

candies =2021
move=1
max_move = 28
first_move= candies%(move+max_move)-move
print(f'ПСС...Если хочешь выиграть бери {first_move} конфет')
your_move = int(input("Какое количество конфет вы хотите взять? "))
if  your_move<19:
    bot_move = 19-your_move
if  your_move>19:
    bot_move =19+29-your_move
candies=candies-your_move-bot_move
print(f'Бот взял {bot_move} конфет, осталось {candies}')
while candies>0 and candies<=29:
    your_move = int(input("Какое количество конфет вы хотите взять? "))
    bot_move = 29-your_move
    candies=candies-your_move-bot_move
    print(f'Бот взял {bot_move} конфет, осталось {candies}')
    if candies==29:
        print('Бот умнее вас')
    if candies<29:
        print("Тебе повезло, кожанный")



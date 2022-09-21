# Создайте программу для игры в ""Крестики-нолики"".
print("Давай сыграем с тобой в одну игру")
desktop = [2,2,2,2,2,2,2,2,2]
temp=int
for i in range(1,10):
    if i%2 !=0:
        your_move=int(input('Игрок1, Введите номер вашего хода от 1 до 9 :'))
        if desktop[your_move-1] !=1 and desktop[your_move-1] !=0:
            desktop.insert(your_move-1,1)
            if (desktop[0]==desktop[1]==desktop[2]==1 or desktop[3]==desktop[4]==desktop[5]==1 or 
             desktop[6]==desktop[7]==desktop[8]==1 or desktop[6]==desktop[2]==desktop[4]==1 or
             desktop[0]==desktop[3]==desktop[6]==1 or desktop[1]==desktop[7]==desktop[4]==1 or
             desktop[2]==desktop[5]==desktop[8]==1 or desktop[0]==desktop[4]==desktop[8]==1 ):
             print("Игрок1, поздравляем с победой!")
             break
        else: print("Клетка занята либо такой клетки не существует")
    if i%2 ==0:
        my_move=int(input('Игрок2, Введите номер вашего хода от 1 до 9 :'))
        if desktop[my_move-1] !=1 and desktop[my_move-1] !=0:
            desktop.insert(your_move-1,0)
            if (desktop[0]==desktop[1]==desktop[2]==0 or desktop[3]==desktop[4]==desktop[5]==0 or 
             desktop[6]==desktop[7]==desktop[8]==0 or desktop[6]==desktop[2]==desktop[4]==0 or
             desktop[0]==desktop[3]==desktop[6]==0 or desktop[1]==desktop[7]==desktop[4]==0 or
             desktop[2]==desktop[5]==desktop[8]==0 or desktop[0]==desktop[4]==desktop[8]==0 ):
             print("Игрок2, поздравляем с победой!")
             break
        else: print("Клетка занята либо такой клетки не существует")



        
   




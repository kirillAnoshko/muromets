import os
def shop(player_name, player_hp, player_money, player_potions):
    print(f"{player_name} приехал в магазин,зелье лечения стоит 200,у него {player_money} монет, и {player_potions} зелий")
    print("1-купить зелье")
    print("2-вернуться к камню")

    while True:
        answer = input("введите номер действия и нажмите ENTER: ")


        if answer == "1":
            if player_money >= 200:
                player_money -= 200
                player_potions += 1
                print(f"{player_name} купил зелье")
            else:
                print("у вас нет денег")
                input("введите номер действия и нажмите ENTER")
        elif answer == "2":
            print("вернулся к камню")
            break



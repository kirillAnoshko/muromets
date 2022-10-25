import fight, dice, shop



    # создаем героя
player_name = "Вася Питонов"
player_hp = 100
player_money = 500
player_potions = 1

def game(player_name, player_hp, player_money, player_potions):
    print("1-битва с разбойниками")
    print("2-игра в кости")
    print("3-лавка алхимика")

    while True:
        answer = input("введите номер действия и нажмите ENTER: ")
        if answer == "1" or answer == "2" or answer == "3":
            break
    if answer == "1":
        fight.fight(player_name, player_hp, player_money, player_potions)
    elif answer == "2":
        dice.dice(player_name, player_hp, player_money, player_potions)
    elif answer == "3":
        shop.shop(player_name, player_hp, player_money, player_potions)




game(player_name, player_hp, player_money, player_potions)
from random import seed
from random import randrange
from datetime import datetime

#globals

score = [
    {
        "ones": -1,
        "twos": -1,
        "threes": -1,
        "fours": -1,
        "fives": -1,
        "sixes": -1
    },
    {
        "ones": -1,
        "twos": -1,
        "threes": -1,
        "fours": -1,
        "fives": -1,
        "sixes": -1
    },
]

#functions

def roll_dice(n):  # n plithos twn zariwn
    dice = []

    for i in range(n):
        dice += [randrange(1, 6 + 1)]

    return sorted(dice)


def player_turn():
    dices_rolling = 5
    dice_kept = []

    for roll in range(3):
        dice = roll_dice(dices_rolling)
        print("-" * 15)
        print("Roll " + str(roll + 1) + " !")
        if roll in range(2):
            while True:
                print("Dice = " + str(dice))
                choice = input("Do you want to keep a die? (Type the number or 'n'): ")
                if choice == 'n':
                    break
                elif int(choice) not in dice:
                    print("There is no " + choice + "in your dice!")
                else:
                    dices_rolling -= 1
                    dice.remove(int(choice))
                    dice_kept += [int(choice)]
        else: #roll == 2
            dice_kept += dice

    print("Your dice is: " + str(dice_kept))
    return  dice_kept

def translate_name(s):
    if s=="ones":
        return 1
    if s=="twos":
        return 2
    if s=="threes":
        return 3
    if s=="fours":
        return 4
    if s=="fives":
        return 5
    if s=="sixes":
        return 6

def player_picks(player, dice):
    print("You can store your dice as: ", end=", ")
    picks = []

    for key, value in score[player].items():
        if value == -1:
            print(key, end=", ")
            picks += [key]
    while True:
        choice = input("Type your chice: ")
        if choice not in picks:
            print("Wrong Choice! ")
            continue
        else:
            key_val = translate_name(choice)
            score[player][choice] = dice.count(key_val) * key_val
            return


def main():
    seed(datetime.now())
    dice = player_turn()
    player_picks(0, dice)
    print(score)

main()

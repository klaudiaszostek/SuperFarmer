import random

dice1 = ["królik"] * 6 + ["owca"] * 3 + ["świnia", "krowa", "wilk"]
dice2 = ["królik"] * 6 + ["owca"] * 2 + ["świnia"] * 2 + ["koń", "lis"]

def roll_dice():
    return [random.choice(dice1), random.choice(dice2)]

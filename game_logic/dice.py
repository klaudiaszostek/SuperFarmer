import random

dice1 = ["rabbit"] * 6 + ["sheep"] * 3 + ["pig", "cow", "wolf"]
dice2 = ["rabbit"] * 6 + ["sheep"] * 2 + ["pig"] * 2 + ["horse", "fox"]

def roll_dice():
    return [random.choice(dice1), random.choice(dice2)]

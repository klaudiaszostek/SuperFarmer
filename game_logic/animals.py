animal_list = ["rabbit", "sheep", "pig", "cow", "horse", "small_dog", "big_dog"]

def apply_threats(animals, dice_results):
    log = []
    if "fox" in dice_results:
        if animals["small_dog"] > 0:
            animals["small_dog"] -= 1
            log.append("Lis został odstraszony przez małego psa.")
        else:
            log.append("Lis pożarł wszystkie króliki!")
            animals["rabbit"] = 0

    if "wolf" in dice_results:
        if animals["big_dog"] > 0:
            animals["big_dog"] -= 1
            log.append("Wilk został odstraszony przez dużego psa.")
        else:
            log.append("Wilk pożarł owce, świnie i krowy!")
            animals["sheep"] = 0
            animals["pig"] = 0
            animals["cow"] = 0

    return log

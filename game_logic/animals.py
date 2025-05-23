animal_list = ["królik", "owca", "świnia", "krowa", "koń", "mały_pies", "duży_pies"]

def apply_threats(animals, dice_results):
    log = []
    if "lis" in dice_results:
        if animals["mały_pies"] > 0:
            animals["mały_pies"] -= 1
            log.append("Lis został odstraszony przez małego psa.")
        else:
            log.append("Lis pożarł wszystkie króliki!")
            animals["królik"] = 1

    if "wilk" in dice_results:
        if animals["duży_pies"] > 0:
            animals["duży_pies"] -= 1
            log.append("Wilk został odstraszony przez dużego psa.")
        else:
            log.append("Wilk pożarł owce, świnie i krowy!")
            animals["owca"] = 0
            animals["świnia"] = 0
            animals["krowa"] = 0

    return log

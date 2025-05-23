from game_logic.animals import animal_list, apply_threats
from game_logic.market import market_rates


class Player:
    def __init__(self):
        self.animals = {animal: 0 for animal in animal_list}
        self.animals["królik"] = 1
        self.turn = 1
        self.exchanged_this_turn = False
        self.main_herd = {
            "królik": 30,
            "owca": 20,
            "świnia": 15,
            "krowa": 10,
            "koń": 5,
            "mały_pies": 5,
            "duży_pies": 3
        }


    def get_animals(self):
        return self.animals


    def apply_roll(self, dice_results):
        log = []

        log += apply_threats(self.animals, dice_results)

        dice_counts = {}
        for animal in dice_results:
            if animal not in dice_counts:
                dice_counts[animal] = 1
            else:
                dice_counts[animal] += 1

        for animal, count_on_dice in dice_counts.items():
            if animal in ["koń", "krowa"]:
                continue

            owned = self.animals.get(animal, 0)
            total = owned + count_on_dice

            if owned > 0:
                pairs = total // 2
            else:
                pairs = 1 if count_on_dice == 2 else 0

            bonus = min(pairs, self.main_herd.get(animal, 0))
            if bonus > 0:
                self.animals[animal] += bonus
                self.main_herd[animal] -= bonus
                log.append(f"Dostałeś {bonus} {animal}(ów) za {pairs} pełnych par.")

        self.exchanged_this_turn = False
        self.turn += 1
        return log



    def get_possible_trades(self):
        trades = []
        for rate in market_rates:
            if self.animals[rate['from']] >= rate['cost']:
                trades.append(rate)
        return trades


    def exchange(self, from_animal, to_animal):
        if self.exchanged_this_turn:
            return False, "Możesz wykonać tylko 1 wymianę na turę."

        for rate in market_rates:
            if rate['from'] == from_animal and rate['to'] == to_animal:
                if self.animals[from_animal] >= rate['cost']:
                    self.animals[from_animal] -= rate['cost']
                    self.animals[to_animal] += 1
                    self.exchanged_this_turn = True
                    return True, "Wymiana zakończona sukcesem."
                else:
                    return False, "Brak wystarczających zasobów do wymiany."

        return False, "Taka wymiana nie jest dostępna."


    def check_victory(self):
        required = ["królik", "owca", "świnia", "krowa", "koń"]
        return all(self.animals[animal] >= 1 for animal in required)

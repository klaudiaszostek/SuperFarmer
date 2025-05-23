from game_logic.animals import animal_list, apply_threats

class Player:
    def __init__(self):
        self.animals = {animal: 0 for animal in animal_list}
        self.animals["rabbit"] = 1
        self.turn = 1
        self.exchanged_this_turn = False

    def get_animals(self):
        return self.animals

    def apply_roll(self, dice_results):
        event_log = []
        event_log += apply_threats(self.animals, dice_results)

        for animal in dice_results:
            if animal in self.animals:
                self.animals[animal] += 1

        self.exchanged_this_turn = False
        self.turn += 1
        return event_log

    def get_possible_trades(self):
        trades = []

        if self.animals["rabbit"] >= 6:
            trades.append({"from": "rabbit", "to": "sheep", "cost": 6})
        if self.animals["sheep"] >= 2:
            trades.append({"from": "sheep", "to": "pig", "cost": 2})
        if self.animals["pig"] >= 3:
            trades.append({"from": "pig", "to": "cow", "cost": 3})
        if self.animals["cow"] >= 2:
            trades.append({"from": "cow", "to": "horse", "cost": 2})
        return trades

    def exchange(self, from_animal, to_animal):
        if self.exchanged_this_turn:
            return False, "Możesz wykonać tylko 1 wymianę na turę."

        rates = {
            ("rabbit", "sheep"): 6,
            ("sheep", "pig"): 2,
            ("pig", "cow"): 3,
            ("cow", "horse"): 2
        }

        if (from_animal, to_animal) in rates:
            cost = rates[(from_animal, to_animal)]
            if self.animals[from_animal] >= cost:
                self.animals[from_animal] -= cost
                self.animals[to_animal] += 1
                self.exchanged_this_turn = True
                return True, "Wymiana zakończona sukcesem."

        return False, "Brak wystarczających zasobów do wymiany."

    def check_victory(self):
        required = ["rabbit", "sheep", "pig", "cow", "horse"]
        return all(self.animals[animal] >= 1 for animal in required)

import json


class Match:
    """
        Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune
    contenant deux éléments : un joueur et un score. Les matchs doivent être stockés sous
    forme de liste dans l'instance du tour auquel ils appartiennent.
    """

    def __init__(self, player_1, player_2, score_1: float, score_2: float):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def __str__(self) -> str:
        return f"([{self.player_1}, {self.score_1}], [{self.player_2}, {self.score_2}])"

    def get_serialized_match(self):
        serialized_match = {
            "player_1": self.player_1.get_serialized_player(),
            "player_2": self.player_2.get_serialized_player(),
            "score_1": self.score_1,
            "score_2": self.score_2,
        }
        return json.dumps(serialized_match)

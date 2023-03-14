import json
import random


class Match:
    """
        Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune
    contenant deux éléments : un joueur et un score. Les matchs doivent être stockés sous
    forme de liste dans l'instance du tour auquel ils appartiennent.
    """

    def __init__(
        self, 
        player_1, 
        player_2, 
        score_1: float=0.0, 
        score_2: float=0.0, 
        name: str
        ):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2
        self.winner = None
        self.name = name
    
    def create_pairs(self):
        """set tuple of match"""
        return (
            [self.player_1, self.score_1],[self.player_2, self.score_2]
        )
    
    def set_player_color(self):
        if random.choice([True, False]):
            self.color_player1 = "Blanc"
            self.color_player2 = "Noir"
        else:
            self.color_player1 = "Noir"
            self.color_player2 = "Blanc"

    def get_serialized_match(self):
        serialized_match = {
            "player_1": self.player_1.get_serialized_player(),
            "player_2": self.player_2.get_serialized_player(),
            "score_1": self.score_1,
            "score_2": self.score_2,
            "winner":self.winner,
            "name": self.name
        }
        return serialized_match

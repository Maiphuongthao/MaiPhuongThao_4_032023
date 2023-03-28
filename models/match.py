import random


class Match:
    """
        Un match unique doit être stocké sous la forme d'un tuple contenant deux listes, chacune
    contenant deux éléments : un joueur et un score. Les matches doivent être stockés sous
    forme de liste dans l'instance du tour auquel ils appartiennent.
    """

    def __init__(
        self,
        player_1=None,
        player_2=None,
        score_1=0.0,
        score_2=0.0,
    ):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def set_pairs(self):
        """set tuple of match"""
        return ([self.player_1, self.score_1], [self.player_2, self.score_2])

    def get_serialized_match(self):
        serialized_match = {
            "Joueur_1": self.player_1,
            "Score_1": self.score_1,
            "Joueur_2": self.player_2,
            "Score_2": self.score_2,
        }
        return serialized_match

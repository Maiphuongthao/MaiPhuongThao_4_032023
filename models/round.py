import datetime
import json
from match import Match


class Round:
    """
        chaque instance du tour doit contenir un nom.
        Elle doit également
    contenir un champ Date et heure de début et un champ Date et heure de fin, qui doivent
    tous deux être automatiquement remplis lorsque l'utilisateur crée un tour et le marque
    comme terminé.
    """

    def __init__(
        self,
        name: str,
        # pair_of_players: str,
        start_date_time: datetime,
        end_date_time: datetime,
        matchs: list[Match],
    ):
        self.name = name
        # self.pair_of_players = (pair_of_players,)
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.matchs: matchs

    def __str__(self) -> str:
        pass

    def set_round(self):
        """
        return round to a list
        """
        return [self.name, self.start_date_time, self.end_date_time, self.matchs]

    def get_list_of_matchs(self):
        self.matchs.append(Match.create_pairs())

    def get_serialized_round(self):
        serialized_round = {
            "name": self.name,
            # "pair_of_players": self.pair_of_players,
            "start_date_time": self.start_date_time,
            "end_date_time": self.end_date_time,
            "matches": [match.get_serialized_match() for match in self.matchs],
        }
        return json.dumps(serialized_round)

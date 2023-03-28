import datetime


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
        start_date: datetime,
        end_date: datetime,
        matches: list,
    ):
        self.name = name
        # self.pair_of_players = (pair_of_players,)
        self.start_date = start_date
        self.end_date = end_date
        self.matches = matches

    def __str__(self) -> str:
        pass

    def get_serialized_round(self):
        serialized_round = {
            "Nom": self.name,
            "Date de début": self.start_date,
            "Date de fin": self.end_date,
            "List des matchs": self.matches,
        }
        return serialized_round

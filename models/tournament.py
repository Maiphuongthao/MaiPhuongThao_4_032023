import datetime
import json
from round import Round
from player import Player


class Tournament:
    """
    Create class Tournaments to get tournaments infos like name, location,
    start_date etc

    """

    def __init__(
        self,
        name: str,
        location: str,
        start_date: datetime,
        end_date: datetime,
        rounds: list[Round],
        players: list[Player],
        current_round: int,
        description: str,
        number_of_rounds: int = 4,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.players = players
        self.current_round = current_round
        self.description = description
        self.number_of_rounds = number_of_rounds

    def __str__(self) -> str:
        pass

    def get_serialized_tournaments(self):
        serialized_tournaments = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rounds": [round.get_serialized_round() for round in self.rounds],
            "players": [player.get_serialized_player() for player in self.players],
            "current_round": self.current_round,
            "description": self.description,
            "number_of_rounds": self.number_of_rounds,
        }
        return json.dumps(serialized_tournaments)

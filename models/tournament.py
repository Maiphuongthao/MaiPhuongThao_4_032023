import datetime
from tinydb import TinyDB, where
from pathlib import Path
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

    def sort_players_by_rank(self):
        """ "Sort players by theirs rank ascending position"""
        self.players = sorted(self.players, key=lambda x: x.get("rank"))

    def sort_palyer_by_score(self):
        """sort players by their score descending position"""
        self.players = sorted(self.players, key=lambda x: x.get("score"), reverse=True)

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
        return serialized_tournaments

    def save_tournament_data(self):
        """Save tournament data into json file"""
        file_name = "tournaments.json"
        file_path = Path("database")

        if not Path(file_path).exists():
            Path.mkdir(file_path)

        path = file_path.joinpath(file_name)
        data = TinyDB(path)
        data.insert(self.get_serialized_tournaments())

    def update_tournament(self):
        """update tournament after each round"""
        data = TinyDB("database/tournaments.json")
        data.update({"rounds": self.rounds}, where("name") == self.name)
        data.update({"players": self.players}, where("name" == self.name))
        data.update({"current_round": self.current_round}, where("name" == self.name))

    def update_time(self, time, info):
        """
        update start and end time of tournament
        """
        data = TinyDB("database/tournaments.json")
        data.update({info: time}, where("name" == self.name))

    def load_tournament(self):
        """
        Load tournament data ti return the list"""
        data = TinyDB("database/tournaments.json")
        data.all()
        tournaments_list = []
        for tournament in data:
            tournaments_list.append(tournament)
        return tournaments_list

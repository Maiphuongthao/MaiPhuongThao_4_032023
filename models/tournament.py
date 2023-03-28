from tinydb import TinyDB, where
from pathlib import Path
import datetime


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
        rounds: list,
        players: list,
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

    def sort_players_by_rank(self):
        """ "Sort players by theirs rank ascending position"""
        self.players = sorted(self.players, key=lambda x: x.get("rank"))

    def sort_players_by_score(self):
        """sort players by their score descending position"""
        self.players = sorted(self.players, key=lambda x: x.get("scores"), reverse=True)

    def merge_players(self, top_players, bottom_players):
        merged_players = []
        for i in range(len(self.players) // 2):
            merged_players.append(top_players[i])
            merged_players.append(bottom_players[i])

        self.players = merged_players

    def get_serialized_tournaments(self):
        serialized_tournaments = {
            "Nom": self.name,
            "Lieu": self.location,
            "Date de début": self.start_date,
            "Date de fin": self.end_date,
            "List des tours": self.rounds,
            "List des joueurs": self.players,
            "Tour actuel": self.current_round,
            "Description": self.description,
            "Nombre de tours": self.number_of_rounds,
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
        data.update({"List de tours": self.rounds}, where("Nom") == self.name)
        data.update({"List des joueurs": self.players}, where("Nom") == self.name)
        data.update({"Date de fin": self.end_date}, where("Nom") == self.name)
        data.update({"Tour actuel": self.current_round}, where("Nom") == self.name)

    def update_time(self, time, info):
        """
        update start and end time of tournament
        """
        data = TinyDB("database/tournaments.json")
        data.update({info: time}, where("Nom" == self.name))

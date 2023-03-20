from tinydb import TinyDB, where
from pathlib import Path


class Player:
    """
    Create Player class to get player_id, firstname, lastname, birthday, rank ,
    scores and who they play with.
    Then get serialized player's data
    """

    def __init__(
        self,
        player_id: str,
        first_name: str,
        last_name: str,
        birthday: str,
        rank: int,
    ):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_day = birthday
        self.rank = rank
        self.scores = 0.0
        self.play_with = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_serialized_player(self):
        serialized_player = {
            "player_id": self.player_id,
            "firstname": self.first_name,
            "lastname": self.last_name,
            "birthday": self.birth_day,
            "rank": self.rank,
            "scores": self.scores,
        }
        return serialized_player

    def save_player_data(self):
        """
        save user data to json file
        """
        file_name = "players.json"
        file_path = Path("database")

        if not Path(file_path).exists():
            Path.mkdir(file_path)

        path = file_path.joinpath(file_name)
        data = TinyDB(path)
        data.insert(self.get_serialized_player())

    def update_player(self, info, choice):
        """
        Update user info in database: here is json file
        @param info has user input that need to be update
        @param choice will have info in integer(rank) or string for the rest
        """
        data = TinyDB("database/players.json")
        if choice == "rank":
            data.update({choice: int(info)}, where("player_id") == self.player_id)
        else:
            data.update({choice: info}, where("player_id") == self.player_id)

    def load_players_data(self):
        """get list of players"""
        data = TinyDB("database/players.json")
        data.all()
        players = []
        for player in data:
            players.append(player)

        return players

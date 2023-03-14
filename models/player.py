import json
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

    def save_player(self):
        file_name = "players.json"
        file_path = Path("database")

        if not Path(file_path).exists():
            Path.mkdir(file_path)

        path = file_path.joinpath(file_name)
        with open(path, "a") as file:
            json.dump(
                self.get_serialized_player(),
                file,
                indent=4,
            )

    def update_player(self):
        file = "database/players.json"
        with open(file, "r+") as f:
            for line in f:
                data = json.loads(line)
                if self.player_id == data["player_id"]:
                    print("okay")


# player = Player("AB12345", "thao", "mai", "24/22/1990", 1)
# player.save_player()
# player2 = Player("AB12346", "thao", "mai", "24/22/1990", 1)
# player2.save_player()
# player.update_player()

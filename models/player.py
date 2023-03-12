import json


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
            "firstname": self.first_name,
            "lastname": self.last_name,
            "birthday": self.birth_day,
            "rank": self.rank,
            "scores": self.scores,
        }
        return json.dumps(serialized_player)


# player = Player("AB12345", "thao", "mai", "24/22/1990",1)

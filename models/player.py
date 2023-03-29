from tinydb import TinyDB, where


class Player:
    """
    Create Player class to get player_id, firstname, lastname, birthday, rank ,
    scores and who they play with.
    Then get serialized player's data
    """

    def __init__(
        self,
        player_id: str,
        last_name: str,
        first_name: str,
        birthday: str,
        rank: int = 0,
    ):
        self.player_id = player_id
        self.last_name = last_name
        self.first_name = first_name
        self.birth_day = birthday
        self.rank = rank
        self.scores = 0.0

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_serialized_player(self):
        serialized_player = {
            "Joueur_id": self.player_id,
            "Nom": self.first_name,
            "Prénom": self.last_name,
            "Date de naissance": self.birth_day,
            "Classement": self.rank,
            "Score": self.scores,
        }
        return serialized_player

    def update_player(self, info, choice):
        """
        Update user info in database: here is json file
        @param info has user input that need to be update
        @param choice will have info in integer(rank) or string for the rest
        """
        data = TinyDB("database/players.json")
        if choice == "Classement":
            data.update({choice: int(info)}, where("Joueur_id") == self.player_id)
        else:
            data.update({choice: info}, where("Joueur_id") == self.player_id)

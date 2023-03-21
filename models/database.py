from tinydb import TinyDB


def load_players_data():
    """get list of players"""
    data = TinyDB("database/players.json")
    data.all()
    players = []
    for player in data:
        players.append(player)

    return players

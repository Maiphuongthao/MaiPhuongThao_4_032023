from tinydb import TinyDB
import datetime


def load_players_data():
    """get list of players"""
    data = TinyDB("database/players.json")
    data.all()
    return [player for player in data]


def set_start_date():
    start_date = datetime.datetime.now
    return start_date


def get_player_ids():
    return [player["id"] for player in load_players_data()]

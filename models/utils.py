from tinydb import TinyDB
from pathlib import Path
import datetime

"""
This is for the database functions and other small need functions which doesn't need to be part of object
"""


def save_data_db(file_name, serialized_data):
    """
    save user data to json file, set id json as id of player
    """
    file_path = Path("database")

    if not Path(file_path).exists():
        Path.mkdir(file_path)

    path = file_path.joinpath(file_name)
    data = TinyDB(path)
    id = data.insert(serialized_data)
    data.update({"id": id}, doc_ids=[id])


def load_players_data():
    """get list of players"""
    data = TinyDB("database/players.json")
    data.all()
    return [player for player in data]


def load_tournament():
    """
    Load tournament data ti return the list"""
    data = TinyDB("database/tournaments.json")
    data.all()
    tournaments_list = []
    for tournament in data:
        tournaments_list.append(tournament)
    return tournaments_list


def set_date_time():
    date_time = datetime.datetime.now()
    start_date = date_time.strftime("%d/%m/%Y, %H:%M:%S")
    return start_date


def get_player_ids():
    return [player["id"] for player in load_players_data()]

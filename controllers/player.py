from models.player import Player
from models import utils
from views.player import PlayerView
from views.menu import Menu

class PlayerManager:
    def __init__(self) -> None:
        self.player_view = PlayerView()
        self.view_menu = Menu()
    def return_menu(self):
        from controllers.menu import MenuManager
        MenuManager().start_main_menu()
    def create_tournament(self):
        from controllers.tournaments import TournamentManager
        TournamentManager().create_tournament()

    def create_player(self):
        self.player_view.create_player_title()
        player_infos = []
        info_values = [
            "Jouer id",
            "Nom",
            "Prénom",
            "Naissance (dd/mm/yyy)",
        ]
        for i in info_values:
            self.view_menu.input_prompt_text(i)
            user_input = input()
            if user_input == "q":
                self.return_menu()
            else:
                player_infos.append(user_input)

        self.player_view.review_player(player_infos)
        user_input = input().lower()
        match user_input:
            case "oui":
                player = Player(
                    player_id=player_infos[0],
                    first_name=player_infos[1],
                    last_name=player_infos[2],
                    birthday=player_infos[3],
                )
                serialized_data = player.get_serialized_player()
                utils.save_data_db("players.json", serialized_data)
                self.player_view.player_saved()
                self.create_player()

            case "non":
                self.return_menu()
            case _:
                self.view_menu.error_msg()
                self.return_menu()

    def update_player_info(self):
        """
        update existing player's infos
        load player data and get selected player
        chose the option that need to be changed then save it to new
        """
        players = utils.load_players_data()
        self.player_view.select_a_player(players, "pour modifier")
        self.view_menu.input_prompt()
        user_input = input()
        if user_input == "q":
            self.return_menu()
        # breakpoint()

        p = players[int(user_input) - 1]
        p = Player(
            p["Joueur_id"],
            p["Nom"],
            p["Prénom"],
            p["Date de naissance"],
        )
        input_values = ["Prénom", "Nom", "Date de naissance"]
        self.player_view.update_player_info(p, input_values)
        self.view_menu.input_prompt()
        user_input = input()

        if user_input == "q":
            self.update_player_info()

        elif int(user_input) <= len(input_values):
            update_info = input_values[int(user_input) - 1]

            key = ["Nom", "Prénom", "Date de naissance"]
            updated_info = key[int(user_input) - 1]

            self.view_menu.input_prompt_text(f"Nouveau {update_info}")
            user_input = input()

            if user_input == "q":
                self.return_menu()
            else:
                # updated_info = key[int(user_input) - 1]
                p.update_player(user_input, updated_info)
                self.player_view.player_saved()
                self.update_player_info()
        else:
            self.view_menu.error_msg()
            self.update_player_info()

    def select_players(self, total_chosen_players):
        """
        Select playrs for tournament:
        @param: total_chosed_player as number of total player that user chose
        @return: list of chosen players
        """
        players = utils.load_players_data()
        list_ids = utils.get_player_ids()

        len_list = len(list_ids)
        tour_players = []
        # while the players in data is not enough to chose, user need to add more new player
        while total_chosen_players > len_list:
            self.player_view.total_players_prompt(len_list, total_chosen_players)
            self.create_player()
            len_list += 1

        i = 0
        # while there are enough players in the data, chose them as number of length
        while i < total_chosen_players:
            self.player_view.select_a_player(players, i + 1)
            self.view_menu.input_prompt()
            user_input = int(input())
            if user_input == "q":
                self.create_tournament()

            elif user_input in list_ids:
                index = list_ids.index(user_input)
                tour_players.append(players[index])
                list_ids.remove(list_ids[index])
                players.remove(players[index])
                i += 1
            else:
                self.view_menu.player_selected_error()
                selection = input()
                if selection == "1":
                    self.select_players(total_chosen_players)
                if selection == "2":
                    tour_players.append(self.create_player())
                else:
                    self.view_menu.error_msg()
                    self.create_tournament()

        return tour_players

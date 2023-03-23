from views.menu import Menu
from models.player import Player
from models.tournament import Tournament
from models import utils
from controllers.tournaments import TournamentManager


class MenuManager:
    def __init__(self):
        self.view_menu = Menu()
        self.tournament_controller = TournamentManager()

    def return_option(self):
        self.view_menu.exit_msg()
        user_input = input().lower()
        match user_input:
            case "oui":
                exit()
            case "non":
                self.start_main_menu()
            case _:
                self.view_menu.error_msg()
                self.return_option()

    def start_main_menu(self):
        """
        Selections of main menu
        """
        self.view_menu.title()

        choices = {
            "1": {"text": "Créer un tournois", "controller": self.create_tournament},
            "2": {
                "text": "Charger un tournois",
                "controller": self.resume_tournament(),
            },
            "3": {
                "text": "Créer des jouers",
                "controller": self.create_player,
            },
            "4": {
                "text": "Modifier un jouer",
                "controller": self.update_player_info,
            },
            "5": {"text": "Rapports", "controller": self.reports_menu},
            "q": {"text": "Quitter", "controller": self.exit},
        }

        self.view_menu.main_menu(choices)
        self.view_menu.input_prompt()
        user_input = input().lower()

        try:
            choices[user_input]["controller"]()
        except KeyError:
            self.view_menu.error_msg
            self.start_main_menu

    def create_tournament(self):
        """create a tournament and save it"""
        self.view_menu.tournament_title()
        tournament_info = []
        infos = [
            "name",
            "location",
            "description",
            "date de debut",
            "nombre des jouers (min 8)",
            "nombre de tour (min 4)",
        ]
        for info in infos:
            self.view_menu.input_prompt_text(info)
            user_input = input()
            if user_input == "q":
                self.start_main_menu()
            else:
                tournament_info.append(user_input)

        if tournament_info[3] == "":
            tournament_info[3] = utils.set_start_date()
        if tournament_info[4] == "":
            tournament_info[4] = int(8)
        if tournament_info[5] == "":
            tournament_info[5] = int(4)

        tour_players = self.select_players(tournament_info[4])
        self.view_menu.review_tournament(tournament_info, tour_players)
        user_input = input().lower()
        if user_input == "non":
            self.start_main_menu()
        elif user_input == "oui":
            tournament = Tournament(
                name=tournament_info[0],
                location=tournament_info[1],
                start_date=tournament_info[3],
                end_date="TBD",
                rounds=[],
                players=tour_players,
                current_round=1,
                description=tournament_info[2],
                number_of_rounds=tournament_info[5],
            )
            tournament.save_tournament_data()
            self.view_menu.tournament_saved()
            self.view_menu.start_tournament_question()
            user_input = input()
            if user_input == "oui":
                self.tournament_controller.start_tournament(tournament)
            elif user_input == "non":
                self.start_main_menu()
            else:
                self.view_menu.error_msg()
        else:
            self.view_menu.error_msg()

    def select_players(self, total_chosed_players):
        """
        Select playrs for tournament, 4 tours corresponds with 8 players by max default
        """
        players = utils.load_players_data()
        list_ids = utils.get_player_ids()

        len_list = len(list_ids)
        tour_players = []

        while total_chosed_players > len_list:
            self.view_menu.total_players_prompt(len_list, total_chosed_players)
            self.create_player()
            len_list

        i = 0
        while i < total_chosed_players:
            self.view_menu.select_a_player(players, i + 1)
            self.view_menu.input_prompt()
            user_input = int(input())
            if user_input == "q":
                self.start_main_menu()

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
                    self.select_players(total_chosed_players)
                if selection == "2":
                    self.create_player()
                else:
                    self.view_menu.error_msg()
                    self.create_tournament()

        return tour_players

    def reports_menu(self):
        pass

    def resume_tournament(self):
        pass

    def exit(self):
        pass

    def create_player(self):
        self.view_menu.create_player_title()
        player_infos = []
        info_values = ["Jouer id", "Prénom", "Nom", "Naissance (dd/mm/yyy)", "rang"]
        for i in info_values:
            self.view_menu.input_prompt_text(i)
            user_input = input()
            if user_input == "q":
                self.start_main_menu()
            else:
                player_infos.append(user_input)

        if player_infos[4] == "":
            player_infos[4] = "0"

        self.view_menu.review_player(player_infos)
        user_input = input().lower()
        match user_input:
            case "oui":
                player = Player(
                    player_id=player_infos[0],
                    first_name=player_infos[1],
                    last_name=player_infos[2],
                    birthday=player_infos[3],
                    rank=int(player_infos[4]),
                )
                player.save_player_data()
                self.view_menu.player_saved()

            case "non":
                self.start_main_menu()
            case _:
                self.view_menu.error_msg()
                self.start_main_menu()

    def update_player_info(self):
        """
        update existing player's infos
        load player data and get selected player
        chose the option that need to be changed then save it to new
        """
        players = utils.load_players_data()
        self.view_menu.select_a_player(players, "pour modifier")
        self.view_menu.input_prompt()
        user_input = input()
        if user_input == "q":
            self.start_main_menu()
        # breakpoint()

        p = players[int(user_input) - 1]
        p = Player(
            p["player_id"], p["firstname"], p["lastname"], p["birthday"], p["rank"]
        )

        input_values = ["prénom", "nom", "date de naissance", "rang"]
        self.view_menu.update_player_info(p, input_values)
        self.view_menu.input_prompt()
        user_input = input()

        if user_input == "q":
            self.start_main_menu()

        elif int(user_input) <= len(input_values):
            update_info = input_values[int(user_input) - 1]

            key = ["firstname", " lastname", " birthday", "rank"]
            updated_info = key[int(user_input) - 1]

            self.view_menu.input_prompt_text(f"nouveau {update_info}")
            user_input = input()

            if user_input == "q":
                self.start_main_menu()
            else:
                # updated_info = key[int(user_input) - 1]
                p.update_player(user_input, updated_info)
                self.view_menu.player_saved()
                self.update_player_info()
        else:
            self.view_menu.error_msg()
            self.update_player_info()

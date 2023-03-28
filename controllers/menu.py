from views.menu import Menu
from views.tournament import TournamentView
from views.player import PlayerView
from views.report import ReportView
from models.player import Player
from models.tournament import Tournament
from models import utils
from controllers.tournaments import TournamentManager


class MenuManager:
    """
    Menu and main functions of menu
    """

    def __init__(self):
        self.view_menu = Menu()
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
        self.tournament_controller = TournamentManager()
        self.report_view = ReportView()

    def start_main_menu(self):
        # main menu choices
        self.view_menu.title()

        choices = {
            "1": {"text": "Créer un tournois", "controller": self.create_tournament},
            "2": {
                "text": "Charger un tournois",
                "controller": self.resume_tournament,
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
            self.view_menu.error_msg()
            self.start_main_menu()

    def create_tournament(self):
        """create a tournament and save it to db"""
        self.tournament_view.tournament_title()
        tournament_info = []
        infos = [
            "Nom",
            "Lieu",
            "Description",
            "Date de debut",
            "Nombre des jouers (8 par default))",
            "Nombre de tour (4 par default)",
        ]
        for info in infos:
            self.view_menu.input_prompt_text(info)
            user_input = input()
            if user_input == "q":
                self.start_main_menu()
            else:
                tournament_info.append(user_input)
        # check if the input has no return values, return value by default where it isn't
        if tournament_info[3] == "":
            tournament_info[3] = utils.set_date_time()
        if tournament_info[4] == "":
            tournament_info[4] = int(8)
        if tournament_info[5] == "":
            tournament_info[5] = int(4)

        # select players and add to players lists. Min 8 players as min 4 tours to begin a tournament
        tour_players = self.select_players(tournament_info[4])
        self.tournament_view.review_tournament(tournament_info, tour_players)
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
            serialized_data = tournament.get_serialized_tournaments()
            # Save tournament to json file
            utils.save_data_db("tournaments.json", serialized_data)
            self.tournament_view.tournament_saved()
            # Check if user want to start the tournament
            self.tournament_view.start_tournament_question()
            user_input = input()
            if user_input == "oui":
                self.tournament_controller.start_tournament(tournament)
            elif user_input == "non":
                self.start_main_menu()
            else:
                self.view_menu.error_msg()
        else:
            self.view_menu.error_msg()

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

    def resume_tournament(self):
        tournament_data = utils.load_tournament()
        tournament = self.one_tournament(tournament_data)
        self.tournament_controller.start_tournament(tournament)

    def create_player(self):
        self.player_view.create_player_title()
        player_infos = []
        info_values = [
            "Jouer id",
            "Nom",
            "Prénom",
            "Naissance (dd/mm/yyy)",
            "Classement",
        ]
        for i in info_values:
            self.view_menu.input_prompt_text(i)
            user_input = input()
            if user_input == "q":
                self.start_main_menu()
            else:
                player_infos.append(user_input)

        if player_infos[4] == "":
            player_infos[4] = "0"

        self.player_view.review_player(player_infos)
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
                serialized_data = player.get_serialized_player()
                utils.save_data_db("players.json", serialized_data)
                self.player_view.player_saved()
                self.create_player()

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
        self.player_view.select_a_player(players, "pour modifier")
        self.view_menu.input_prompt()
        user_input = input()
        if user_input == "q":
            self.start_main_menu()
        # breakpoint()

        p = players[int(user_input) - 1]
        p = Player(
            p["Joueur_id"],
            p["Nom"],
            p["Prénom"],
            p["Date de naissance"],
            p["Classement"],
        )

        input_values = ["Prénom", "Nom", "Date de naissance", "Classement"]
        self.player_view.update_player_info(p, input_values)
        self.view_menu.input_prompt()
        user_input = input()

        if user_input == "q":
            self.update_player_info()

        elif int(user_input) <= len(input_values):
            update_info = input_values[int(user_input) - 1]

            key = ["Nom", "Prénom", "Date de naissance", "Classement"]
            updated_info = key[int(user_input) - 1]

            self.view_menu.input_prompt_text(f"Nouveau {update_info}")
            user_input = input()

            if user_input == "q":
                self.start_main_menu()
            else:
                # updated_info = key[int(user_input) - 1]
                p.update_player(user_input, updated_info)
                self.player_view.player_saved()
                self.update_player_info()
        else:
            self.view_menu.error_msg()
            self.update_player_info()

    def reports_menu(self):
        self.report_view.report_title()
        choices = {
            "1": {
                "text": "Tous les jouers",
                "controller": self.report_view.display_players,
                "value": utils.load_players_data(),
            },
            "2": {
                "text": "Tous les tournois",
                "controller": self.report_view.display_all_tournaments,
                "value": utils.load_tournament(),
            },
            "3": {
                "text": "Un tournois",
                "controller": self.display_one_tournament,
                "value": utils.load_tournament(),
            },
            "4": {
                "text": "Tous les joueurs d'un tournois",
                "controller": self.display_players_one_tournament,
                "value": utils.load_tournament(),
            },
            "5": {
                "text": "Tous les tours et matches d'un tournois",
                "controller": self.rounds_matches,
                "value": utils.load_tournament(),
            },
            "q": {
                "text": "Quitter pour retourner au menu principal",
                "controller": self.start_main_menu,
            },
        }
        self.report_view.report_menu(choices)
        self.view_menu.input_prompt()
        user_input = input().lower()
        try:
            choices[user_input]["controller"](choices[user_input]["value"])
        except KeyError:
            self.view_menu.error_msg()
            self.reports_menu()

    def one_tournament(self, tournaments):
        if len(tournaments) == 0:
            self.tournament_view.no_tournament()
            self.start_main_menu()
        else:
            self.tournament_view.select_tournament(tournaments)
            self.view_menu.input_prompt()
            user_input = input()

            if user_input == "q":
                self.reports_menu()
            try:
                for t in range(len(tournaments)):
                    if int(user_input) == tournaments[t]["id"]:
                        loaded_tournament = tournaments[int(user_input) - 1]
                        loaded_tournament = Tournament(
                            loaded_tournament["Nom"],
                            loaded_tournament["Lieu"],
                            loaded_tournament["Date de début"],
                            loaded_tournament["Date de fin"],
                            loaded_tournament["List des tours"],
                            loaded_tournament["List des joueurs"],
                            loaded_tournament["Tour actuel"],
                            loaded_tournament["Description"],
                            loaded_tournament["Nombre de tours"],
                        )
                        return loaded_tournament

            except KeyError:
                self.view_menu.error_msg()
                self.reports_menu()

    def display_one_tournament(self, tournaments):
        tournament = self.one_tournament(tournaments)
        self.report_view.display_one_tournament(tournament)

    def display_players_one_tournament(self, tournaments):
        tournament = self.one_tournament(tournaments)
        self.report_view.display_players_one_tournament(tournament)

    def exit(self):
        pass

    def rounds_matches(self, tournaments):
        tournament = self.one_tournament(tournaments)
        rounds = tournament.rounds
        for r in range(len(rounds)):
            breakpoint()
            matches = rounds[r]["List des matchs"]
        self.report_view.display_rounds_matches(tournament, rounds, matches)

from views.menu import Menu
from views.tournament import TournamentView
from views.player import PlayerView
from views.report import ReportView
from models import utils
from controllers.tournaments import TournamentManager
from controllers.raport import RaportManager
from controllers.player import PlayerManager
import sys


class MenuManager:
    """
    Menu and main functions of menu
    """

    def __init__(self):
        self.view_menu = Menu()
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
        self.tournament_controller = TournamentManager()
        self.report_controller = RaportManager()
        self.report_view = ReportView()
        self.player_controller = PlayerManager()

    def start_main_menu(self):
        # main menu choices
        self.view_menu.title()

        choices = {
            "1": {
                "text": "Créer un tournois",
                "controller": self.tournament_controller.create_tournament,
            },
            "2": {
                "text": "Charger un tournois",
                "controller": self.tournament_controller.resume_tournament,
            },
            "3": {
                "text": "Créer des jouers",
                "controller": self.player_controller.create_player,
            },
            "4": {
                "text": "Modifier un jouer",
                "controller": self.player_controller.update_player_info,
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
                "controller": self.report_controller.display_one_tournament,
                "value": utils.load_tournament(),
            },
            "4": {
                "text": "Tous les joueurs d'un tournois",
                "controller": self.report_controller.display_players_one_tournament,
                "value": utils.load_tournament(),
            },
            "5": {
                "text": "Tous les tours et matches d'un tournois",
                "controller": self.report_controller.rounds_matches,
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
            value = choices[user_input].get("value", None)
            if value:
                choices[user_input]["controller"](value)
            else:
                choices[user_input]["controller"]()
        except KeyError:
            self.view_menu.error_msg()
            self.reports_menu()
        self.report_controller.return_report_menu()

    def exit(self):
        self.view_menu.exit_msg()
        user_input = input().lower()
        match user_input:
            case "oui":
                sys.exit("Vous être sortie du système")
            case "non":
                self.start_main_menu()
            case _:
                self.view_menu.error_msg()
                self.start_main_menu()
    
    
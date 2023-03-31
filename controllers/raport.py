from views.tournament import TournamentView
from views.menu import Menu
from views.report import ReportView
from models.tournament import Tournament


class RaportManager:
    def __init__(self):
        self.tournament_view = TournamentView()
        self.view_menu = Menu()
        self.report_view = ReportView()

    def one_tournament(self, tournaments):
        if len(tournaments) == 0:
            self.tournament_view.no_tournament()
            self.return_menu()
        else:
            self.tournament_view.select_tournament(tournaments)
            self.view_menu.input_prompt()
            user_input = input()

            if user_input == "q":
                self.return_menu()
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

    def rounds_matches(self, tournaments):
        tournament = self.one_tournament(tournaments)
        rounds = tournament.rounds
        self.report_view.title_rounds_matchs_report(tournament)
        self.report_view.display_rounds_matches(tournament, rounds)

    def return_report_menu(self):
        self.report_view.final_menu()
        user_input = input()
        if user_input == "1":
            self.report_menu()
        if user_input == "2":
            self.return_menu()
        else:
            self.view_menu.error_msg

    def return_menu(self):
        from controllers.menu import MenuManager

        MenuManager().start_main_menu()

    def report_menu(self):
        from controllers.menu import MenuManager

        MenuManager().reports_menu()

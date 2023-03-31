from prettytable import PrettyTable


class RoundView:
    def __init__(self):
        self.table = PrettyTable()

        self.round_field_names = [
            "Match #",
            "Nom P1",
            "Score P1",
            " ",
            "Nom P2",
            "Score P2",
        ]

        self.results_field_names = [
            "Classement du tournois",
            "Nom et Prénom",
            "Score finale",
            "Classement global",
        ]

    def round_title(self, tournament, time):
        one = f"\n\nROUND {tournament.current_round}, {time}"
        print(one.center(100, " "), end="\n")

    def display_matches(self, matches):
        """
        @param matches: list of matches tuples
        @return table of matches of the current round
        """
        self.table.clear()
        self.table.field_names = self.round_field_names
        self.table.align = "l"
        for i, match in enumerate(matches):
            name_p1 = f"{match.player_1['Nom']} {match.player_1['Prénom']}"
            name_p2 = f"{match.player_2['Nom']} {match.player_2['Prénom']}"
            score_p1 = 0
            score_p2 = 0
            row = [
                i + 1,
                name_p1,
                score_p1,
                " VS ",
                name_p2,
                score_p2,
            ]
            self.table.add_row(row)
        print(self.table)

    def finish_round(self):
        print("\nVous avez complété ce tour? oui/non", end="\n")
        print("Tapez q pour retourner au menu principal.")

    def scores_options(self, match):
        print("\nMatch: ", match)
        print("1: Jouer 1 gangé")
        print("2: Jouer 2 gagné")
        print("3: Match null")
        print("\nTapez q pour retournez au menu principal")

    def erreur_scores_option(self):
        print("\nVotre choix est invalide, veuillez choisir le bon bon option")

    def winer_1(self, player_1):
        print(f"Player {player_1['Nom']} {player_1['Prénom']} a gagné")

    def display_result(self, tournament):
        self.table.clear()
        self.table.field_names = self.results_field_names
        title = f"RESULTAT de : {tournament.name.upper()} à {tournament.location.title()} {tournament.start_date} - {tournament.end_date}"
        self.table.title = title
        for i in range(len(tournament.players)):
            self.table.add_row(
                [
                    i + 1,
                    tournament.players[i]["Nom"]
                    + " "
                    + tournament.players[i]["Prénom"],
                    tournament.players[i]["Score"],
                    tournament.players[i]["Classement"],
                ]
            )
        print(self.table)

    def offer_ranking(self):
        print("Voulez vous modifier les classements? oui/ non:")

    def rank_confirm(self, p):
        print(
            f"\n\nModifier classement de joueur: {p.last_name.title()} {p.first_name.title()}"
        )
        print("Noveau rank:")

    def update_rank(self):
        print("Classement de joueur est bien modifié. Retourn au menu principal.")

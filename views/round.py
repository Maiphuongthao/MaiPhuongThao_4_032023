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
            "Nom",
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
        for i in range(len(matches)):
            name_p1 = f"{matches[i][0][0]['Nom']} {matches[i][0][0]['Prénom']}"
            name_p2 = f"{matches[i][1][0]['Nom']} {matches[i][1][0]['Prénom']}"
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
        for i in range(len(tournament.players)):
            self.table.add_row(
                {
                    i + 1,
                    tournament.players[i]["Nom"] + tournament.players[i]["Prénom"],
                    tournament.players[i]["Score"],
                    tournament.players[i]["Classement"],
                }
            )
        print("\n---RESULTS---")
        print(f"{tournament.name.upper()}", end="\n")
        print(f"Lieu: {tournament.location.title()}", end="/n")
        print(f"Description: {tournament.description}", end="/n")
        print(
            f"Date de début: {tournament.start_date} | Date de fin: {tournament.end_date}",
            end="/n",
        )
        print(self.table)

    def offer_rankin(self):
        print("Voulez vous modifier les classements? oui/ non:")

    def rank_confirm(self, p):
        print(f"Modifier classement de joueur: {p.lastname} {p.firstname}")
        print("Noveau rank (tapez 'q' pour retourner au menu principal):")

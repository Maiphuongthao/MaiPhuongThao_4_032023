from prettytable import PrettyTable


class RoundView:
    def __init__(self):
        self.table = PrettyTable()

        self.round_field_names = [
            "Match #",
            "Nom P1",
            "Classement P1",
            "Score P1",
            " ",
            "Nom P2",
            "Classement P2",
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

        for i in range(len(matches)):
            name_p1 = f"{matches[i][0][0]['Nom']} {matches[i][0][0]['Prénom']}"
            name_p2 = f"{matches[i][1][0]['Nom']} {matches[i][1][0]['Prénom']}"
            rank_p1 = f"{matches[i][0][0]['Classement']}"
            rank_p2 = f"{matches[i][1][0]['Classement']}"
            score_p1 = f"{matches[i][0][1]}"
            score_p2 = f"{matches[i][1][1]}"
            row = []
            row.insert(0, str(i + 1))
            row.insert(1, name_p1)
            row.insert(2, rank_p1)
            row.insert(3, score_p1)
            row.insert(4, "vs")
            row.insert(5, name_p2)
            row.insert(6, rank_p2)
            row.insert(7, score_p2)

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

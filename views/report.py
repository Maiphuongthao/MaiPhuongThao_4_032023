from prettytable import PrettyTable


class ReportView:
    def __init__(self):
        self.table = PrettyTable()
        self.players_report_feild_names = [
            "Joueur ID",
            "Nom",
            "Prénom",
            "Date de naissance",
            "Scores",
        ]
        self.tournament_report_field_names = [
            "Nom",
            "Location",
            "Description",
            "Date de début",
            "Date de fin",
            "Tour actuel",
            "Jouers",
        ]
        self.match_field_names = [
            "Match #",
            "Nom P1",
            "Score P1",
            " ",
            "Nom P2",
            "Score P2",
        ]

    def report_title(self):
        print("\n\n---RAPPORTS---")

    def report_menu(self, choices):
        for choice in choices:
            print(choice, choices[choice]["text"])

    def display_players(self, players):
        self.table.clear()
        self.table.field_names = self.players_report_feild_names
        self.table.align = "l"
        for i in range(len(players)):
            self.table.add_row(
                [
                    players[i]["Joueur_id"],
                    players[i]["Nom"],
                    players[i]["Prénom"],
                    players[i]["Date de naissance"],
                    players[i]["Score"],
                ]
            )
        self.table.sortby = "Nom"
        print("\n---JOUEURS AVEC LES NOMS TRIES PAR ORDRE ALPHABETIQUE---")
        print(self.table)

    def display_all_tournaments(self, tournaments):
        self.table.clear()
        self.table.field_names = self.tournament_report_field_names
        self.table.align = "l"

        for i in range(len(tournaments)):
            players_in_tournament = []
            players = tournaments[i]["List des joueurs"]
            for p in range(len(players)):
                name = f"{players[p]['Prénom']} {players[p]['Nom']}"
                players_in_tournament.append(name)
            players_for_table = "\n".join(players_in_tournament)
            self.table.add_row(
                [
                    tournaments[i]["Nom"],
                    tournaments[i]["Lieu"],
                    tournaments[i]["Description"],
                    tournaments[i]["Date de début"],
                    tournaments[i]["Date de fin"],
                    str(tournaments[i]["Tour actuel"] - 1)
                    + "/"
                    + str(tournaments[i]["Nombre de tours"]),
                    players_for_table,
                ]
            )
        print("\n\n---LES TOURNOIS---")
        print(self.table)

    def display_one_tournament(self, tournament):
        self.table.clear()
        self.table.field_names = ["Nom", "Date de début", "Date de fin"]
        self.table.align = "l"
        self.table.add_row(
            [tournament.name, tournament.start_date, tournament.end_date]
        )
        print(f"\n\n---{tournament.name.upper()}---")
        print(self.table)

    def display_players_one_tournament(self, tournament):
        players = tournament.players
        self.display_one_tournament(tournament)
        print("\n---ET---")
        self.display_players(players)

    def display_rounds_matches(self, tournament, rounds):
        self.display_one_tournament(tournament)
        print("\n")
        print(f"\n---LES TOURS DE {tournament.name.upper()} ")
        self.display_rounds(rounds)
        print("\n")
        for i in range(len(rounds)):
            matches = rounds[i]["List des matchs"]
            print(f"---LES MATCHES DE {rounds[i]['Nom'].upper()}")
            self.display_matches(matches)
            print("\n")

    def display_rounds(self, rounds):
        self.table.clear()
        self.table.field_names = ["Nom", "Date de début", "Date de fin"]
        self.table.align = "l"
        for round in rounds:
            self.table.add_row(
                [round["Nom"], round["Date de début"], round["Date de fin"]]
            )
        print(self.table)

    def display_matches(self, matches):
        self.table.clear()
        self.table.field_names = self.match_field_names
        self.table.align = "l"
        for i in range(len(matches)):
            name_p1 = f"{matches[i][0][0]['Nom']} {matches[i][0][0]['Prénom']}"
            name_p2 = f"{matches[i][1][0]['Nom']} {matches[i][1][0]['Prénom']}"
            score_p1 = f"{matches[i][0][1]}"
            score_p2 = f"{matches[i][1][1]}"
            row = [
                i + 1,
                name_p1,
                score_p1,
                " vs ",
                name_p2,
                score_p2,
            ]
            self.table.add_row(row)
        print(self.table)

    def final_menu(self):
        print("\n Voulez vous retourner au:", end="\n")
        print("1: Menu des raports")
        print("2: Menu principal")

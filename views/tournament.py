class TournamentView:
    def __init__(self) -> None:
        pass

    def tournament_title(self):
        print("\n\n\nNOUVEAU TOURNAMENT")

    def review_tournament(self, info, players):
        print(f"Nouveau tournament: {info[0].upper()}", end="\n")
        print(f"Lieu: {info[1]} | Description: {info[2]}", end=" | ")
        print(f"Date de début: {info[3]} | Tour: {info[4]}", end="\n")
        print("Les joueurs:")
        for p in players:
            print(f"Player {players.index(p) + 1} : [{p['Joueur_id']}]", end=" | ")
            print(f"{p['Nom']} {p['Prénom']}", end=" | ")
            print(f"{p['Date de naissance']}", end=" | ")
            print(f"Classement: {p['Classement']}")
        print("\nEnregistrer ces informations? (oui/ non)")

    def tournament_saved(self):
        print("Le tournois est créé")

    def start_tournament_question(self):
        print("Commencez le tournois maintenant? (oui/ non)")

    def select_tournament(self, tournaments):
        print("\n\nSELECT TOURNAMENT\n")
        for t in range(len(tournaments)):
            print(f"{tournaments[t]['id']}: {tournaments[t]['Nom']}", end=" | ")
            print(
                f"{tournaments[t]['Lieu']} | {tournaments[t]['Description']}",
                end=" | ",
            )
            print(
                f"Date de début: {tournaments[t]['Date de début']} | Date de fin: {tournaments[t]['Date de fin']}",
                end=" | ",
            )
            print(
                f"{tournaments[t]['Tour actuel'] - 1} sur {tournaments[t]['Nombre de tours']} tours",
                end="\n",
            )
        print("Tapez q pour retourner au menu principal")

    def no_tournament(self):
        print("\nAucun tournois est enregistré.")

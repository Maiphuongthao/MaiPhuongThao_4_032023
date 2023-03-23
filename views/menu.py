from .ascii_chess import chess_tournaments_ascii


class Menu:
    def __init__(self) -> None:
        pass

    def title(self):
        print(chess_tournaments_ascii)

    def main_menu(self, choices):
        for choice in choices:
            print(choice, choices[choice]["text"])

    def input_prompt(self):
        print("\nSelectionnez votre choix: ")

    def tournament_title(self):
        print("\n\n\nNOUVEAU TOURNAMENT")

    def review_tournament(self, info, players):
        print(
            f"Nouveau tournament: {info[0].upper()}, à {info[1]}\nDescription: {info[2]}\nCommence le: {info[3]}\nTour: {info[4]}\nJouers:\n"
        )
        for p in players:
            players_details = f"Player{players.index(p) + 1}:{p['player_id']} | {p['firstname']} {p['lastname']} | {p['birthday']} | Rang: {p['rank']}"
            print(players_details)
        print("\nEnregistrer ces informations? (oui/ non)")

    def player_selected_error(self):
        print(
            "Ce jouer est selectionné ou n'existe pas, veuillez choisir un autre jouer ou créer un nouveau",
            end="\n",
        )
        print("1: Choisir un autre jouer", end="\n")
        print("2: Créer un nouveau jouer")

    def tournament_saved(self):
        print("Le tournois est créé")

    def start_tournament_question(self):
        print("Commencez le tournois maintenant? (oui/ non)")

    def create_player_title(self):
        print("\n\n\nNOUVEAU JOUER")

    def total_players_prompt(self, players_total, players_needed):
        print(
            f"il y a que {players_total} jouer(s) dans la list. Veuillez ajouter {players_needed - players_total} jouers."
        )

    def review_player(self, info):
        print("\nNouveau jouer est créé\n")
        print(f"{info[1]}, {info[2]} - {info[0]}", end="\n")
        print(f"Née le: {info[3]}", end="\n")
        print(f"Rang: {info[4]}", end="\n")
        print("Vous voulez ajouter ce jouer? [oui/ non]", end="\n")

    def player_saved(self):
        print("\nJouer est bien enregistré")

    def select_a_player(self, players, number_player):
        """
        Display the player
        """
        print(f"\nChoisir le jouer: {number_player}")
        # breakpoint()
        for p in range(len(players)):
            print(f"{players[p]['id']} : [{players[p]['player_id']}]", end=" - ")
            print(f"{players[p]['firstname']} {players[p]['lastname']}", end=" | ")
            print(f"Rang : {players[p]['rank']}")
        print("\nEntrez q pour retourner au menu principal")

    def update_player_info(self, player, info):
        """
        display player info that is changed
        """
        print("\nModifier l'information de jouer\n")
        print(f"Jouer modifié: {player.first_name} {player.last_name}", end="\n")
        for i in range(len(info)):
            print(f"{i+1}: modifié {info[i]}")
        print("\nTapez q pour retournez au menu principal.")

    def exit_msg(self):
        print("\nEtês vous sûr de vouloir quitter ce programme? oui/non")

    def error_msg(self):
        print("\nVotre choix n'est pas valide. le sytème retourner au menu principal ")

    def input_prompt_text(self, option):
        print(f"\nEntrez {option} (tapez q pour retourner au menu principal) : ")

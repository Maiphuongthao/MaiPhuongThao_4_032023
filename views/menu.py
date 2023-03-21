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

    def create_player_title(self):
        print("\n\n\nNOUVEAU JOUER")

    def review_player(self, info):
        print("\nNouveau jouer est créé\n")
        print(f"{info[1]}, {info[2]} - {info[0]}", end="\n")
        print(f"Née le: {info[3]}", end="\n")
        print(f"Rang: {info[4]}", end="\n")
        print("Vous voulez ajouter ce jouer? [oui/ non]", end="\n")

    def player_saved(self):
        print("\nJouer est bien enregistré")
    
    def select_a_player(self, players):
        """
        Display the player
        """
        print("\nChoisir le jouer:")
        # breakpoint()
        for i, player in enumerate(players):
            print(f"{i + 1} : [{players[i]['player_id']}]", end=" - ")
            print(
                f"{players[i]['firstname']} {players[i]['lastname']}", end=" | "
            )
            print(f"Rang : {players[i]['rank']}")
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

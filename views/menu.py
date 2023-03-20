from .ascii_chess import chess_tournaments_ascii


class Menu:
    def __init__(self) -> None:
        pass

    def title(self):
        print(chess_tournaments_ascii)

    def main_menu(self, choices):
        for choice in choices:
            print(choice, choices[choice].text)

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
        for player in range(len(players)):
            print(f"[{players[player]['id']}]", end=" - ")
            print(
                f"{players[player]['first_name']}, {players[i]['last_name']}", end="\n"
            )
            print(f"Rang : {players[player]['rank']}")
        print("\nTapez 5 pour retourner au menu principal")

    def update_player_info(player, info):
        """
        display player info that is changed
        """
        print("\nModifier l'information de jouer\n")
        print(f"Jouer modifié: {player.first_name} {player.last_name}", end="\n")
        for i in range(len(info)):
            print(f"{i+1} modifié {info[i]}")
        print("\nTapez 5 pour retournez au menu principal.")

    def exit_msg(self):
        print("\nEtês vous sûr de vouloir quitter ce programme? oui/non")

    def error_msg(self):
        print("\nVeuillez entrez un choix valide: ")

    def input_prompt_text(self, option):
        print(f"\nEntrez {option} (tapez 5 pour retourner au menu principal) : ")

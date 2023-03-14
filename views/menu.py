from .ascii_chess import chess_tournaments_ascii


class Menu:
    def __init__(self) -> None:
        pass

    def title(self):
        print(chess_tournaments_ascii)

    def main_menu(self):
        print("\n\n0: Créer un tournoi")
        print("1: Charger un tournois  ")
        print("2: Créer des jouers ")
        print("3: Rapports ")
        print("4: Quitter ")

    def input_prompt(self):
        print("\nSelectionnez votre choix: ")

    def tournament_title(self):
        print("\n\n\n NEW TOURNAMENT")

    def exit_msg(self):
        print("\nEtês vous sûr de vouloir quitter ce programme? y/n")

    def error_msg(self):
        print("\nVeuillez entrez un choix valide: ")

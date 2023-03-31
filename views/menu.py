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
        print("\nSelectionnez votre choix:")

    def player_selected_error(self):
        print(
            "Ce jouer est selectionné ou n'existe pas, veuillez choisir un autre jouer ou créer un nouveau",
            end="\n",
        )
        print("1: Choisir un autre jouer", end="\n")
        print("2: Créer un nouveau jouer")

    def exit_msg(self):
        print("\nEtês vous sûr de vouloir quitter ce programme? oui/non")

    def error_msg(self):
        print("\nVotre choix n'est pas valide. le sytème retourner au menu principal ")

    def input_prompt_text(self, option):
        print(f"\nEntrez {option} (tapez q pour retourner au menu principal) : ")

    def not_valide(self):
        print("\nVotre choix n'est pas valide. Veuillez choisir un bon option: ")

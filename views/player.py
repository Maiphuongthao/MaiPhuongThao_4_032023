class PlayerView:
    def __init__(self) -> None:
        pass

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
            print(f"{players[p]['id']} : [{players[p]['Joueur_id']}]", end=" - ")
            print(f"{players[p]['Prénom']} {players[p]['Nom']}", end=" - ")
            print(f"Classement : {players[p]['Classement']}")
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

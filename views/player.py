class PlayerView:
    def __init__(self) -> None:
        pass

    def create_player_title(self):
        print("\n\n---NOUVEAU JOUER---")

    def total_players_prompt(self, players_total, players_needed):
        print(f"Il y a que {players_total} jouer(s) dans la list")
        print(f"Veuillez ajouter {players_needed - players_total} joueurs")

    def review_player(self, info):
        print("\nNouveau jouer est créé\n")
        print(f"[{info[0]}], {info[1]} {info[2]}", end="\n")
        print(f"Née le: {info[3]}", end="\n")
        print("Vous voulez ajouter ce jouer? [oui/ non]", end="\n")

    def player_saved(self):
        print("\nJouer est bien enregistré")

    def select_a_player(self, players, number_player):
        """
        Display the players
        """
        print(f"\n\n\n---Choisir le jouer: {number_player} ---", end="\n")
        for p in range(len(players)):
            print(f"{players[p]['id']} : [{players[p]['Joueur_id']}]", end=" - ")
            print(
                f"{players[p]['Nom'].title()} {players[p]['Prénom'].title()}", end="\n"
            )
        print("\nSélectionnez votre choix ou 'q' pour retournez au menu principal:")

    def update_player_info(self, player, info):
        """
        display player info that is changed
        """
        print("\n\n---MODIFIER L'INFORMATION DE JOUEUR---\n")
        print(
            f"Jouer choisi: {player.first_name} {player.last_name}",
            end=" | ",
        )
        print(f"{player.birthday}", end="\n")
        for i in range(len(info)):
            print(f"{i+1}: modifié {info[i]}")
        print("\nSélectionnez votre choix ou 'q' pour retournez au menu principal:")

from views.menu import Menu
from models.player import Player


class MenuManager:
    def __init__(self):
        self.view_menu = Menu()

    def exit_option(self):
        self.view_menu.exit_msg()
        user_input = input().lower()
        match user_input:
            case "oui":
                exit()
            case "non":
                self.start_main_menu()
            case _:
                self.view_menu.error_msg()
                self.exit_option()

    def start_main_menu(self):
        """
        Selections of main menu
        """

        choices = {
            "1": {"text": "Créer un tournois", "controller": self.create_tournament()},
            "2": {
                "text": "Charger un tournois",
                "controller": self.resume_tournament(),
            },
            "3": {"text": "Créer des jouers", "controller": self.create_player()},
            "4": {"text": "Rapports", "controller": self.reports_menu()},
            "5": {"text": "Quitter", "controller": self.exit_option()},
        }

        self.view_menu.main_menu(choices)
        self.view_menu.input_prompt()
        user_input = input()
        try:
            choices[user_input].controller()
        except KeyError:
            self.view_menu.error_msg()
            self.start_main_menu()

    def create_tournament(self):
        pass

    def reports_menu(self):
        pass

    def resume_tournament(self):
        pass

    """def create_tournament(self):
       
        #Create a new tournament, serialized it and import to db
     
        self.view_menu.tournament_title()
        tournament_info = []
        options = ["name", "location", "description"]
        for op in options:
            self.view_menu.input_prompt_text()
            user_input = input()
            if user_input == "5":
                self.start_main_menu()
            else:
                tournament_info.append(user_input)
        
    """

    def create_player(self):
        self.view_menu.create_player_title()
        player_infos = []
        info_values = ["Jouer id", "Prénom", "Nom", "Naissance (dd/mm/yyy)", "rang"]
        for i in info_values:
            self.view_menu.input_prompt_text(i)
            user_input = input()
            if user_input == "5":
                self.start_main_menu()
            else:
                player_infos.append(user_input)
        self.view_menu.review_player(player_infos)
        user_input = input().lower()
        match user_input:
            case "oui":
                player = Player(
                    player_id=player_infos[0],
                    first_name=player_infos[1],
                    last_name=player_infos[2],
                    birthday=player_infos[3],
                    rank=int(player_infos[4]),
                )
                player.save_player_data()
                self.view_menu.player_saved()
                self.start_main_menu()
            case "non":
                self.start_main_menu()
            case _:
                self.view_menu.error_msg()
                self.exit_option()

    def update_player_info(self):
        """
        update existing player's infos
        load player data and get selected player
        chose the option that need to be changed
        """
        players = Player.load_players_data()
        self.view_menu.select_a_player(players)
        self.view_menu.input_prompt()
        user_input = input()
        if user_input == "5":
            self.start_main_menu()

        p = players(int(user_input - 1))
        p = Player(
            p["player_id"], p["first_name"], p["last_name"], p["birthday"], p["rank"]
        )

        input_values = ["prénom", "nom", "date de naissance", "rang"]
        self.view_menu.update_player_info(p, input_values)
        self.view_menu.input_prompt()
        user_input = input()

        if user_input == "5":
            self.start_main_menu()

        elif int(user_input) <= len(input_values):
            update_info = input_values[int(user_input) - 1]
            key = ["first_name", " last_name", " birthday", "rank"]

            self.view_menu.input_prompt_text(f"nouveau {update_info}")
            user_input = input()

            if user_input == "5":
                self.start_main_menu()
            else:
                updated_info = key[int(user_input) - 1]
                p.update_player(user_input, updated_info)
                self.view_menu.player_saved()
                self.update_player_info()

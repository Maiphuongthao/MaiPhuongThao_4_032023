from views.menu import Menu


class MenuController:
    def __init__(self):
        self.view_menu = Menu()

    def start_main_menu(self):
        """
        Selections of main menu
        """

        self.view_menu.main_menu()
        self.view_menu.input_prompt()
        user_input = int(input())

        match user_input:
            case 0:
                self.create_tournament()
            case 1:
                self.resume_tournament()
            case 3:
                self.create_players()
            case 4:
                self.reports_menu()
            case 5:
                self.view_menu.exit_msg()
                user_input = input().lower()
                match user_input:
                    case "y":
                        exit()
                    case "n":
                        self.start_main_menu()
            case _:
                self.view_menu.error_msg()
                self.start_main_menu()
    
    def create_tournament(self):
        """
        Create a new tournament, serialize it
        """
        self.view_menu.tournament_title()
        tournament_info = []
        
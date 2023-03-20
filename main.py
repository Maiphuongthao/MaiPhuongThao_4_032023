from controllers.menu import MenuManager
from views.menu import Menu


def main():
    menu_title = Menu()
    start_menu = MenuManager()
    menu_title.title()
    start_menu.start_main_menu()


if __name__ == "__main__":
    main()

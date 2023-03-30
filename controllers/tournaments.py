from views.round import RoundView
from views.menu import Menu
from views.tournament import TournamentView
from models.round import Round
from models.match import Match
from models.tournament import Tournament
from models.player import Player
from models import utils
from operator import itemgetter
from controllers.player import PlayerManager
from controllers.raport import RaportManager


class TournamentManager:
    def __init__(self):
        self.round_view = RoundView()
        self.view_menu = Menu()
        self.tournament_view = TournamentView()
        self.player_controller = PlayerManager()
        self.report_controller = RaportManager()

    def create_tournament(self):
        """------------- create a tournament and save it to db -----------------"""
        self.tournament_view.tournament_title()
        tournament_info = []
        infos = [
            "Nom",
            "Lieu",
            "Description",
            "Date de debut",
            "Nombre des jouers (8 par default))",
            "Nombre de tour (4 par default)",
        ]
        for info in infos:
            self.view_menu.input_prompt_text(info)
            user_input = input()
            if user_input == "q":
                self.back_to_menu()
            else:
                tournament_info.append(user_input)
        # check if the input has no return values, return value by default where it isn't
        if tournament_info[3] == "":
            tournament_info[3] = utils.set_date_time()
        if tournament_info[4] == "":
            tournament_info[4] = int(8)
        if tournament_info[5] == "":
            tournament_info[5] = int(4)

        # select players and add to players lists. Min 8 players as min 4 tours to begin a tournament
        tour_players = self.player_controller.select_players(tournament_info[4])
        self.tournament_view.review_tournament(tournament_info, tour_players)
        user_input = input().lower()
        if user_input == "non":
            self.back_to_menu()
        elif user_input == "oui":
            tournament = Tournament(
                name=tournament_info[0],
                location=tournament_info[1],
                start_date=tournament_info[3],
                end_date="TBD",
                rounds=[],
                players=tour_players,
                current_round=1,
                description=tournament_info[2],
                number_of_rounds=tournament_info[5],
            )
            serialized_data = tournament.get_serialized_tournaments()
            # Save tournament to json file
            utils.save_data_db("tournaments.json", serialized_data)
            self.tournament_view.tournament_saved()
            # Check if user want to start the tournament
            self.tournament_view.start_tournament_question()
            user_input = input()
            if user_input == "oui":
                self.start_tournament(tournament)
            elif user_input == "non":
                self.back_to_menu()
            else:
                self.view_menu.error_msg()
                self.back_to_menu()
        else:
            self.view_menu.error_msg()
            self.create_tournament()

    def resume_tournament(self):
        """-------------------- Select the tournament to be resume and start its rounds ----------"""
        tournament_data = utils.load_tournament()
        tournament = self.report_controller.one_tournament(tournament_data)
        self.start_tournament(tournament)

    def continue_rounds(self, tournament):
        """----------- while the current round doesnt reach to and end then continue ------------"""
        while tournament.current_round <= tournament.number_of_rounds:
            self.next_round(tournament)
            tournament.current_round += 1
            tournament.update_tournament()

    def start_tournament(self, tournament):
        """------------ if its 1st round, then add 1 to the current round incase resuming  ----------
        ------------ then continue it until playing and updating untill the end of rounds -------
        """
        if tournament.current_round == 1:
            self.first_round(tournament)
            tournament.current_round += 1
            tournament.update_tournament()
            self.continue_rounds(tournament)
        elif 1 < tournament.current_round <= tournament.number_of_rounds:
            self.continue_rounds(tournament)
            tournament.end_date = utils.set_date_time()
            self.tournament_end(tournament)
        elif tournament.current_round > tournament.number_of_rounds:
            self.tournament_end(tournament)
        # message erreur here

    def play_tour(self, tournament, round):
        """
        -------------- show the matches of the round and ask if
        its finished and add it to list of rounds of tournament ------
        """
        self.round_view.round_title(tournament, round.start_date)
        self.round_view.display_matches(round.matches)
        self.round_view.finish_round()
        user_input = input().lower()
        scores_list = []

        match user_input:
            case "oui":
                round.end_date = utils.set_date_time()
                tournament.rounds.append(self.set_round(round))

                self.end_of_round(tournament)

            case "non":
                self.first_round(tournament)
            case "q":
                self.back_to_menu()
            case _:
                self.view_menu.error_msg()
                self.start_tournament(tournament)

    def first_round(self, tournament):
        """
        --------create and play the 1st round-------
        """
        matches = self.initialize_starting_pairs(tournament)
        round = Round(
            "Tour 1",
            utils.set_date_time(),
            "TBD",
            matches,
        )
        self.play_tour(tournament, round)

    def initialize_starting_pairs(self, tournament):
        """
        ---------- Create matches for 1st round---------------
        devide the players len in half and get top and bottom players
        matches then in random way no need correct index
        @return: matches to be used for 1st round
        """
        number_of_pairs = len(tournament.players) // 2
        top_players = tournament.players[number_of_pairs:]
        bottom_players = tournament.players[:number_of_pairs]
        matches = []

        for i in range(number_of_pairs):
            m = Match(
                top_players[i],
                bottom_players[i],
                top_players[i]["Score"],
                bottom_players[i]["Score"],
            )
            self.add_play_with(top_players[i], bottom_players[i])
            pairs = m.set_pairs()

            matches.append(pairs)

        return matches

    def next_round(self, tournament):
        """
        ---------- Create and play the next rounds--------
        """
        matches = self.initialize_pairs(tournament)
        round = Round(
            ("Tour " + str(tournament.current_round)),
            utils.set_date_time(),
            "TBD",
            matches,
        )

        self.play_tour(tournament, round)

    def initialize_pairs(self, tournament):
        """
        -------------Create matches for next rounds-----------
        1st list= list of tournaments players which is updated from each played rounds
        sort it by score
        2nd list: get emply list to add chosen players from the above list
        match player as: 1-2 if 2 is in play_with od 1, then chekc 1-3
        """
        sorted_players = []
        matches = []
        flatten_players = tournament.players

        flatten_players.sort(key=itemgetter("Score"), reverse=True)
        for player_1 in flatten_players:
            if player_1 in sorted_players:
                continue
            else:
                try:
                    player_2 = flatten_players[flatten_players.index(player_1) + 1]
                except IndexError:
                    break
            while player_2["Joueur_id"] in player_1["play_with"]:
                try:
                    player_2 = flatten_players[flatten_players.index(player_2) + 1]
                except IndexError:
                    break
            else:
                m = Match(player_1, player_2, player_1["Score"], player_2["Score"])
                self.add_play_with(player_1, player_2)
                pairs = m.set_pairs()
                sorted_players.append(player_1)
                sorted_players.append(player_2)
                matches.append(pairs)
        return matches

    def add_play_with(self, player1, player2):
        """---------add opponents of players------"""
        player1["play_with"].append(player2["Joueur_id"])
        player2["play_with"].append(player1["Joueur_id"])

    def get_round_matches(self, tournament):
        """-----return matches of all rounds------"""
        matches = []
        for i in range(len(tournament.rounds)):
            for match in tournament.rounds[i]["List des matchs"]:
                matches.append(match)
        return matches

    def set_round(self, round):
        return round.get_serialized_round()

    def end_of_round(self, tournament):
        for i in range(tournament.number_of_rounds):
            self.round_view.scores_options(i + 1)
            matches = tournament.rounds[i]["List des matchs"]
            for m in range(len(matches)):
                player1 = matches[m][0][0]
                player2 = matches[m][1][0]
                score_player1 = matches[m][0][1]
                score_player2 = matches[m][1][1]

                self.score_options(player1, player2, score_player1, score_player2)
                breakpoint()

        # tournament.players = self.update_scores_player(
        #     tournament.players, matches_players
        # )

    # def update_scores_player(self, players, matches_players):
    #     for p in matches_players:
    #         noveau_score = p["Score"] + players[players.index(p)]["Score"]
    #         players[players.index(p)]["Score"] = noveau_score
    #     return players

    # def update_scores(self, matches, score):
    #     for score in matches:
    #         for i in range(len(score)):
    #             score[i][1] = score
    #     return score

    def score_options(self, player1, player2, score_player1, score_player2):
        res = input()
        match res:
            case "1":
                player1["Score"] += 1.0
                score_player1 += 1.0
            case "2":
                player2["Score"] += 1.0
                score_player2 += 1.0

            case "3":
                player1["Score"] += 0.5
                score_player1 += 0.5
                player1["Score"] += 0.5
                score_player1 += 0.5

            case "q":
                self.back_to_menu()
            case _:
                self.round_view.erreur_scores_option()
                self.score_options(player1, player2, score_player1, score_player2)

    def tournament_end(self, tournament):
        """
        -----display final result of the tournament----
        offer user to update rank
        """
        players = tournament.players
        players.sort(key=itemgetter("Score"), reverse=True)
        self.round_view.display_result(tournament)
        self.round_view.offer_rankin()
        user_input = input().lower()
        try:
            if user_input == "oui":
                self.update_rank(players)
            elif user_input == "non":
                self.back_to_menu()
        except KeyError:
            self.view_menu.error_msg()
            self.back_to_menu()

    def update_rank(self, players):
        """-----update players rank---------"""
        self.player_controller.select_players(players, "to update")
        self.view_menu.input_prompt()
        user_input = input()
        if user_input == "q":
            self.back_to_menu()
        for i in range(len(players)):
            if int(user_input) == players[i]["Joueur_id"]:
                player = players[players.index(players[i])]
                player = Player(
                    player["Joueur_id"],
                    player["Nom"],
                    player["Prénom"],
                    player["Date de naissance"],
                )
                self.round_view.rank_confirm(player)
                user_input = input()
                if user_input == "non":
                    self.back_to_menu()
                elif user_input == "oui":
                    player.update_player(int(user_input), "Classement")
                    players[i]["Classement"] = int(user_input)
                    return players

    def back_to_menu(self):
        from controllers.menu import MenuManager

        MenuManager().start_main_menu()

from views.menu import Menu
from views.round import RoundView
from models.round import Round
from models.match import Match
from models.player import Player
from models.utils import set_date_time
from operator import attrgetter


class TournamentManager:
    MATCHS_PLAYED = []

    def __init__(self):
        self.view_menu = Menu()
        self.round_view = RoundView()

    def start_tournament(self, tournament):
        if tournament.current_round == 1:
            self.first_round(tournament)
            tournament.current_round += 1
            tournament.update_tournament()
            self.next_round(tournament)
        elif 1 < tournament.current_round <= tournament.number_of_rounds:
            while tournament.current_round <= tournament.number_of_rounds:
                self.next_round(tournament)
                tournament.current_round += 1
            tournament.end_date = set_date_time()
            tournament.update_tournament("Date de début", tournament.end_date)
            self.tournament_end(tournament)
        elif tournament.current_round > tournament.number_of_rounds:
            self.tournament_end(tournament)
        # message erreur here

    def first_round(self, tournament):
        matches = self.initialize_starting_pairs(tournament)
        round = Round(
            "Tour 1",
            set_date_time(),
            "TBD",
            matches,
        )

        self.round_view.round_title(tournament, round.start_date)
        self.round_view.display_matches(round.matches)
        self.round_view.finish_round()
        user_input = input().lower()

        match user_input:
            case "oui":
                round.end_date = set_date_time()
                tournament.rounds.append(self.set_round(round))
                self.end_of_round(tournament, round)

            case "non":
                self.first_round()
            case "q":
                self.view_menu.main_menu()
            case _:
                self.view_menu.error_msg()
                self.view_menu.main_menu()

    def next_round(self, tournament):
        round = Round(
            ("Tour " + str(tournament.current_round)),
            set_date_time(),
            "TBD",
        )
        pass

    def initialize_starting_pairs(self, tournament):
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
            self.MATCHS_PLAYED.append({top_players[i], bottom_players[i]})
            pairs = m.set_pairs()
            matches.append(pairs)

        return matches

    def initialize_pairs(self, tournament):
        sorted_players_by_score = []
        sorted_player_flat = []
        match_to_try = set()

        for round in tournament.rounds:
            for player in round.matches:
                sorted_players_by_score.append(player)

        for player in sorted_players_by_score:
            player.pop()
            sorted_player_flat.append(player[0])

        sorted_player_flat.sort(key=attrgetter("Score", "Classement"), reverse=True)
        sorted_players_by_score.clear()

        for player_1 in sorted_player_flat:
            if player_1 in sorted_players_by_score:
                continue
            else:
                try:
                    player_2 = sorted_player_flat[
                        sorted_player_flat.index(player_1) + 1
                    ]
                except IndexError:
                    break
            match_to_try.add(player_1)
            match_to_try.add(player_2)

            while match_to_try in self.MATCHS_PLAYED:
                match_to_try.remove(player_2)
                try:
                    player_2 = sorted_player_flat[
                        sorted_player_flat.index(player_2) + 1
                    ]
                except IndexError:
                    break
                match_to_try.add(player_2)
                continue
            else:
                sorted_players_by_score.append(player_1)
                sorted_players_by_score.append(player_2)
                sorted_player_flat.pop(sorted_player_flat.index(player_2) + 1)
                self.MATCHS_PLAYED.append({player_1, player_2})
                match_to_try.clear()
        return sorted_players_by_score

    def set_round(self, round):
        return round.get_serialized_round()

    def end_of_round(self, tournament, round):
        score_list = []
        for i in range(tournament.number_of_rounds):
            self.round_view.scores_options(i + 1)
            self.score_options(score_list)
        tournament.players = self.update_scores(tournament.players, score_list)

    def update_scores(self, players, score_list: list):
        for i in range(len(players)):
            players[i]["Score"] += score_list[i]
        return players

    def score_options(self, score_list):
        res = input()
        match res:
            case "1":
                score_list.extend([1.0, 0.0])
            case "2":
                score_list.extend([0.0, 1.0])
            case "3":
                score_list.extend([0.5, 0.5])
            case "q":
                self.view_menu.main_menu()
            case _:
                self.round_view.erreur_scores_option()
                self.score_options(score_list)

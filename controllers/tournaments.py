from views.menu import Menu
from views.round import RoundView
from models.round import Round
from models.match import Match
from models.player import Player
from models.utils import set_date_time, save_data_db
from operator import itemgetter


class TournamentManager:
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
                tournament.update_tournament()
            tournament.end_date = set_date_time()
            self.tournament_end(tournament)
        elif tournament.current_round > tournament.number_of_rounds:
            self.tournament_end(tournament)
        # message erreur here

    def play_tour(self, tournament, round):
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

    def first_round(self, tournament):
        matches = self.initialize_starting_pairs(tournament)
        round = Round(
            "Tour 1",
            set_date_time(),
            "TBD",
            matches,
        )

        self.play_tour(tournament, round)

    def next_round(self, tournament):
        matches = self.initialize_pairs(tournament)
        round = Round(
            ("Tour " + str(tournament.current_round)), set_date_time(), "TBD", matches
        )

        self.play_tour(tournament, round)

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
            pairs = m.set_pairs()
            matches.append(pairs)
        return matches

    def initialize_pairs(self, tournament):
        sorted_players = []
        flatten_players = self.get_flatten_players(tournament)
        match_to_try = set()
        matches_played = self.get_matches_played(tournament)

        flatten_players.sort(key=itemgetter("Score", "Classement"), reverse=True)
        for player_1 in flatten_players:
            if player_1 in sorted_players:
                continue
            else:
                try:
                    player_2 = flatten_players[flatten_players.index(player_1) + 1]
                except IndexError:
                    break
            unserilized_player_1 = self.unserialized_player(player_1)
            unserialized_player_2 = self.unserialized_player(player_2)
            match_to_try.add(unserilized_player_1)
            match_to_try.add(unserialized_player_2)
            while match_to_try in matches_played:
                match_to_try.remove(unserialized_player_2)
                try:
                    player_2 = flatten_players[flatten_players.index(player_2) + 1]
                    match_to_try.add(unserialized_player_2)
                except IndexError:
                    break
               
            else:
                new_match = [
                    (player_1, player_1["Score"]),
                    (player_2, player_2["Score"]),
                ]
                sorted_players.append(new_match)
                match_to_try.clear()
        return sorted_players

    def get_matches_played(self, tournament):
        matches_played = []
        for round in tournament.rounds:
            for match in round["List des matchs"]:
                player_1 = self.unserialized_player(match[0][0])
                player_2 = self.unserialized_player(match[1][0])
                matches_played.append({player_1, player_2})
        return matches_played

    def get_flatten_players(self, tournament):
        flatten_players = []
        for round in tournament.rounds:
            for match in round["List des matchs"]:
                for player in match:
                    flatten_players.append(player[0])
        return flatten_players

    def unserialized_player(self, serialized_player):
        player_id = serialized_player["Joueur_id"]
        last_name = serialized_player["Nom"]
        first_name = serialized_player["Prénom"]
        birth_day = serialized_player["Date de naissance"]
        rank = serialized_player["Classement"]
        scores = serialized_player["Score"]
        id = serialized_player["id"]
        return (player_id, last_name, first_name, birth_day, rank, scores, id)

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

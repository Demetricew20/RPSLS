from players import *
from gesture import *
from UI import user_interface


class Score:
    def __init__(self, player1_wins, player2_wins, cpu_wins, tie_count):
        self.player1_wins = player1_wins
        self.player2_wins = player2_wins
        self.cpu_wins = cpu_wins
        self.tie_count = tie_count

    def scoring_dictionary(self, mode_selected, player1, player2, cpu):
        gestures_dict = gestures.gestures_dict
        if player1.gesture == cpu.gesture or player1.gesture == player2.gesture:
            print('It is a tie!')
            self.tie_count += 1
            return
        for key in gestures_dict:
            if player1.gesture == key:
                if cpu.gesture in gestures_dict[key] or player2.gesture in gestures_dict[key]:
                    user_interface.round_winner(player1)
                    self.player1_wins += 1
                    return
                else:
                    Score.cpu_and_player2_scores(self, mode_selected, player2, cpu)
                    return

    def cpu_and_player2_scores(self, mode_selected, player2, cpu):
        if mode_selected == 'Single-Player':
            self.cpu_wins += 1
            user_interface.round_winner(cpu)
        elif mode_selected == 'Multi-Player':
            self.player2_wins += 1
            user_interface.round_winner(player2)

    def score_tracker(self):
        # Loop Through Players & Player wins
        tracker = [self.player1_wins, self.player2_wins, self.cpu_wins]
        if self.tie_count == 2:
            print('Game has ended in a tie!')
        for i in range(0, len(tracker)):
            if tracker[i] == 2:
                user_interface.game_winner(list_of_players[i])
                return


score = Score(0, 0, 0, 0)

from players import player_list
from gesture import *


class Score:
    def __init__(self, player1_wins, player2_wins, cpu_wins, tie_count):
        self.player1_wins = player1_wins
        self.player2_wins = player2_wins
        self.cpu_wins = cpu_wins
        self.tie_count = tie_count
        self.tracker = [self.player1_wins, self.player2_wins, self.cpu_wins]

    def scoring_dictionary(self, mode_selected, player1, player2, cpu):
        gestures_dict = gestures.gestures_dict
        if player1.gesture == cpu.gesture or player1.gesture == player2.gesture:
            print('It is a tie!')
            self.tie_count += 1
            return
        for key in gestures_dict:
            if player1.gesture == key:
                if cpu.gesture in gestures_dict[key] or player2.gesture in gestures_dict[key]:
                    print(f'{player1.name} wins round!')
                    self.player1_wins += 1
                    return
                else:
                    Score.cpu_and_player2_scores(self, mode_selected, player2)
                    return

    def cpu_and_player2_scores(self, mode_selected, player2):
        if mode_selected == 'Single-Player':
            self.cpu_wins += 1
            print('CPU wins round!')
        elif mode_selected == 'Multi-Player':
            self.player2_wins += 1
            print(f'{player2.name} wins round!')

    def score_tracker(self, player1, player2, cpu):
        # Loop Through Players & Player wins
        lst = player_list
        if self.tie_count == 2:
            print('Game has ended in a tie!')
        elif self.player1_wins == 2:
            print(f'{player1.name} has won the game!')
        elif self.player2_wins == 2:
            print(f'{player2.name} has won the game!')
        elif self.cpu_wins == 2:
            print(f'{cpu.name} has won the game!')
        # for i in range(0, len(self.tracker)):
        #     if self.tracker[i] == 2:
        #         print(f'{lst[i].name} has won the game!')
        #         return


score = Score(0, 0, 0, 0)

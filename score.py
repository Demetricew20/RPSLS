from players import Players

class Score:
    def __init__(self, player1_wins, player2_wins, cpu_wins, tie_count):
        self.player1_wins = player1_wins
        self.player2_wins = player2_wins
        self.cpu_wins = cpu_wins
        self.tie_count = tie_count

    def score_tracker(self, player1, player2, cpu):
        tracker = [self.player1_wins, self.player2_wins, self.cpu_wins]
        player_list = [player1, player2, cpu]
        for i in range(0, len(tracker)):
            if tracker[i] == 2:
                print(f'{player_list[i].name} has won the game!')
                return
            elif self.tie_count == 2:
                print('Game has ended in a tie!')
                return



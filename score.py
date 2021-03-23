from players import player_list


class Score:
    def __init__(self, player1_wins, player2_wins, cpu_wins, tie_count):
        self.player1_wins = player1_wins
        self.player2_wins = player2_wins
        self.cpu_wins = cpu_wins
        self.tie_count = tie_count
        self.tracker = [player1_wins, player2_wins, cpu_wins]

    def score_tracker(self):
        tracker = self.tracker.copy()
        #Loop Through Players & Player wins
        lst = player_list
        for i in range(0, len(tracker)):
            if self.tie_count == 2:
                print('Game has ended in a tie!')
                break
            elif tracker[i] == 2:
                print(f'{lst[i].name} has won the game!')
                return

    def scoring_rules(self, mode_selected, player1, cpu, player2):
        if player1.gesture == cpu.gesture or player1.gesture == player2.gesture:
            print('It is a tie!')
            self.tie_count += 1
        elif player1.gesture == 'Rock':
            if cpu.gesture in ('Lizard', 'Scissors') or player2.gesture in ('Lizard', 'Scissors'):
                print(f'{player1.name} wins round!')
                self.player1_wins += 1
            else:
                Score.cpu_and_player2_scores(self, mode_selected, player2)
        elif player1.gesture == 'Paper':
            if cpu.gesture in ('Spock', 'Rock') or player2.gesture in ('Spock', 'Rock'):
                print(f'{player1.name} wins round!')
                self.player1_wins += 1
            else:
                Score.cpu_and_player2_scores(self, mode_selected, player2)
        elif player1.gesture == 'Scissors':
            if cpu.gesture in ('Paper', 'Lizard') or player2.gesture in ('Paper', 'Lizard'):
                print(f'{player1.name} wins round!')
                self.player1_wins += 1
            else:
                Score.cpu_and_player2_scores(self, mode_selected, player2)
        elif player1.gesture == 'Lizard':
            if cpu.gesture in ('Paper', 'Spock') or player2.gesture in ('Paper', 'Spock'):
                print(f'{player1.name} wins round!')
                self.player1_wins += 1
            else:
                Score.cpu_and_player2_scores(self, mode_selected, player2)
        elif player1.gesture == 'Spock':
            if cpu.gesture in ('Rock', 'Lizard') or player2.gesture in ('Rock', 'Lizard'):
                print(f'{player1.name} wins round!')
                self.player1_wins += 1
            else:
                Score.cpu_and_player2_scores(self, mode_selected, player2)

    def cpu_and_player2_scores(self, mode_selected, player2):
        if mode_selected == 'Single-Player':
            self.cpu_wins += 1
            print('CPU wins round!')
        elif mode_selected == 'Multi-Player':
            self.player2_wins += 1
            print(f'{player2.name} wins round!')
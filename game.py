import random
from score import Score, score
from gesture import gestures


class Game(Score):
    def __init__(self, name):
        self.name = name
        self.mode_options = ('Single-Player', 'Multi-Player')
        self.mode_selected = ''
        self.gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.dictionary = {'Rock': ('Lizard', 'Scissors'), 'Paper': ('Spock', 'Rock'), 'Scissors': ('Paper', 'Lizard'),
                           'Lizard': ('Paper', 'Spock'), 'Spock': ('Rock', 'Lizard')}
        super().__init__(player1_wins=score.player1_wins, player2_wins=score.player2_wins, cpu_wins=score.cpu_wins
                         , tie_count=score.tie_count)

    # Welcome Message
    def welcome_message(self):
        print(f'Welcome to {self.name}!')

    # Rules
    def rules(self):
        print('**RULES**:\nEach player will simultaneously through a gesture from the available options list.'
              '\nScoring goes as follows:\nRock > Scissors\nRock > Lizard\nPaper > Rock\nPaper > Spock'
              '\nScissors > Lizard\nScissors > Paper\nLizard > Spock\nLizard > Paper\nSpock > Scissors\nSpock > Rock')

    def dict_to_list(self):
        keys = self.dictionary.keys()
        keys_list = list(keys)
        return keys_list

    # Select 1-player or 2-players
    def select_mode(self):
        user_input = input('Enter mode - Single-Player | Multi-Player : ')
        while user_input not in self.mode_options:
            user_input = input('Must choose Single-Player or Multi-Player. Try again: ')
        self.mode_selected = user_input
        print(f'*{self.mode_selected} mode selected*')

    def validate_user_input(self, player1, player2):
        if self.mode_selected == 'Single-Player':
            print(f'Available Options: {gestures.dict_keys()}')
            player1.gesture = input(f'{player1.name} select gesture: ')
            while player1.gesture not in gestures.dict_keys():
                player1.gesture = input(f'*{player1.name}* choose from options list only! Try again: ')
            print(f'{player1.name} selected : {player1.gesture}')
        elif self.mode_selected == 'Multi-Player':
            player_list = [player1, player2]
            print(f'Available Options: {gestures.dict_keys()}')
            for player in player_list:
                player.gesture = input(f'{player.name} select gesture: ')
                while player.gesture not in gestures.dict_keys():
                    player.gesture = input(f'*{player.name}* choose from options list only! Try again: ')
                print(f'{player.name} selected : {player.gesture}')

    # Run Game
    def start_game(self, player1, player2, cpu):
        # Begin Score Tracker
        while score.player1_wins != 2 and score.player2_wins != 2 and score.tie_count != 2 and score.cpu_wins != 2:
            # Player1 move
            Game.validate_user_input(self, player1, player2)
            if self.mode_selected == 'Single-Player':
                # CPU move
                cpu.gesture = random.choice(list(gestures.dict_keys()))
                print(f'CPU selected : {cpu.gesture}')
                # SP Scoring
                score.scoring_dictionary(self.mode_selected, player1, player2, cpu)
                # SP Update Score Tracker
                score.score_tracker(player1, player2, cpu)
            if self.mode_selected == 'Multi-Player':
                # MP Scoring
                score.scoring_dictionary(self.mode_selected, player1, player2, cpu)
                # MP Update Score Tracker
                score.score_tracker(player1, player2, cpu)

    # End Game/Message
    def end_game(self):
        print('Game Over. Rematch?')


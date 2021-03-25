import random
from score import Score, score
from gesture import gestures
from UI import user_interface


class Game(Score):
    def __init__(self, name):
        self.name = name
        self.mode_options = ('Single-Player', 'Multi-Player')
        self.mode_selected = ''
        super().__init__(player1_wins=score.player1_wins, player2_wins=score.player2_wins, cpu_wins=score.cpu_wins
                         , tie_count=score.tie_count)

    # Welcome Message
    def welcome_message(self):
        user_interface.start_message(self.name)
        user_interface.rules()

    # Select 1-player or 2-players
    def select_mode(self):
        user_input = user_interface.mode_selection()
        while user_input not in self.mode_options:
            user_interface.validation_statement()
            user_input = user_interface.mode_selection()
        self.mode_selected = user_input
        user_interface.mode_selection_statement(self.mode_selected)

    def validate_user_input(self, player1, player2):
        if self.mode_selected == 'Single-Player':
            user_interface.available_gestures(gestures.dict_keys())
            user_interface.gesture_selection(player1)
            while player1.gesture not in gestures.dict_keys():
                user_interface.validation_statement()
                user_interface.available_gestures(gestures.dict_keys())
                user_interface.gesture_selection(player1)
            user_interface.gesture_selected_statement(player1)
        elif self.mode_selected == 'Multi-Player':
            lst = [player1, player2]
            for player in lst:
                user_interface.available_gestures(gestures.dict_keys())
                user_interface.gesture_selection(player)
                user_interface.clear_console()
                while player.gesture not in gestures.dict_keys():
                    user_interface.validation_statement()
                    user_interface.available_gestures(gestures.dict_keys())
                    user_interface.gesture_selection(player)
                    user_interface.gesture_selected_statement(player)
                    user_interface.clear_console()

    # Run Game
    def start_game(self, player1, player2, cpu):
        # Begin Score Tracker
        while score.player1_wins != 2 and score.player2_wins != 2 and score.tie_count != 2 and score.cpu_wins != 2:
            # Player1 move
            Game.validate_user_input(self, player1, player2)
            if self.mode_selected == 'Single-Player':
                # CPU move
                cpu.gesture = random.choice(list(gestures.dict_keys()))
                user_interface.gesture_selected_statement(cpu)
                # SP Scoring
                score.scoring_dictionary(self.mode_selected, player1, player2, cpu)
                # SP Update Score Tracker
                score.score_tracker()
            if self.mode_selected == 'Multi-Player':
                # MP Scoring
                score.scoring_dictionary(self.mode_selected, player1, player2, cpu)
                # MP Update Score Tracker
                score.score_tracker()

    # End Game/Message
    def end_game(self):
        user_interface.end_game_message()



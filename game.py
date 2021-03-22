import random


class Game:
    def __init__(self, name):
        self.name = name
        self.mode_options = ('Single-Player', 'Multi-Player')
        self.mode_selected = ''
        self.options_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    # Welcome Message
    def welcome_message(self):
        print(f'Welcome to {self.name}!')
    # Rules
    def rules(self):
        print('**RULES**:\nEach player will simultaneously through a gesture from the available options list.'
              '\nScoring goes as follows:\nRock > Scissors\nScissors > Paper\nPaper > Rock\nRock > Lizard\nLizard > Spock'
              '\nSpock > Scissors\nScissors > Lizard\nLizard > Paper\nPaper > Spock\nSpock > Rock')

    # Select 1-player or 2-players
    def select_mode(self):
        user_input = input('Enter mode- Single-Player | Multi-Player : ')
        while user_input not in self.mode_options:
            user_input = input('Must choose Single-Player or Multi-Player. Try again: ')
        self.mode_selected = user_input
        print(f'*{self.mode_selected} mode selected*')

    # Run Game
    def start_game(self, player1, player2, cpu):
        if self.mode_selected == 'Single-Player':
            options_list = self.options_list.copy()
            player1_wins = 0
            cpu_wins = 0
            tie_count = 0
            while player1_wins != 2 and cpu_wins != 2:
                # Player1 move
                print(f'Available Options: {self.options_list}')
                player1.gesture = input(f'{player1.name} select gesture: ')
                while player1.gesture not in self.options_list:
                    player1.gesture = input(f'*{player1.name}* choose from options list only! Try again: ')
                print(f'{player1.name} selected : {player1.gesture}')
                # CPU move
                n = random.randint(0, 4)
                cpu.gesture = options_list[n]
                print(f'CPU selected : {cpu.gesture}')

                # Scoring
                if player1.gesture == cpu.gesture:
                    print('It is a tie!')
                    tie_count += 1
                elif player1.gesture == 'Rock' and cpu.gesture in ('Lizard', 'Scissors'):
                    print(f'{player1.name} wins round!')
                    player1_wins += 1
                elif player1.gesture == 'Paper' and cpu.gesture in ('Spock', 'Rock'):
                    print(f'{player1.name} wins round!')
                    player1_wins += 1
                elif player1.gesture == 'Scissors' and cpu.gesture in ('Paper', 'Lizard'):
                    print(f'{player1.name} wins round!')
                    player1_wins += 1
                elif player1.gesture == 'Lizard' and cpu.gesture in ('Paper', 'Spock'):
                    print(f'{player1.name} wins round!')
                    player1_wins += 1
                elif player1.gesture == 'Spock' and cpu.gesture in ('Rock', 'Lizard'):
                    print(f'{player1.name} wins round!')
                    player1_wins += 1
                else:
                    print('CPU wins round!')
                    cpu_wins += 1

                # Score Tracker for game
                if player1_wins == 2:
                    print(f'{player1.name} wins game!')
                    break
                elif cpu_wins == 2:
                    print('CPU wins game!')
                    break
                elif tie_count == 2:
                    print('Game is a tie!')
                    break
        if self.mode_selected == 'Multi-Player':
            player1_wins = 0
            player2_wins = 0
            tie_count = 0
            while player1_wins != 2 and player2_wins != 2:
                # Player1 move
                print(f'Available Options: {self.options_list}')
                player1.gesture = input(f'{player1.name} select gesture: ')
                while player1.gesture not in self.options_list:
                    player1.gesture = input(f'*{player1.name}* Choose from options list only! Try again: ')
                print(f'Player1 selected : {player1.gesture}')
                # Player2 move
                n = random.randint(0, 4)
                print(f'Available Options: {self.options_list}')
                player2.gesture = input(f'{player2.name} select gesture: ')
                while player2.gesture not in self.options_list:
                    player2.gesture = input(f'*{player2.name}* Choose from options list only! Try again: ')
                print(f'{player2.name} selected : {player2.gesture}')

                # Scoring
                if player1.gesture == player2.gesture:
                    print('It is a tie!')
                    tie_count += 1
                elif player1.gesture == 'Rock' and player2.gesture in ('Lizard', 'Scissors'):
                    print(f'{player1.name} wins round!')
                    player1_wins += 1
                elif player1.gesture == 'Paper' and player2.gesture in ('Spock', 'Rock'):
                    print(f'{player1.name} wins round!')
                    player1_wins += 1
                elif player1.gesture == 'Scissors' and player2.gesture in ('Paper', 'Lizard'):
                    print(f'{player1.name} wins round!')
                    player1_wins += 1
                elif player1.gesture == 'Lizard' and player2.gesture in ('Paper', 'Spock'):
                    print(f'{player1.name} wins round!')
                    player1_wins += 1
                elif player1.gesture == 'Spock' and player2.gesture in ('Rock', 'Lizard'):
                    print(f'{player1.name} wins round!')
                    player1_wins += 1
                else:
                    print(f'{player2.name} wins round!')
                    player2_wins += 1

                # Score Tracker for game
                if player1_wins == 2:
                    print(f'{player1.name} wins game!')
                    break
                elif player2_wins == 2:
                    print(f'({player2.name} wins game!')
                    break
                elif tie_count == 2:
                    print('Game is a tie!')
                    break

    # End Game/Message
    def end_game(self):
        print('Game Over. Rematch?')

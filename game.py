import random

class Game:
    def __init__(self, name):
        self.name = name
        self.mode = ""
        self.options_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    #Welcome Message
    def welcome_message(self):
        print (f'Welcome to {self.name}!')
    #Rules
    def rules(self):
        print('**RULES**:\nEach player will simultaneously through a gesture from the available options list.'
              '\nScoring goes as follows:\nRock > Scissors\nScissors > Paper\nPaper > Rock\nRock > Lizard\nLizard > Spock'
              '\nSpock > Scissors\nScissors > Lizard\nLizard > Paper\nPaper > Spock\nSpock > Rock')
    #Select 1-player or 2-players
    def select_mode(self):
        user_input = input('Enter mode- Single-Player | Multi-Player : ')
        if user_input == 'Single-Player' or user_input == 'Multi-Player':
            self.mode = user_input
            print(f'*{self.mode} mode selected*')
    #Run Game
    def start_game(self, player1, player2):
        options_list = self.options_list.copy()
        player1_wins = 0
        cpu_wins = 0
        tie_count = 0
        if self.mode == 'Single-Player':
            #Provide Results
            #Handle Ties
            #Keep Score, while loop, score tracker
            while player1_wins != 2 and cpu_wins != 2:
                #Player1 move
                print(f'Available Options: {self.options_list}')
                player1.gesture = input('Select gesture: ')
                print(f'User selected : {player1.gesture}')
                #CPU move
                n = random.randint(0, 4)
                player2.gesture = options_list[n]
                print(f'CPU selected : {player2.gesture}')

                #Scoring
                if player1.gesture == player2.gesture:
                    print('It is a tie!')
                    tie_count += 1
                elif player1.gesture == 'Rock' and player2.gesture in ('Lizard', 'Scissors'):
                    print('Player1 wins round!')
                    player1_wins += 1
                elif player1.gesture == 'Paper' and player2.gesture in ('Spock', 'Rock'):
                    print('Player1 wins round!')
                    player1_wins += 1
                elif player1.gesture == 'Scissors' and player2.gesture in ('Paper', 'Lizard'):
                    print('Player1 wins round!')
                    player1_wins += 1
                elif player1.gesture == 'Lizard' and player2.gesture in ('Paper', 'Spock'):
                    print('Player1 wins round!')
                    player1_wins += 1
                elif player1.gesture == 'Spock' and player2.gesture in ('Rock', 'Lizard'):
                    print('Player1 wins round!')
                    player1_wins += 1
                else:
                    print('CPU wins round!')
                    cpu_wins += 1
                    
                #Score Tracker for game
                if player1_wins == 2:
                    print('Player1 wins game!')
                    break
                elif cpu_wins == 2:
                    print('CPU wins game!')
                    break
                elif tie_count == 2:
                    print('Game is a tie. Rematch?')
                    break


            #Best of Three





    #End Game/Message



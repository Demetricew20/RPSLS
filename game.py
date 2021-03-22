

class Game:
    def __init__(self, name):
        self.name = name
        self.mode = ""

    #Welcome Message
    def welcome_message(self):
        print (f'Welcome to {self.name}!')
    #Rules
    def rules(self):
        print('**RULES**:\nEach player will simultaneously through a gesture from the available options list.'
              '\nScoring goes as follows:\nRock > Scissors\nScissors > Paper\nPaper > Rock\nRock > Lizard\nLizard > Spock'
              'Spock > Scissors\nScissors > Lizard\nLizard > Paper\nPaper > Spock\nSpock > Rock')
    #Select 1-player or 2-players
    def select_mode(self):
        user_input = input('Enter mode- Single-Player | Multi-Player : ')
        if user_input == 'Single-Player' or user_input == 'Multi-Player':
            self.mode = user_input
            print(f'*{self.mode} mode selected*')
    #Options List

    #Run Game

    #End Game/Message



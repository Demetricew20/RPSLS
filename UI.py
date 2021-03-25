import keyboard
import os


class UI:
    def __init__(self):
        pass

    def start_message(self, name):
        print(f'Welcome to {name}!')

    def rules(self):
        print('**RULES**:\nEach player will simultaneously through a gesture from the available options list.'
              '\nScoring goes as follows:\nRock > Scissors\nRock > Lizard\nPaper > Rock\nPaper > Spock'
              '\nScissors > Lizard\nScissors > Paper\nLizard > Spock\nLizard > Paper\nSpock > Scissors\nSpock > Rock')

    def mode_selection(self):
        user_input = input('Enter mode - Single-Player | Multi-Player: ')
        return user_input

    def mode_selection_statement(self, mode_selected):
        print(f'**{mode_selected} mode was selected**')

    def available_gestures(self, options):
        print(f'Available Gestures: {options}')

    def gesture_selection(self, player):
        player.gesture = input(f'{player.name} select gesture: ')
        return player.gesture

    def gesture_selected_statement(self, player):
        print(f'{player.name} selected: {player.gesture}')

    def ai_selected_statement(self, cpu):
        print(f'{cpu.name} selected: {cpu.gesture}')

    def validation_statement(self):
        print('Invalid input. Must select from list. Try Again. ')

    def round_winner(self, player):
        print(f'{player.name} has won the round!')

    def game_winner(self, player):
        print(f'\n{player.name} has won the game!')

    def end_game_message(self):
        print('Game over! Press DOWN arrow for rematch! Press Enter key to exit game.')
        while True:
            if keyboard.is_pressed('down'):
                os.system('python main.py')
                break
            elif keyboard.is_pressed('enter'):
                print('Thanks for playing!')
                break


user_interface = UI()


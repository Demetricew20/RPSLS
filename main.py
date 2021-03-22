from players import Players, CPU
from game import Game

if __name__ == '__main__':

    rpsls = Game('Rock Paper Scissors Lizard Spock')
    rpsls.welcome_message()
    rpsls.rules()
    rpsls.select_mode()

    cpu = CPU()
    player1 = Players('Player1')
    player2 = Players('Player2')

    rpsls.start_game(player1, player2, cpu)


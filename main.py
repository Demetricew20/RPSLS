from players import Humans, CPU
from game import Game

if __name__ == '__main__':

    rpsls = Game('Rock Paper Scissors Lizard Spock')
    rpsls.welcome_message()
    rpsls.rules()
    rpsls.select_mode()
    cpu = CPU('CPU')
    player1 = Humans('John')
    player2 = Humans('Jane')
    rpsls.start_game(player1, player2, cpu)
    rpsls.end_game()


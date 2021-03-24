from players import Humans, CPU, player_list
from game import Game

if __name__ == '__main__':

    rpsls = Game('Rock Paper Scissors Lizard Spock')
    rpsls.welcome_message()
    rpsls.select_mode()
    cpu = CPU('CPU')
    john = Humans('John')
    jane = Humans('Jane')
    player_list.add_player(john)
    player_list.add_player(jane)
    player_list.add_player(cpu)
    rpsls.start_game(john, jane, cpu)
    rpsls.end_game()






class Players:
    def __init__(self, name):
        self.gesture = ''
        self.name = name


class Humans(Players):
    def __init__(self, name):
        super().__init__(name)


class CPU(Players):
    def __init__(self, name):
        super().__init__(name)


class PlayersList:
    def __init__(self):
        self.player_list = []

    def add_player(self, player):
        self.player_list.append(player)

    def __repr__(self):
        player_list = self.player_list.copy()
        return f'{player_list}'


player_list = PlayersList()
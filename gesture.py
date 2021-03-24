class Gestures:
    def __init__(self):
        self.gestures_dict = {'Rock': ('Lizard', 'Scissors'), 'Paper': ('Spock', 'Rock'),
                              'Scissors': ('Paper', 'Lizard'), 'Lizard': ('Paper', 'Spock'),
                              'Spock': ('Rock', 'Lizard')}

    def dict_keys(self):
        keys = self.gestures_dict.keys()
        keys_list = list(keys)
        return keys_list

    def dict_values(self):
        values = self.gestures_dict.values()
        values_list = list(values)
        return values_list



gestures = Gestures()

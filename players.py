

class CPU:
    def __init__(self):
        self.options = ['Rock',  'Paper', 'Scissors', 'Lizard', 'Spock']


class Players(CPU):
    def __init__(self, name):
        super(CPU, self).__init__()
        self.name = name



    # def __repr__(self):
    #     print(f'{self.name}')
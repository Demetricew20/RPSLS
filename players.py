

class Players:
    def __init__(self, name):
        self.name = name
        self.gesture = ''
class Humans(Players):
    def __init__(self, name):
        self.name = name
        super(Humans, self).__init__(Players)

class CPU(Players):
    def __init__(self):
        super(CPU, self).__init__(Players)



class Players:
    def __init__(self):
        self.gesture = ''


class Humans(Players):
    def __init__(self, name):
        self.name = name
        super(Humans, self).__init__()


class CPU(Players):
    def __init__(self):
        super(CPU, self).__init__()

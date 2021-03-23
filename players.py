

class Players:
    def __init__(self, name):
        self.gesture = ''
        self.name = name


class Humans(Players):
    def __init__(self, name):
        super().__init__(name)


class CPU(Players):
    def __init__(self, name):
        super(CPU, self).__init__(name)

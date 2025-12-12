from Vehicle import Vehicle
class Ship(Vehicle):
    def __init__(self, capacity, name):
        super().__init__(self, capacity)
        self.name = name
        self.capacity = capacity

d = Ship(1, 2)


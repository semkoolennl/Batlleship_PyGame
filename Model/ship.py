class Ship:
    def __init__(self, name, length):
        self.placed = False
        self.destroyed = False
        self.x = 0
        self.y = 0
        self.length = length
        self.rotation = "horizontal"

    def getPos(self):
        return [self.x, self.y]

    def move(self, position):
        self.x = position[0]
        self.y = position[1]

    def rotate(self):
        if self.rotation == "horizontal":
            self.rotation = "vertical"
        else:
            self.rotation = "horizontal"

    def getHitbox(self):
        if self.rotation == "horizontal":
            hitbox = [[x, self.y] for x in range(self.x, self.x + self.length)]
        else:
            hitbox = [[self.x, y] for y in range(self.y, self.y + self.length)]

        return hitbox


class Fleet:
    def __init__(self, CONFIG):
        self.config = CONFIG.ships
        self.ships = self.create_ships()

    def create_ships(self):
        ships = []
        for name in self.config:
            size = self.config[name]
            ships += [Ship(name, size)]
        print(ships)



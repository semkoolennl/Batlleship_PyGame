import string
ascii_uppercase = list(string.ascii_uppercase)


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hit = False
        self.ship = None

    def __str__(self):
        if self.hit:
            if self.ship:
                if self.ship.destroyed:
                    return "X"
                return "x"
            return "*"

        return "#"

    def setShip(self, ship):
        self.ship = ship

    def hit(self):
        self.hit = True
        if self.ship:
            return True
        else:
            return False


class Board:
    def __init__(self):
        self.ships = []
        self.hits = []
        self.misses = []
        self.rows = [letter for letter in list(string.ascii_uppercase)[:10]]
        self.columns = [number for number in range(1, 11)]
        self.map = self.createMap()

    def createMap(self):
        row = [x for x in range(10)]
        return [[Tile(x, y) for x in range(10)] for y in range(10)]

    def print(self):
        for row in self.map:
            print("", [rep.__str__() for rep in row])
            # for tile in row:
            #     print(tile)
        # print(" ", self.rows)
        # for i in range(len(self.columns) + 1):
        #     if i == 0:
        #         print(" ", self.rows)
        #     else:
        #     print("Rows: ", self.rows)
        #     print("Columns: ", self.columns)

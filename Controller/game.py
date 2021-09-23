from Model.ship import Ship, Fleet
from Model.board import Board
from Model.configurator import Configurator
CONFIG = Configurator()

class Battleship:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        player_fleet = Fleet(CONFIG)
        enemy_fleet = Fleet(CONFIG)
        ship1 = Ship("Cruiser", 3)
        player_board = Board()
        player_board.map[0][0].ship = ship1
        ship1.destroyed = True
        player_board.map[0][0].hit = True
        player_board.print()
        print(ship1.getPos())


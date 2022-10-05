from battleship.board import Board
from battleship.ship import Ship

class Game:
  def __init__(self, rows, cols):
    self.board = Board(rows, cols)

  def create(self, ships):
    index = 0
    for ship in ships:
      ship_name = f"ship-{index}"
      x_axis = ship.get("x")
      y_axis = ship.get("y")
      size = ship.get("size")
      direction = ship.get("direction")
      ship_obj = Ship(x_axis, y_axis, size, ship_name, direction)
      index = index + 1
      if not ship_obj.plot_ship(self.board):
        return False
    return True

  def fire(self, coords):
    return self.board.place_shot(coords)
class Ship:
  def __init__(self, x_axis, y_axis, size, ship_name, direction):
    self.x_axis = x_axis
    self.y_axis = y_axis
    self.size = size
    self.ship_name = ship_name
    self.direction = direction

  def plot_ship(self, board):
    try:
      return board.plot_ship_on_board(self.x_axis, self.y_axis, self.ship_name, self.size, self.direction)
    except IndexError:
      return False
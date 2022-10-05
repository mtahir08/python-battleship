from battleship import constant


class Board:
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.grid = [[0] * self.rows for i  in range(self.cols)]
  
  def can_plot_ship_vertically(self, x_axis, y_axis, total_size):
    ship_size = y_axis
    for start in range(y_axis, total_size):
      if self.grid[x_axis][start] == 0:
        ship_size = ship_size + 1
    if ship_size == total_size:
      return True
    return False

  def can_plot_ship_horizontally(self, x_axis, y_axis, total_size):
    ship_size = x_axis
    for start in range(x_axis, total_size):
      if self.grid[start][y_axis] == 0:
        ship_size = ship_size + 1
    if ship_size == total_size:
      return True
    return False
    

  def plot_ship_on_board(self, x_axis, y_axis, ship_name, ship_size, direction):
    if direction == constant.VERTICAL:
      total_size = ship_size + y_axis
      if self.can_plot_ship_vertically(x_axis, y_axis, total_size):
          for start in range(y_axis, total_size):
              self.grid[x_axis][start] = ship_name
          return True
      return False
    elif direction == constant.HORIZONTAL:
      total_size = ship_size + x_axis
      if self.can_plot_ship_horizontally(x_axis, y_axis, total_size):
        for start in range(x_axis, total_size):
            self.grid[start][y_axis] = ship_name
        return True
      return False
    return False
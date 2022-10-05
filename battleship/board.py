from battleship import constant


class Board:
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.grid = [[0] * self.rows for i in range(self.cols)]
  
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

  def place_shot(self, coords):
    x_axis_to_shot = coords.get('x')
    y_axis_to_shot = coords.get('y')
    ship_name = self.grid[x_axis_to_shot][y_axis_to_shot]
    # check if ship part already got Hit
    if ship_name == constant.HIT:
      return constant.HIT
    # check if hit on water
    elif ship_name == 0:
      return constant.WATER
    
    ship_blocks = 0
    for x_axis in self.grid:
      for y_axis in x_axis:
        if y_axis == ship_name:
          ship_blocks = ship_blocks + 1

    if ship_blocks > 1:
      self.grid[x_axis_to_shot][y_axis_to_shot] = constant.HIT
      return constant.HIT
    return constant.SINK
    
  def delete_game_progress(self):
    self.grid = [[0] * self.rows for i in range(self.cols)]
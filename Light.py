from Lib.util import color

class Light:
  def __init__(self, position, intensity=1, color=color(1, 1, 1)) -> None:
    self.position = position
    self.intensity = intensity
    self.color = color

import pygame as pg

from pygame.locals import *

class Tile:
  """
  Represents an individual tile with content drawn on a Pygame surface.

  Parameters:
  - content (chr): The character content to be rendered on the tile.
  - side_len (int, optional): The side length of the tile. Default is 50.

  Attributes:
  - rect (pg.Rect): A Pygame rectangle representing the dimensions of the tile.
  - surface (pg.Surface): A Pygame surface for drawing the tile.
  - font (pg.font.Font): A Pygame font for rendering the content.
  - content (pg.Surface): The rendered content on the tile surface.
  - surface_rect (pg.Rect): The rectangle representing the dimensions of the tile surface.
  - content_rect (pg.Rect): The rectangle representing the dimensions of the rendered content.

  Methods:
  - __eq__(self, other): Equals comparison method. Used to compare tiles based on their content.
  """
  
  def __init__(self, content: str, side_len=50, color='pink') -> None:
    """
    Initializes a Tile with the specified content and side length.

    The content is rendered on the tile surface, and its position is centered.

    Args:
    - content (str): The character content to be rendered on the tile.
    - side_len (int, optional): The side length of the tile. Default is 50.
    - color (str): The pygame color of the background of the Tile. Default is pink.
    """

    if not isinstance(content, str):
      if len(content) != 1:
        raise ValueError(f'content is not a single character')

    self.rect = pg.Rect((0, 0), (side_len, side_len))
    self.surface = pg.Surface(size=self.rect.size)
    font_size = 96
    self.font = pg.font.Font(None, font_size)
    self.content = self.font.render(content, True, 'black')
    # Centering font
    self.surface_rect = self.surface.get_rect()
    self.content_rect = self.content.get_rect()
    self.content_rect.center = self.surface_rect.center
    
    pg.draw.rect(self.surface, color, self.rect)
    self.surface.blit(self.content, self.content_rect)

  def __eq__(self, other) -> bool:
    """
    Equals comparison method. Used to compare tiles based on their content.
    """

    return self.content == other.content

class TileGroup:
  """
  Represents a group of tiles on the screen.

  Parameters:
  - statestr (str): A string representing the state of the tiles.
  - tile_len (int): The side length of each tile.
  - padding (int, optional): The padding between tiles. Default is 0.
  - scale (int, optional): The scale factor for the entire tile group. Default is 1.
  - highlight (bool): Toggle for highlight mode, in which the blank tile is highlighted.
  
  Attributes:
  - tile_pos (List[Tuple[int, int]]): List of base tile positions before adjustments.
  - tile_len (int): The side length of each tile.
  - padding (int): The padding between tiles.
  - scale (int): The scale factor for the entire tile group.
  - statestr (str): The current state string.
  - tiles (List[Tile]): List of Tile objects created based on the state string.
  
  Methods:
  - draw(screen: pg.Surface): Draws the tile group on the specified Pygame surface.
  - update_statestr(statestr: str): Updates the state string and recreates the tiles accordingly.
  """
  
  def __init__(self, statestr: str, tile_len, padding: int = 0, scale: int = 1, highlight = False) -> None:
    """
    Initializes a TileGroup with the specified parameters.

    Base tile positions are adjusted for side length, padding, and scale.
    Tiles are created based on the provided state string.

    Args:
    - statestr (str): A string representing the state of the tiles.
    - tile_len (int): The side length of each tile.
    - padding (int, optional): The padding between tiles. Default is 0.
    - scale (int, optional): The scale factor for the entire tile group. Default is 1.
    - highlight (bool): Toggle for highlight mode, in which the blank tile is highlighted.
    """

    self.highlight = highlight

    # Base tile positions
    tile_pos: list[tuple[int, int]] = [
      (0, 0), (1, 0), (2, 0),
      (0, 1), (1, 1), (2, 1),
      (0, 2), (1, 2), (2, 2)
    ]
    # Adjust for side length and padding
    tile_pos = [(x*(tile_len + padding), y*(tile_len + padding)) for x, y in tile_pos]
    self.tile_pos = [(x*scale, y*scale) for x, y in tile_pos]

    # Setting internal attributes
    self.tile_len = tile_len
    self.padding = padding
    self.scale = scale
    self.statestr = statestr

    # Creating tiles based on statestr
    self.tiles: list[Tile] = [Tile(tile_num, tile_len) for tile_num in statestr]
    index = self.statestr.index('0')
    zero_color = 'pink' if highlight else 'orange'
    self.tiles[index] = Tile(' ', self.tile_len, color=zero_color)

  def draw(self, screen: pg.Surface) -> None:
    """
    Draws the tile group on the specified Pygame surface.

    Args:
    - screen (pg.Surface): The Pygame surface on which to draw the tile group.
    """

    screen.blits([(t.surface, pos) for t, pos in zip(self.tiles, self.tile_pos)])

  def update_statestr(self, statestr: str) -> None:
    """
    Updates the state string and recreates the tiles accordingly.

    Args:
    - statestr (str): The new state string.
    """
    
    if statestr != self.statestr:
      self.statestr = statestr
      # Creating tiles based on new statestr
      self.tiles: list[Tile] = [Tile(tile_chr, self.tile_len) for tile_chr in statestr]
      index = self.statestr.index('0')
      zero_color = 'pink' if self.highlight else 'orange'
      self.tiles[index] = Tile(' ', self.tile_len, color=zero_color)

class TextBox:
  """
  Represents a text box in Pygame, displaying text read from a file.

  Attributes:
  - path (str): The path to the text file.
  - line_len (int): The maximum number of characters per line in the text box.
  - font_size (int): The size of the font used for rendering the text.
  - text_color (str): The color of the text (default is 'black').
  - back_color (str): The background color of the text box (default is 'white').
  - font (pg.font.Font): The Pygame font object with the specified font size.
  - line_surfaces (list[pg.Surface]): List of Pygame surfaces, each containing a rendered line of text.
  - total_height (int): The total height needed for all lines in the text box.
  - text_surface (pg.Surface): Pygame surface containing the entire rendered text box.
  - rect (pg.Rect): Pygame rectangle representing the dimensions of the text surface.

  Methods:
  - __init__(self, path: str, line_len: int, font_size: int, text_color: str = 'black', back_color: str = 'white') -> None:
      Initializes a TextBox object by reading lines from a file and rendering them onto a Pygame surface. 
  - draw(self, screen: pg.Surface) -> None:
      Draws the text box onto the specified Pygame surface.
  """
    
  def __init__(self, path: str, line_len: int, font_size: int, text_color: str = 'black', back_color: str = 'white') -> None:
    self.font_size: int = font_size
    self.font: pg.font.Font = pg.font.Font(None, self.font_size)

    # Read lines form file
    self.line_len: int = line_len
    with open(file=path) as file:
      lines = file.readlines()

    # Render text box line by line
    self.line_surfaces: list[pg.Surface] = [self.font.render(line.strip(), True, text_color) for line in lines]
    self.total_height: int = sum(surface.get_height() for surface in self.line_surfaces)
    self.text_surface: pg.Surface = pg.Surface((line_len, self.total_height))
    self.text_surface.fill(back_color)

    y_offset = 0
    for line_surface in self.line_surfaces:
      self.text_surface.blit(line_surface, (0, y_offset))
      y_offset += line_surface.get_height()

    self.rect: pg.Rect = self.text_surface.get_rect()

  def draw(self, screen: pg.Surface) -> None:
    """
    Draws the text box onto the specified Pygame surface.
    
    Parameters:
    - screen (pg.Surface): The Pygame surface on which to draw the text box.
  
    Returns:
    - None
    """
    
    screen.blit(self.text_surface, self.rect)

class Speedometer:
  def __init__(self, speed: int, font_size: int, text_color: str = 'red', back_color: str = 'white') -> None:
    self.font_size: int = font_size
    self.font = pg.font.Font(None, font_size)
    self.text_color = text_color
    self.back_color = back_color
    self._update(speed, text_color, back_color)
    self.rect: pg.Rect = self.content.get_rect()
    
  def _update(self, speed: int, text_color: str = 'red', back_color: str = 'white') -> None:
    self.speed: int = speed
    self.content: pg.Surface = self.font.render('Speed: ' + str(round(1000/self.speed, 2)) + 'steps/sec.', True, text_color, back_color)

  def set_speed(self, speed: int) -> None:
    self._update(speed, self.text_color, self.back_color)

  def draw(self, screen: pg.Surface) -> None:
    """
    Draws the text box onto the specified Pygame surface.
    
    Parameters:
    - screen (pg.Surface): The Pygame surface on which to draw the text box.
  
    Returns:
    - None
    """
    
    screen.blit(self.content, self.rect)
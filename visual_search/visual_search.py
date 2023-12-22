"""Main module."""

import puzzle
import pygame as pg
from pygame.locals import *

pg.init()

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
  - No public methods are provided.
  """
  
  def __init__(self, content: chr, side_len=50) -> None:
    """
    Initializes a Tile with the specified content and side length.

    The content is rendered on the tile surface, and its position is centered.

    Args:
    - content (chr): The character content to be rendered on the tile.
    - side_len (int, optional): The side length of the tile. Default is 50.
    """

    self.rect = pg.Rect((0, 0), (side_len, side_len))
    self.surface = pg.Surface(size=self.rect.size)
    font_size = 96
    self.font = pg.font.Font(None, font_size)
    self.content = self.font.render(content, True, 'black')
    # Centering font
    self.surface_rect = self.surface.get_rect()
    self.content_rect = self.content.get_rect()
    self.content_rect.center = self.surface_rect.center
    
    pg.draw.rect(self.surface, 'pink', self.rect)
    self.surface.blit(self.content, self.content_rect)

class TileGroup:
  """
  Represents a group of tiles on the screen.

  Parameters:
  - statestr (str): A string representing the state of the tiles.
  - tile_len (int): The side length of each tile.
  - padding (int, optional): The padding between tiles. Default is 0.
  - scale (int, optional): The scale factor for the entire tile group. Default is 1.
  
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

  def __init__(self, statestr, tile_len, padding: int = 0, scale: int = 1) -> None:
    """
    Initializes a TileGroup with the specified parameters.

    Base tile positions are adjusted for side length, padding, and scale.
    Tiles are created based on the provided state string.

    Args:
    - statestr (str): A string representing the state of the tiles.
    - tile_len (int): The side length of each tile.
    - padding (int, optional): The padding between tiles. Default is 0.
    - scale (int, optional): The scale factor for the entire tile group. Default is 1.
    """

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
    
    self.statestr = statestr

if __name__ == '__main__':
  
  screen: pg.Surface = pg.display.set_mode()
  width, height = screen.get_size()
  p: puzzle.EightPuzzle = puzzle.EightPuzzle('012345678')
  tilegroup = TileGroup(p.statestr, tile_len=250, padding=10, scale=1)

  running = True
  while running:
    for e in pg.event.get():
      if e.type == KEYDOWN:
        if e.key == K_ESCAPE:
          running = False
    
    tilegroup.draw(screen)
    pg.display.flip()
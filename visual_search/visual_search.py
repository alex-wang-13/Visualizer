"""Main module."""

import pygame as pg

from pygame.locals import *
from puzzle import EightPuzzle
from components import TileGroup

pg.init()

if __name__ == '__main__':
  
  screen: pg.Surface = pg.display.set_mode()
  width, height = screen.get_size()
  p: EightPuzzle = EightPuzzle(EightPuzzle.goal_state)
  tilegroup = TileGroup(p.statestr, tile_len=250, padding=10, scale=1)

  running = True
  while running:
    for e in pg.event.get():
      if e.type == KEYDOWN:
        if e.key == K_ESCAPE:
          running = False
        # Check K_1 to K_8
        for value in range(K_1, K_1+8):
          if e.key == value:
            p.move(value - K_0)
    
    # Update and draw the tiles to the screen
    tilegroup.update_statestr(p.statestr)
    tilegroup.draw(screen)
    pg.display.flip()

pg.quit()
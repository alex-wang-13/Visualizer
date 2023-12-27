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
  
  clock = pg.time.Clock()
  queue_start_time: int = 0
  queue_delay_time: int = 500
  state_queue: list[list[int]] = []

  running = True
  while running:
    for e in pg.event.get():
      if e.type == KEYDOWN:
        if e.key == K_ESCAPE or e.key == K_q:
          running = False
        if state_queue:
          continue
        # Check K_1 to K_8
        for value in range(K_1, K_1+8):
          if e.key == value:
            p.move(value - K_0)
        if e.key == K_SPACE:
          state_queue = p.solve_astar()
          queue_start_time = pg.time.get_ticks()
    
    # Handle the queue
    if state_queue:
      # Index is based on the number of ticks that has passed
      queue_index = (pg.time.get_ticks() - queue_start_time) // queue_delay_time

      # Check if the last index has been reached; if so, reset the queue.
      if queue_index < len(state_queue):
        tilegroup.highlighted = True
        p.set(state_queue[queue_index])
      else:
        tilegroup.highlighted = False
        state_queue = []
     
    # Update and draw the tiles to the screen
    tilegroup.update_statestr(p.statestr)
    tilegroup.draw(screen)
    pg.display.flip()

    clock.tick(60)

pg.quit()
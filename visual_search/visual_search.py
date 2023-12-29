"""Main module."""

import pygame as pg

from pygame.locals import *
from puzzle import EightPuzzle
from components import TileGroup, TextBox, Speedometer
from utils import controls_fp

pg.init()

if __name__ == '__main__':
  
  screen: pg.Surface = pg.display.set_mode()
  width, height = screen.get_size()
  p: EightPuzzle = EightPuzzle(EightPuzzle.goal_state)
  tilegroup: TileGroup = TileGroup(p.statestr, tile_len=250, padding=10, scale=1)
  
  textbox: TextBox = TextBox(path=controls_fp, line_len=width//2, font_size=64)
  textbox.rect.topleft = width//2, 0

  clock = pg.time.Clock()
  queue_start_time: int = 0
  queue_delay_time: int = 500
  speedometer: Speedometer = Speedometer(500, 64)
  speedometer.rect.topleft = width//2, textbox.rect.height

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
            try:
              p.move(value - K_0)
            except ValueError as error:
              print(error)
        if e.key == K_a:
          state_queue = p.solve_astar()
          queue_start_time = pg.time.get_ticks()
        if e.key == K_s:
          p.shuffle(k=10000)
        if e.key == K_DOWN and queue_delay_time > 100:
          queue_delay_time -= 100
        if e.key == K_UP:
          queue_delay_time += 100
    
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
     
    # Clear the frame
    screen.fill('black')
    
    # Update and draw the tiles to the screen
    tilegroup.update_statestr(p.statestr)
    tilegroup.draw(screen)
    textbox.draw(screen)
    speedometer.set_speed(queue_delay_time)
    speedometer.draw(screen)
    pg.display.flip()

    clock.tick(60)

pg.quit()
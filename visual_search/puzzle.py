import utils

from random import choice, seed

class EightPuzzle:
  """
  Represents the 8-puzzle game.

  Attributes:
  - goal_state (list[int]): The goal state of the puzzle.
  - adj_masks (list[list[int]]): Masks representing the adjacency relationships between tiles.
  - state (list[int]): The current state of the puzzle.
  - statestr (str): A string representation of the current state.
  - adj_mask (list[int]): The adjacency mask for the blank space.
  - z_index (int): The index of the blank space.

  Methods:
  - set(self, state: str) -> list[int]: Converts a string state to a list of integers.
  - move(self, tile: int): Moves the specified tile to the blank space.
  - is_solved(self) -> bool: Checks if the puzzle is in the solved state.
  - print_board(self): Prints the current state of the puzzle.
  - shuffle(self, k: int): Shuffles the puzzle to generate a random solvable configuration.
  - reset(self): Resets the puzzle to its initial state.
  """

  goal_state: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  _adj_masks: list[list[int]] = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0]
  ]

  def __init__(self, state: list[int]):
    """
    Initializes the EightPuzzle instance with the given state.

    Args:
    - state (list[int]): The initial state of the puzzle.
    """
    
    self.set(state)
    
  def set(self, state: list[int]):
    """
    Converts a string state to a list of integers.

    Args:
    - state (list[int]): The representation of the state.
    """

    if not isinstance(state, list):
      raise ValueError(f'given argument is not a list')
    if len(state) != utils.num_tiles:
      raise ValueError(f'state {state} does not have 9 digits')
    for val in state:
      if not isinstance(val, int):
        raise ValueError(f'given values in list are not type int')
    if set(state) != set(range(utils.num_tiles)):
      raise ValueError(f'state does not have integers 0-8')
      
    self.state = state
    self.statestr = ''.join(str(i) for i in self.state)
    self.z_index = self.state.index(0)
    self.adj_mask = self._adj_masks[self.z_index]

  def move(self, tile: int):
    """
    Moves the specified tile to the blank space.

    Args:
    - tile (int): The tile to move.
    """
    
    # Get the index of the tile and check for adjacency
    t_index = self.state.index(tile)
    if self.adj_mask[t_index]:
      state = self.state.copy()
      state[t_index], state[self.z_index] = state[self.z_index], state[t_index]
      self.set(state)
    else:
      raise ValueError(f'the tile {tile} cannot be moved to the blank space')

  def is_solved(self):
    """
    Checks if the current board configuration matches the goal state.

    Returns:
    - bool: True if the puzzle is solved, False otherwise.
    """
    return self.state == self.goal_state

  def print_board(self):
    """
    Prints the current state of the puzzle.
    """

    print(self.statestr[0:3])
    print(self.statestr[3:6])
    print(self.statestr[6:9])

  def shuffle(self, k: int, set_seed: int = None):
    """
    Shuffles the puzzle to generate a random solvable configuration.

    Args:
    - k (int): The number of random moves to perform.
    - seed (int): The seed for RNG.
    """
    
    if seed:
      seed(set_seed)

    for i in range(k):
      options = [self.state[index] for index, value in enumerate(self.adj_mask) if value]
      self.move(choice(options))

  def reset(self):
    """
    Resets the puzzle to its initial state.
    """

    self.set(self.goal_state.copy())

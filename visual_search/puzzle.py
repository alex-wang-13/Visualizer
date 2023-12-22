import utils

class EightPuzzle:
  """
  Represents the 8-puzzle game.

  Attributes:
  - goal_state (list[int]): The goal state of the puzzle.
  - adj_masks (list[list[int]]): Masks representing the adjacency relationships between tiles.
  - state (list[int]): The current state of the puzzle.
  - statestr (str): A string representation of the current state.
  - adj_mask (list[int]): The adjacency mask for the blank space.

  Methods:
  - set(self, state: str) -> list[int]: Converts a string state to a list of integers.
  - move(self, tile: int): Moves the specified tile to the blank space.
  - is_solved(self) -> bool: Checks if the puzzle is in the solved state.
  - print_board(self): Prints the current state of the puzzle.
  - shuffle(self, k: int): Shuffles the puzzle to generate a random solvable configuration.
  - reset(self): Resets the puzzle to its initial state.
  """

  goal_state: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  adj_masks: list[list[int]] = [
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

  def __init__(self, state: str):
    """
    Initializes the EightPuzzle instance with the given state.

    Args:
    - state (str): The initial state of the puzzle.
    """
    
    self.state = self.set(state)
    self.statestr = ''.join(str(i) for i in self.state)
    self.adj_mask = self.adj_masks[self.state.index(0)]
    
  def set(self, state):
    """
    Converts a string state to a list of integers.

    Args:
    - state (str): The string representation of the state.

    Returns:
    - list[int]: The state as a list of integers.
    """

    if isinstance(state, str):
      state = ''.join(char for char in state if char.isdigit())
      if len(state) != 9:
        raise ValueError(f'filtered state {state} does not have 9 digits')
      return utils.str2intlist(state, max_len=9)
    
    raise ValueError(f'given argument is not a str')


  def move(self, tile: int):
    """
    Moves the specified tile to the blank space.

    Args:
    - tile (int): The tile to move.
    """
    # Implementation of move method...

  def is_solved(self):
    """
    Checks if the current board configuration matches the goal state.

    Returns:
    - bool: True if the puzzle is solved, False otherwise.
    """
    # Implementation of is_solved method...

  def print_board(self):
    """
    Prints the current state of the puzzle.
    """

    print(self.state[0:3])
    print(self.state[3:6])
    print(self.state[6:9])

  def shuffle(self, k: int):
    """
    Shuffles the puzzle to generate a random solvable configuration.

    Args:
    - k (int): The number of random moves to perform.
    """
    # Implementation of shuffle method...

  def reset(self):
    """
    Resets the puzzle to its initial state.
    """
    # Implementation of reset method...

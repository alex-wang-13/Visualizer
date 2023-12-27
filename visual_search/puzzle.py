import heapq
import utils

from random import choice, seed
from utils import Node

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

  def _get_neighbors(self, state: list[int]) -> list[list[int]]:
    """
    Get the neighboring states of the given state by swapping the blank tile (0) with adjacent tiles.

    Args:
    - state (list[int]): The current state represented as a list of integers.

    Returns:
    - list[list[int]]: A list of neighboring states obtained by swapping the blank tile with adjacent tiles.
    """

    # Get the index of the blank tile
    z_index: int = state.index(0)
    adj_indices: list[int] = [i for i, val in enumerate(self._adj_masks[z_index]) if val]

    # Generate list of neighbor states
    neighbors: list[list[int]] = []
    for index in adj_indices:
      copy = state.copy()
      copy[index], copy[z_index] = copy[z_index], copy[index]
      neighbors.append(copy)
    return neighbors
  
  def heuristic(self, state: list[int]):
    """
    Calculate the heuristic value (Manhattan distance) for the given state.

    Args:
    - state (list[int]): The current state represented as a list of integers.

    Returns:
    - int: The calculated heuristic value.
    """

    distance: int = 0
    for index, value in enumerate(state):
      # Manhattan distance heuristic
      x_i, y_i = index % 3, index // 3
      x_v, y_v = value % 3, value // 3
      distance += abs(x_i - x_v) + abs(y_i - y_v)

    return distance

  def solve_astar(self) -> list[list[int]]:
    """
    Solve the puzzle using the A* algorithm and return the path from the initial state to the goal state.

    Returns:
    - list[list[int]] or None: A list of states representing the path from the initial state to the goal state,
      or None if no path is found.
    """

    open_set: list[Node] = []
    closed_set: set[str] = set()

    start_node = Node(self.state)
    goal_node = Node(self.goal_state)

    heapq.heappush(open_set, (start_node.f, start_node))

    while open_set:
      current_node: Node = heapq.heappop(open_set)[1]

      if current_node.state == goal_node.state:
        path = []
        while current_node:
          path.append(current_node.state)
          current_node = current_node.parent
        
        return path[::-1]
      
      closed_set.add(current_node.statestr)

      for neighbor in self._get_neighbors(current_node.state):
        if ''.join(str(i) for i in neighbor) in closed_set:
          continue

        g = current_node.g + 1
        h = self.heuristic(neighbor)
        f = g + h

        new_node = Node(neighbor, current_node)

        if (f, new_node) not in open_set:
          heapq.heappush(open_set, (f, new_node))

    return None # No path is found
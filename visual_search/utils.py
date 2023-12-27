from sys import maxsize

num_tiles: int = 9

# Formatting functions
def str2intlist(s: str, max_len: int = maxsize) -> list[int]:
  """
  Converts a string of digits to a list of integers.
  
  Args:
  - s (str): The input string.
  - max_len (int, optional): The maximum length of the resulting list. Default is sys.maxsize.
  
  Returns:
  - list[int]: A list of integers extracted from the input string.
  
  Raises:
  - ValueError: If the input is not a string.
  """
  
  if not isinstance(s, str):
    raise ValueError(f'input arg {s} is not a str')
  
  # Clean string
  s = ''.join(char for char in s if s.isdigit())

  result: list[int] = list()
  for char, _ in zip(s, range(max_len)):
    try:
      result.append(int(char))
    except ValueError:
      raise ValueError(f'should not see this error')

  return result

class Node:
  def __init__(self, state, parent=None) -> None:
    self.state: list[int] = state
    self.statestr: str = ''.join(str(chr) for chr in state)
    self.parent = parent
    self.g = 0 # The current path cost
    self.h = 0 # The estimated future cost
    self.f = 0 # the total cost f = g + h

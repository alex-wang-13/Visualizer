# Eight Puzzle Solver

This Python application implements an Eight Puzzle Solver using the A* algorithm in conjunction with Pygame for visualization. The Eight Puzzle is a sliding puzzle consisting of eight numbered tiles arranged in a 3x3 grid. The goal is to rearrange the tiles from a given initial state to the goal state.

## How to Use
1. Clone the repository:
``` bash
git clone git@github.com:alex-wang-13/Visualizer.git
cd visual_search
```

2. Make sure you have all the libraries needed to run the program:
``` bash
pip install -r requirements_dev.txt
```

3. Run the program:
``` bash
python visual_search/main.py
```

4. Controls:
* Use the number keys 1 to 8 to move tiles (Empty space denoted by 0) and solve the puzzle.
* Press a to let the A* algorithm solve the puzzle automatically.
* Press s to shuffle the puzzle into a solvable state.
* Use the UP and DOWN arrow keys to adjust the solving speed.

5. Termination:
* Press ESC or q to exit the program.

## Components

EightPuzzle Class:
* Represents the Eight Puzzle and includes methods for moving tiles, solving the puzzle with the A* algorithm, and shuffling the puzzle.

TileGroup Class:
* Handles the visualization of the puzzle tiles using Pygame.

TextBox Class:
* Displays information and controls using Pygame, fetching text content from a specified file.

Speedometer Class:
* Visualizes and controls the solving speed of the A* algorithm.

## Controls File
* The controls and instructions are fetched from a file specified by the controls_fp variable.

## Acknowledgments
This project is based on the Eight Puzzle problem, a classic problem in artificial intelligence. The A* algorithm is utilized for efficient solving.

## Author

Alex Wang

## License
This project is licensed under the MIT License - see the LICENSE file for details.
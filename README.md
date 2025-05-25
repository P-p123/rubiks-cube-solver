# Rubik's Cube Solver

A project for solving and visualizing the Rubik's Cube using algorithmic approaches and a graphical user interface.

## Overview

This project provides a tool to solve a standard 3x3 Rubik's Cube and visualize both the cube and its solution steps. The main application is a desktop GUI built with Tkinter, enabling interactive cube input, random cube generation, and animated solution visualization. The core solver logic is based in part on open source code by Tom Begley, adapted under the MIT License.

## Features

- **Graphical User Interface (GUI):**  
  A Tkinter-based desktop app for easy cube interaction.
- **Visual Cube Display:**  
  Real-time 2D visualization of the current cube state.
- **Manual or Random Cube Input:**  
  Enter your own cube state or generate a valid random scramble.
- **Automated Solution:**  
  Fast solver (two-phase algorithm) finds optimal solutions for any valid cube.
- **Animated Solution Steps:**  
  Watch the cube update as each solution move is applied.
- **Error Handling:**  
  User-friendly messages for invalid inputs or unsolvable cubes.
- **Extensible & Readable Code Structure:**  
  Modular functions for state handling, visualization, and solver integration.

## My Contributions

While this project uses the robust two-phase cube-solving logic from Tom Begley's open source code, the following parts were **designed, written, and integrated by me**:

- Built the entire Tkinter GUI (`main.py`), including:
  - Cube visualization canvas
  - Input and randomization controls
  - Solution animation logic
  - Error and information dialogs
- Developed functions for:
  - Generating valid random scrambles and cube states
  - Parsing and validating user cube input
  - Applying moves and updating the cube state for visualization
- Integrated the solver with the GUI for seamless user experience
- Wrote comprehensive comments and documentation to make the code approachable for future contributors

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/P-p123/rubiks_solver.git
   cd rubiks_solver
   ```

2. **Set up environment:**  
   (If using Python, recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   python main.py
   ```

## Usage

- **Enter Cube State:**  
  Paste a 54-character string representing the cube (using U, R, F, D, L, B for face colors).
- **Load Cube:**  
  Click "Load Cube" to visualize your input.
- **Random Cube:**  
  Click "Random Cube" to get a solvable random scramble.
- **Visualize Solution:**  
  Click "Visualize Solution" to animate the solving process step by step.

## Project Structure

```
rubiks_solver/
├── main.py           # GUI and visualization logic (written by me)
├── cube_solver/
│   └── twophase/     # Two-phase algorithm (by Tom Begley)
├── requirements.txt
├── README.md
└── ...
```

## Attribution

Parts of the cube-solving algorithm are based on code from [Tom Begley’s Rubik's Cube Solver](https://github.com/tom-begeley/rubiks-cube-solver), used under the MIT License.  
See the LICENSE file for details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Tom Begley for the original two-phase Rubik's Cube solving algorithm
- The open-source community for resources and inspiration

---

_Feedback and suggestions are welcome!_
=======
# rubiks-cube-solver
>>>>>>> 12801e5b711ed2c8a3f862be7b7d4fd7f0c1f3d3

import tkinter as tk
from tkinter import messagebox
from cube_solver.twophase import solve
from cube_solver.twophase.cubes import FaceCube
import random

color_map = {'U': 'white', 'R': 'red', 'F': 'green', 'D': 'yellow', 'L': 'orange', 'B': 'blue'}

face_positions = {
    'U': (90, 0, 105, -20),
    'R': (180, 90, 225, 120),
    'F': (90, 90, 120, 120),
    'D': (90, 180, 120, 240),
    'L': (0, 90, 0, 120),
    'B': (270, 90, 270, 120)
}

def solved_facelets():
    return 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'

def random_scramble(length=20):
    moves = ['U', "U'", 'U2', 'D', "D'", 'D2', 'F', "F'", 'F2', 'B', "B'", 'B2', 'L', "L'", 'L2', 'R', "R'", 'R2']
    scramble = []
    prev = ''
    for _ in range(length):
        move = random.choice(moves)
        while prev and move[0] == prev[0]:
            move = random.choice(moves)
        scramble.append(move)
        prev = move
    return scramble

move_names = ['U', 'R', 'F', 'D', 'L', 'B']

def move_str_to_index(move):
    face = move[0]
    idx = move_names.index(face)
    if move.endswith("2"):
        return [idx, idx]
    elif move.endswith("'"):
        return [idx, idx, idx]
    else:
        return [idx]

def apply_moves_with_facecube(state, moves):
    from cube_solver.twophase.cubes import FaceCube
    fc = FaceCube(state)
    cc = fc.to_cubiecube()
    for move in moves:
        for mv in move_str_to_index(move):
            cc.move(mv)
    fc = cc.to_facecube()
    return fc.to_string()

def get_valid_random_state(max_attempts=100):
    for _ in range(max_attempts):
        scramble = random_scramble()
        facelets = apply_moves_with_facecube(solved_facelets(), scramble)
        try:
            solve(facelets)  # Will raise if invalid
            return facelets, scramble
        except Exception:
            continue
    raise RuntimeError("Failed to generate a valid random cube state.")

class CubeVisualizer:
    def __init__(self, root):
        self.root = root
        root.title("Rubik's Cube Visualizer")

        self.state = solved_facelets()

        tk.Label(root, text="Enter 54-char cube state:").pack()
        self.input_box = tk.Text(root, height=2, width=60)
        self.input_box.pack()
        self.input_box.insert("1.0", self.state)

        self.load_btn = tk.Button(root, text="Load Cube", command=self.load_cube)
        self.load_btn.pack()

        self.random_btn = tk.Button(root, text="Random Cube", command=self.load_random_cube)
        self.random_btn.pack()

        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()

        self.solve_btn = tk.Button(root, text="Visualize Solution", command=self.visualize_solution)
        self.solve_btn.pack()
        self.solve_btn.config(state='normal')

        self.draw_cube()

    def draw_face(self, stickers, x0, y0, face_name=None, label_x=None, label_y=None):
        size = 30
        for i, c in enumerate(stickers):
            x = x0 + (i % 3) * size
            y = y0 + (i // 3) * size
            self.canvas.create_rectangle(x, y, x + size, y + size, fill=color_map.get(c, 'black'), outline='black')
        if face_name and label_x is not None and label_y is not None:
            self.canvas.create_text(label_x, label_y, text=face_name, font=('Arial', 14, 'bold'))

    def draw_cube(self):
        self.canvas.delete("all")
        s = self.state
        for face, (x0, y0, label_x, label_y) in face_positions.items():
            idx = 'URFDLB'.index(face)
            stickers = s[idx*9:(idx+1)*9]
            self.draw_face(stickers, x0, y0, face, label_x, label_y)

    def load_cube(self):
        s = self.input_box.get("1.0", "end").strip().upper()
        if len(s) != 54 or any(c not in "URFDLB" for c in s):
            messagebox.showerror("Error", "Input must be exactly 54 characters with only U,R,F,D,L,B")
            return
        self.state = s
        self.draw_cube()
        self.solve_btn.config(state='normal')

    def load_random_cube(self):
        try:
            facelets, scramble = get_valid_random_state()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
        self.state = facelets
        self.input_box.delete("1.0", "end")
        self.input_box.insert("1.0", facelets)
        self.draw_cube()
        self.solve_btn.config(state='normal')
        messagebox.showinfo("Random Scramble", "Scramble: " + ' '.join(scramble))

    def visualize_solution(self):
        try:
            solution = solve(self.state)
            print("Solution:", solution)
        except Exception as e:
            messagebox.showerror("Error", f"Solver error: {e}")
            return

        moves = solution.strip().split()
        if not moves or (len(moves) == 1 and moves[0] == ''):
            messagebox.showinfo("Info", "No moves to animate (cube may be solved or unsolvable).")
            return

        state = self.state
        def animate_moves(i=0):
            nonlocal state
            if i >= len(moves):
                self.state = state
                self.draw_cube()
                messagebox.showinfo("Solved", "Cube is solved!")
                return
            self.state = state
            self.draw_cube()
            state = apply_moves_with_facecube(state, [moves[i]])
            self.root.after(700, lambda: animate_moves(i + 1))
        animate_moves()

if __name__ == "__main__":
    root = tk.Tk()
    app = CubeVisualizer(root)
    root.mainloop()  
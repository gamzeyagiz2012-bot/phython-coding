import random
import tkinter as tk

# Ekran Boyutları
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 600
BLOCK_SIZE = 30
ROWS = 20
COLS = 10

# Tetris Şekilleri ve Renkleri
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
]
COLORS = ["cyan", "yellow", "purple", "orange", "blue", "green", "red"]


class Tetris:

  def __init__(self, root):
    self.root = root
    self.root.title("Tetris")
    self.canvas = tk.Canvas(
        root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black"
    )
    self.canvas.pack()

    self.grid = [["" for _ in range(COLS)] for _ in range(ROWS)]
    self.current_piece = self.new_piece()

    # Tuş Atamaları
    self.root.bind("<Left>", lambda e: self.move(-1, 0))
    self.root.bind("<Right>", lambda e: self.move(1, 0))
    self.root.bind("<Down>", lambda e: self.move(0, 1))
    self.root.bind("<Up>", lambda e: self.rotate())

    self.update()

  def new_piece(self):
    shape = random.choice(SHAPES)
    color = random.choice(COLORS)
    return {
        "shape": shape,
        "color": color,
        "x": COLS // 2 - len(shape[0]) // 2,
        "y": 0,
    }

  def move(self, dx, dy):
    self.current_piece["x"] += dx
    self.current_piece["y"] += dy
    if not self.is_valid_position():
      self.current_piece["x"] -= dx
      self.current_piece["y"] -= dy
      if dy > 0:
        self.lock_piece()

  def rotate(self):
    old_shape = self.current_piece["shape"]
    self.current_piece["shape"] = [list(row) for row in zip(*old_shape[::-1])]
    if not self.is_valid_position():
      self.current_piece["shape"] = old_shape

  def is_valid_position(self):
    for r, row in enumerate(self.current_piece["shape"]):
      for c, val in enumerate(row):
        if val:
          x = self.current_piece["x"] + c
          y = self.current_piece["y"] + r
          if (
              x < 0
              or x >= COLS
              or y >= ROWS
              or (y >= 0 and self.grid[y][x] != "")
          ):
            return False
    return True

  def lock_piece(self):
    for r, row in enumerate(self.current_piece["shape"]):
      for c, val in enumerate(row):
        if val:
          x = self.current_piece["x"] + c
          y = self.current_piece["y"] + r
          if y < 0:
            self.root.destroy()
            return
          self.grid[y][x] = self.current_piece["color"]
    self.clear_rows()
    self.current_piece = self.new_piece()

  def clear_rows(self):
    self.grid = [row for row in self.grid if "" in row]
    while len(self.grid) < ROWS:
      self.grid.insert(0, ["" for _ in range(COLS)])

  def update(self):
    self.move(0, 1)
    self.draw()
    self.root.after(400, self.update)

  def draw(self):
    self.canvas.delete("all")
    for r in range(ROWS):
      for c in range(COLS):
        if self.grid[r][c] != "":
          self.canvas.create_rectangle(
              c * BLOCK_SIZE,
              r * BLOCK_SIZE,
              (c + 1) * BLOCK_SIZE,
              (r + 1) * BLOCK_SIZE,
              fill=self.grid[r][c],
              outline="gray",
          )
    if self.current_piece:
      for r, row in enumerate(self.current_piece["shape"]):
        for c, val in enumerate(row):
          if val:
            x = self.current_piece["x"] + c
            y = self.current_piece["y"] + r
            if y >= 0:
              self.canvas.create_rectangle(
                  x * BLOCK_SIZE,
                  y * BLOCK_SIZE,
                  (x + 1) * BLOCK_SIZE,
                  (y + 1) * BLOCK_SIZE,
                  fill=self.current_piece["color"],
                  outline="gray",
              )


if __name__ == "__main__":
  root = tk.Tk()
  game = Tetris(root)
  root.mainloop()
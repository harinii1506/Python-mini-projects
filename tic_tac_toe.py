import tkinter as tk
from tkinter import messagebox

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("360x430")
root.resizable(False, False)

# ---------------- BRIGHT THEMES ----------------
themes = {
    "Pink": {
        "bg": "#ffe6f0",
        "grid": "#ff1493",
        "x": "#ff0066",
        "o": "#800040"
    },
    "Red": {
        "bg": "#ffe6e6",
        "grid": "#cc0000",
        "x": "#ff0000",
        "o": "#800000"
    },
    "White": {
        "bg": "#ffffff",
        "grid": "#000000",
        "x": "#0066ff",
        "o": "#ff0000"
    },
    "Light Green": {
        "bg": "#eaffea",
        "grid": "#009933",
        "x": "#00cc66",
        "o": "#006633"
    }
}

current_theme = "White"

# ---------------- CANVAS ----------------
canvas = tk.Canvas(root, width=300, height=300, highlightthickness=0)
canvas.pack(pady=20)

# ---------------- GAME DATA ----------------
board = [""] * 9
current_player = "X"

cell_centers = [
    (50,50),(150,50),(250,50),
    (50,150),(150,150),(250,150),
    (50,250),(150,250),(250,250)
]

# ---------------- APPLY THEME ----------------
def apply_theme(name):
    global current_theme
    current_theme = name
    theme = themes[name]

    root.configure(bg=theme["bg"])
    canvas.configure(bg=theme["bg"])
    reset_game()

# ---------------- DRAW GRID ----------------
def draw_grid():
    theme = themes[current_theme]
    for row in range(3):
        for col in range(3):
            canvas.create_rectangle(
                col*100, row*100,
                col*100+100, row*100+100,
                outline=theme["grid"],
                width=2
            )

# ---------------- DRAW X / O ----------------
def draw_x(cx, cy):
    canvas.create_line(
        cx-25, cy-25, cx+25, cy+25,
        fill=themes[current_theme]["x"], width=5
    )
    canvas.create_line(
        cx+25, cy-25, cx-25, cy+25,
        fill=themes[current_theme]["x"], width=5
    )

def draw_o(cx, cy):
    canvas.create_oval(
        cx-28, cy-28, cx+28, cy+28,
        outline=themes[current_theme]["o"], width=5
    )

# ---------------- WHITE STRIKE ----------------
def white_strike(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill="#ffffff", width=6)

# ---------------- WIN PATTERNS ----------------
win_patterns = {
    (0,1,2):(20,50,280,50),
    (3,4,5):(20,150,280,150),
    (6,7,8):(20,250,280,250),
    (0,3,6):(50,20,50,280),
    (1,4,7):(150,20,150,280),
    (2,5,8):(250,20,250,280),
    (0,4,8):(20,20,280,280),
    (2,4,6):(280,20,20,280)
}

# ---------------- CHECK WIN ----------------
def check_winner():
    for pattern, coords in win_patterns.items():
        a,b,c = pattern
        if board[a] == board[b] == board[c] != "":
            white_strike(*coords)
            root.after(300, lambda:
                messagebox.showinfo("Game Over", f"Player {board[a]} Wins!")
            )
            root.after(800, reset_game)
            return True
    return False

def check_draw():
    if "" not in board:
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset_game()

# ---------------- CLICK HANDLER ----------------
def click(event):
    global current_player

    col = event.x // 100
    row = event.y // 100
    index = row * 3 + col

    if index < 0 or index > 8 or board[index] != "":
        return

    board[index] = current_player
    cx, cy = cell_centers[index]

    if current_player == "X":
        draw_x(cx, cy)
        current_player = "O"
    else:
        draw_o(cx, cy)
        current_player = "X"

    if not check_winner():
        check_draw()

# ---------------- RESET ----------------
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    canvas.delete("all")
    draw_grid()

canvas.bind("<Button-1>", click)

# ---------------- MENU BAR ----------------
menu_bar = tk.Menu(root)

game_menu = tk.Menu(menu_bar, tearoff=0)
game_menu.add_command(label="Restart", command=reset_game)
game_menu.add_separator()
game_menu.add_command(label="Exit", command=root.destroy)

theme_menu = tk.Menu(menu_bar, tearoff=0)
theme_menu.add_command(label="Pink", command=lambda: apply_theme("Pink"))
theme_menu.add_command(label="Red", command=lambda: apply_theme("Red"))
theme_menu.add_command(label="White", command=lambda: apply_theme("White"))
theme_menu.add_command(label="Light Green", command=lambda: apply_theme("Light Green"))

menu_bar.add_cascade(label="Game", menu=game_menu)
menu_bar.add_cascade(label="Themes", menu=theme_menu)

root.config(menu=menu_bar)

# ---------------- START ----------------
apply_theme("White")
root.mainloop()
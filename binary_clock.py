import tkinter as tk
import time

root = tk.Tk()
root.title("Binary Clock")
canvas = tk.Canvas(root, bg="black")
canvas.pack(fill="both", expand=True)

show_clock = False
button_coords = (0,0,0,0)

def draw_clock():
    global button_coords
    canvas.delete("all")

    w = canvas.winfo_width()
    h = canvas.winfo_height()

    scale = 0.4
    cols = 6
    rows = 4
    grid_width = w * scale
    grid_height = h * scale
    startX = (w - grid_width) / 2
    startY = h * 0.15
    spacingX = grid_width / (cols - 1)
    spacingY = grid_height / (rows - 1)
    r = min(spacingX, spacingY) * 0.25

    now = time.localtime()
    digits = [
        now.tm_hour // 10, now.tm_hour % 10,
        now.tm_min // 10, now.tm_min % 10,
        now.tm_sec // 10, now.tm_sec % 10
    ]

    # ---- DRAW CIRCLES ----
    for col in range(cols):
        binary = format(digits[col], "04b")  # MSB first
        for row in range(rows):
            x = startX + col * spacingX
            y = startY + row * spacingY
            fill = "lime" if binary[row] == "1" else "#002200"
            canvas.create_oval(
                x - r, y - r, x + r, y + r,
                outline="lime",
                fill=fill
            )

    # LEFT LABELS
    values = ["8", "4", "2", "1"]
    for i in range(4):
        y = startY + i * spacingY
        canvas.create_text(startX - spacingX * 0.7, y,
                           text=values[i], fill="white",
                           font=("Arial", max(int(r*1.2), 8)))

    # BOTTOM LABELS
    labels = ["H","H","M","M","S","S"]
    for i in range(6):
        x = startX + i * spacingX
        canvas.create_text(x, startY + grid_height + spacingY * 0.6,
                           text=labels[i], fill="white",
                           font=("Arial", max(int(r*1.2), 8)))

    # TITLE
    canvas.create_text(w/2, h*0.05,
                       text="Binary Clock", fill="white",
                       font=("Arial", int(w*0.04), "bold"))

    # DIGITAL CLOCK
    if show_clock:
        t = time.strftime("%H:%M:%S")
        digitalY = startY + grid_height + spacingY * 1.8
        canvas.create_text(w/2, digitalY,
                           text=t, fill="lime",
                           font=("Arial", int(w*0.06)))

    # BUTTON
    bx1 = w*0.35
    by1 = startY + grid_height + spacingY * 2.4
    bx2 = w*0.65
    by2 = startY + grid_height + spacingY * 3.0
    button_coords = (bx1, by1, bx2, by2)
    canvas.create_rectangle(bx1, by1, bx2, by2, fill="white")
    text = "Hide Digital Clock" if show_clock else "Show Digital Clock"
    canvas.create_text((bx1+bx2)/2, (by1+by2)/2,
                       text=text, fill="black",
                       font=("Arial", int(w*0.02)))

    root.after(500, draw_clock)

def toggle(event):
    global show_clock
    bx1, by1, bx2, by2 = button_coords
    if bx1 <= event.x <= bx2 and by1 <= event.y <= by2:
        show_clock = not show_clock

canvas.bind("<Button-1>", toggle)
draw_clock()
root.mainloop()

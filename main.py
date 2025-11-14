import tkinter as tk
import math

# Function for button clicks
def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(screen_var.get())
            screen_var.set(result)
        except Exception:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    elif text == "⌫":
        screen_var.set(screen_var.get()[:-1])
    elif text == "√":
        try:
            value = float(screen_var.get())
            screen_var.set(str(math.sqrt(value)))
        except:
            screen_var.set("Error")
    elif text == "x²":
        try:
            value = float(screen_var.get())
            screen_var.set(str(value ** 2))
        except:
            screen_var.set("Error")
    elif text == "%":
        try:
            value = float(screen_var.get())
            screen_var.set(str(value / 100))
        except:
            screen_var.set("Error")
    elif text == "Mode":
        toggle_mode()
    else:
        screen_var.set(screen_var.get() + text)

# Toggle dark/light mode
def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.config(bg="#222222")
        screen.config(bg="#333333", fg="#FFFFFF", insertbackground="white")
        for b in button_list:
            b.config(bg="#444444", fg="#FFFFFF", activebackground="#555555")
    else:
        root.config(bg="#F0F0F0")
        screen.config(bg="#FFFFFF", fg="#000000", insertbackground="black")
        for b in button_list:
            b.config(bg="#E0E0E0", fg="#000000", activebackground="#D0D0D0")

# Main Window
root = tk.Tk()
root.title("Advanced Python Calculator with Dark/Light Mode")
dark_mode = True  # default mode

# Entry Screen
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

# Buttons Layout
buttons = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "x²"],
    ["1", "2", "3", "-", "%"],
    ["0", ".", "C", "+", "⌫"],
    ["=", "Mode"]
]

button_list = []

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn in row:
        b = tk.Button(frame, text=btn, font="lucida 15 bold", padx=20, pady=10)
        b.pack(side=tk.LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)
        button_list.append(b)

toggle_mode()  # apply default dark mode

root.mainloop()

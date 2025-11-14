import tkinter as tk
import math

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

    else:
        screen_var.set(screen_var.get() + text)


root = tk.Tk()
root.title("Advanced Python Calculator")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "x²"],
    ["1", "2", "3", "-", "%"],
    ["0", ".", "C", "+", "⌫"],
    ["="]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn in row:
        b = tk.Button(frame, text=btn, font="lucida 15 bold", padx=20, pady=10)
        b.pack(side=tk.LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)

root.mainloop()

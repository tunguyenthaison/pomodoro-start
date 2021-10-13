from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# Creating a new window and configurations
window = Tk()
window.title('Simplex Pomodoro')
window_height = 446
window_width = 420
window.minsize(width=window_width, height=window_height)
window.config(padx=100, pady=100, bg=YELLOW)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int(screen_width / 2) - int(window_width / 2)
y_coordinate = int(screen_height / 2) - int(window_height / 2)
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))


tomato = PhotoImage(file='tomato.png')

# Canvas
canvas = Canvas(width=window_width, height=window_height, bg=YELLOW, highlightthickness=0)
canvas.create_image(window_width//4, window_height//4+10, image=tomato)
canvas.create_text(window_width//4, window_height//4+30, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.pack()

# Main loop
window.mainloop()
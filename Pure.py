from tkinter import *
import time
from timeobjectdown import TimeObjectDown
from timeobjectdown import get_current

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- FUNCTIONS HELPERS ------------------------------- #

def get_time_text(count):
    minutes = int(count // 60)
    seconds = count - minutes * 60
    if minutes < 10:
        string_minutes = '%02d' % minutes
    else:
        string_minutes = str(minutes)

    if seconds < 10:
        string_seconds = '%02d' % seconds
    else:
        string_seconds = str(seconds)
    time_text = f"{string_minutes}:{string_seconds}"
    return time_text


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    time_to_print = get_time_text(count)
    canvas.itemconfig(timer_text, text=time_to_print)
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:



# ---------------------------- UI SETUP ------------------------------- #

# Creating a new window and configurations
window = Tk()
window.title('Simplex Pomodoro')
window_height = 446
window_width = 420
window.minsize(width=window_width, height=window_height)
window.config(padx=10, pady=10, bg=YELLOW)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int(screen_width / 2) - int(window_width / 2)
y_coordinate = int(screen_height / 2) - int(window_height / 2)
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# ----------------------------------------------------------- #
# Frame at the top
topFrame = Frame(window, width=window_width, height=90, bg=YELLOW,
                 highlightbackground="red", highlightthickness=1, padx=90)
topFrame.pack()
# ----------------------------------------------------------- #



# ----------------------------------------------------------- #
# Frame at the center
centerFrame = Frame(window, width=window_width, height=223 + 20, bg=YELLOW,
                    highlightbackground="red", highlightthickness=1, padx=90, pady=10)
tomato = PhotoImage(file='tomato.png')

# Canvas
canvas = Canvas(centerFrame, width=window_width // 2, height=window_height // 2 + 20, bg=YELLOW,
                highlightbackground="blue", highlightthickness=1)
canvas.create_image(window_width // 4, window_height // 4, image=tomato)

timer_text = "00:00"
show_clock = canvas.create_text(window_width // 4, window_height // 4 + 30, text=timer_text, fill="white",
                                font=(FONT_NAME, 32, "bold"), tag="clock")
canvas.pack()
centerFrame.pack()
# ----------------------------------------------------------- #


# ----------------------------------------------------------- #
# Frame at the bottom
bottomFrame = Frame(window, width=window_width // 2, height=20, bg=YELLOW,
                    highlightbackground="blue", highlightthickness=1, padx=90, pady=10)
bottomFrame.pack()
# ----------------------------------------------------------- #

def time_action(time_amount):
    time_object = TimeObjectDown(time_amount)
    # while time_object.get_minutes() > 0 or time_object.get_seconds() > 0:
    while time_object.get_timelapse() >= 0:
        time_string = time_object.get_text()
        show_clock = canvas.create_text(window_width // 4, window_height // 4 + 30, text=timer_text, fill="white",
                                        font=(FONT_NAME, 32, "bold"), tag="clock")
        canvas.update()
        canvas.pack()
        canvas.delete("clock")

    canvas.update()
    canvas.pack()
    canvas.delete("clock")


# Variables to keep track of the loop
END_OF_COUNTDOWN = False


# END_OF_FOCUS = False
# END_OF_SHORT_BREAK = False
# END_OF_LONG_BREAK = False


def btnAction(btnName):
    newButton = Button(bottomFrame, text=btnName, bg="white", font=(FONT_NAME, 10, "bold"),
                       command=btnClicked)
    newButton.pack()


def clearFrame(frame):
    # destroy all widgets from frame
    for widget in frame.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    frame.pack_forget()
    END_OF_COUNTDOWN == False


# Buttons
def btnClicked():
    time_action(0.1)


def workFocus():
    btnAction('Start Focusing')
    END_OF_COUNTDOWN = True


def shortBreak():
    btnAction('Start Short Break')
    END_OF_COUNTDOWN = True


def longBreak():
    btnAction('Start Long Break')


if END_OF_COUNTDOWN == False:
    workFocus()
else:
    clearFrame(bottomFrame)
    shortBreak()

# Main loop
window.mainloop()

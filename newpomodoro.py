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

START = False
RESUME = False
PAUSE = False
reps = 0
work_reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def get_current():
    return time.time()


class TimeObjectDown:
    def __init__(self, init):
        self.max = init * 60
        self.start = time.time()
        self.remain = self.max - self.start

    def reset_time(self):
        self.start = time.time()
        self.remain = self.max - self.start

    def get_timelapse(self):
        return self.max - int(get_current() - self.start)

    def get_minutes(self):
        return int(self.get_timelapse() // 60)

    def get_seconds(self):
        return int(self.get_timelapse()) - self.get_minutes() * 60

    def get_text(self):
        seconds = self.get_seconds()
        minutes = self.get_minutes()
        if minutes < 10:
            minutes = '%02d' % minutes
        else:
            minutes = str(minutes)

        if seconds < 10:
            seconds = '%02d' % seconds
        else:
            seconds = str(seconds)

        time_text = f"{minutes}:{seconds}"
        return time_text


def get_time_text(count):
    minutes = int(count // 60)
    seconds = count - minutes * 60
    if minutes < 10:
        minutes = '%02d' % minutes
    else:
        minutes = str(minutes)

    if seconds < 10:
        seconds = '%02d' % seconds
    else:
        seconds = str(seconds)
    time_text = f"{minutes}:{seconds}"
    return time_text


def reset_timer():
    window.after_cancel(timer)
    global reps
    global work_reps
    reps = 0
    work_reps = 0
    timer_Label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="✔︎" * work_reps)


def start_timer():
    global reps
    global work_reps
    global timer
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # work_sec = 4
    # short_break_sec = 3
    # long_break_sec = 5
    if reps % 8 == 7:
        count_down(long_break_sec)
        timer_Label.config(text="Long Break", fg=RED)
    elif (reps % 8) % 2 == 0:
        count_down(work_sec)
        timer_Label.config(text="Work", fg=PINK)
    else:
        count_down(short_break_sec)
        timer_Label.config(text="Short Break", fg=GREEN)


    reps += 1
    if (reps % 8) % 2 == 0:
        work_reps += 1
    # print(f"work_reps = {work_reps}")
    # print(f"reps = {reps}")



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global work_reps
    global reps

    text_to_print = get_time_text(count)
    canvas.itemconfig(timer_text, text=text_to_print)
    if count > 0:
        global timer
        # print(count)
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_marks.config(text="✔︎" * work_reps)




#
# def count_down_time(count):
#     canvas
#     time_object = TimeObjectDown(count)
#     if time_object.get_minutes() <= count:
#         time_string = time_object.get_text()
#         print(time_string)
#         window.after(1000, count_down_time, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

# Creating a new window and configurations
window = Tk()
window.title('Simplex Pomodoro')
window_height = 446
window_width = 420
window.minsize(width=window_width, height=window_height)
window.config(padx=100, pady=100, bg=YELLOW)

# def say_something(thing1, thing2):
#     print(thing1)
#     print(thing2)
#
# window.after(1000, say_something, "Hello", "Bullshit")

# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
# x_coordinate = int(screen_width / 2) - int(window_width / 2)
# y_coordinate = int(screen_height / 2) - int(window_height / 2)
# window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

tomato = PhotoImage(file='tomato.png')

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=1)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# A Label for Timer
# topFrame = Frame(window, height=10, width=10, bg=YELLOW, highlightbackground="red", highlightthickness=1, padx=0, pady=0)
# topFrame.grid(row=0, column=0)
timer_Label = Label(window, text="Timer", font=(FONT_NAME, 32, "bold"), bg=YELLOW, fg=GREEN, highlightthickness=0)
timer_Label.grid(row=0, column=1)


# Buttons
def btnStartAction():
    global reps
    count_down(WORK_MIN * 60)


    # print(_START)
    # if _START is False:
    #     _START = True
    #     count_down(WORK_MIN*60)
        # if (btnStart['text'] == 'Start' or btnStart['text'] == 'Resume'):
        #     btnStart['text'] = 'Pause'
        # elif btnStart['text'] == 'Pause':
        #     btnStart['text'] = 'Resume'
    # else:
    pass

def btnPauseAction():
    pass

def btnResumeAction():
    pass

def btnResetAction():
    btnReset['text'] = 'Reset'
    global reps
    global work_reps
    reps = 0
    work_reps = 0


# # calls action() when pressed
btnStart = Button(text="Start", highlightthickness=0, command=start_timer)
btnStart.grid(row=2, column=0)

btnReset = Button(text="Reset", highlightthickness=0, command=reset_timer)
btnReset.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
check_marks.grid(row=3, column=1)

# count_down(WORK_MIN)

# time_object = TimeObjectDown(WORK_MIN)
# while time_object.get_minutes() <= WORK_MIN:
#     time_string = time_object.get_text()
#     show_clock = canvas.create_text(window_width // 4, window_height // 4 + 30, text=time_string, fill="white",
#                                     font=(FONT_NAME, 32, "bold"), tags="clock")
#     canvas.update()
#     canvas.pack()
#     canvas.delete("clock")


# Main loop
window.mainloop()

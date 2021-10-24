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

reps = 0
work_reps = 0
timer = None
START = False
PAUSE = False
CURRENT_PAUSE_count = 0
RESUME = False
canReset = False

# ---------------------------- FUNCTIONS ------------------------------- #
def get_time_text(count):
    # return strings of time representation of count
    minutes = int(count // 60)
    seconds = count - minutes * 60
    if minutes < 10:
        str_minutes = '%02d' % minutes
    else:
        str_minutes = str(minutes)
    if seconds < 10:
        str_seconds = '%02d' % seconds
    else:
        str_seconds = str(seconds)
    time_text = f"{str_minutes}:{str_seconds}"
    return time_text


def count_down(count):
    global PAUSE
    global CURRENT_PAUSE_count
    global work_reps
    global reps
    timer_text = get_time_text(count)
    canvas.itemconfig(show_clock, text=timer_text)

    if PAUSE is False:
        if count > 0:
            global timer
            timer = window.after(1000, count_down, count - 1)
            print(count)
            print(f"PAUSE = {PAUSE}, START = {START}, RESUME = {RESUME}, CURRENT = {CURRENT_PAUSE_count}")
            print(f"reps = {reps}, work_reps = {work_reps}")
        else:
            start_timer()
    else:
        CURRENT_PAUSE_count = count


# ---------------------------- TIMER PAUSE ------------------------------- #


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global START
    global PAUSE
    global CURRENT_PAUSE_count
    global RESUME
    window.after_cancel(timer)
    canvas.itemconfig(show_clock, text="00:00")
    global reps
    global work_reps
    reps = 0
    work_reps = 0

    timer = None
    START = False
    PAUSE = False
    CURRENT_PAUSE_count = 0
    RESUME = False

    timer_Label.config(text="TIMER", fg=GREEN)



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global canReset
    canReset = True
    global reps
    global work_reps
    global PAUSE
    global START
    global RESUME
    global CURRENT_PAUSE_count
    # work_sec = WORK_MIN * 60
    # short_break_sec = SHORT_BREAK_MIN * 60
    # long_break_sec = LONG_BREAK_MIN * 60
    work_sec = 25
    short_break_sec = 5
    long_break_sec = 20
    if RESUME is False:
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

    else:
        count_down(CURRENT_PAUSE_count)
        RESUME = False
        CURRENT_PAUSE_count = 0




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
# Creating a new window and configurations
window = Tk()
window.title('Simplex Pomodoro')
window_height = 446
window_width = 535
window.minsize(width=window_width, height=window_height)
window.config(padx=50, pady=50, bg=YELLOW)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int(screen_width / 2) - int(window_width / 2)
y_coordinate = int(screen_height / 2) - int(window_height / 2)
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
# Creating a new window and configurations
tomato = PhotoImage(file='tomato.png')

# Label
timer_Label = Label(window, text="Timer", font=(FONT_NAME, 26, "bold"), width=11, height=1,
                    bg=YELLOW, fg=GREEN, highlightthickness=0, pady=10)
timer_Label.grid(row=0, column=1)

# Canvas
canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(110, 112, image=tomato)
show_clock = canvas.create_text(window_width // 4 - 20, window_height // 4 + 25, text="00:00", fill="white",
                                font=(FONT_NAME, 36, "bold"), tags="clock")
canvas.grid(row=2, column=1)


def startFocusing_btn():
    global START
    global PAUSE
    global CURRENT_PAUSE_count
    global RESUME
    if button_l['text'] == "Start Focusing": # That means START = False when clicked
        START = True
        PAUSE = False
        RESUME = False
        button_l['text'] = 'Pause'
        start_timer()
    elif button_l['text'] == "Pause":
        PAUSE = True
        START = False
        RESUME = False
        button_l['text'] = "Resume"
    elif button_l['text'] == "Resume":
        RESUME = True
        START = False
        PAUSE = False
        button_l['text'] = 'Pause'
        start_timer()





button_l = Button(text="Start Focusing", bg='red', width=8, height=1,
                  command=startFocusing_btn, highlightthickness=0, highlightbackground=YELLOW)
button_l.grid(row=3, column=0)


def resetTimer_btn():
    global canReset
    if canReset is True:
        reset_timer()
        button_l['text'] = "Start Focusing"
        canReset = False



button_reset = Button(text="Reset", width=8, height=1, bg='#ffb3fe',
                command=resetTimer_btn, highlightthickness=0, highlightbackground=YELLOW)
button_reset.grid(row=3, column=2)

# Main loop
window.mainloop()

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
def get_current():
    return time.time()


#
#
# class TimeObject:
#
#     def __init__(self, init):
#         self.start = time.time()
#
#     def reset_time(self):
#         self.start = time.time()
#
#     def get_timelapse(self):
#         return int(get_current() - self.start)
#
#     def get_minutes(self):
#         return int(self.get_timelapse() // 60)
#
#     def get_seconds(self):
#         return int(self.get_timelapse()) - self.get_minutes() * 60
#
#     def get_text(self):
#         seconds = self.get_seconds()
#         minutes = self.get_minutes()
#         if minutes < 10:
#             minutes = '%02d' % minutes
#         else:
#             minutes = str(minutes)
#
#         if seconds < 10:
#             seconds = '%02d' % seconds
#         else:
#             seconds = str(seconds)
#
#         time_text = f"{minutes}:{seconds}"
#         return time_text


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
canvas.create_image(window_width // 4, window_height // 4 + 10, image=tomato)

time_object = TimeObjectDown(WORK_MIN)
while time_object.get_minutes() <= WORK_MIN:
    time_string = time_object.get_text()
    show_clock = canvas.create_text(window_width // 4, window_height // 4 + 30, text=time_string, fill="white",
                                    font=(FONT_NAME, 32, "bold"), tags="clock")


    # # Buttons
    # def action():
    #     pass
    # # calls action() when pressed
    # button = Button(text="Calculate", command=action)
    # button.place(0,0)
    #
    # canvas.update()
    # canvas.pack()
    # canvas.delete("clock")





# Main loop
window.mainloop()

from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

TICK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    btn_start.config(state= "active")
    tick_label.config(text="")
    timer_label.config(text="Let's start")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    btn_start.config(state="disabled")
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)  # Long break after 4 work sessions
        timer_label.config(text="Long break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)  # Short break after work
        timer_label.config(text="Short break", fg=PINK)
    else:
        count_down(work_sec)  # Work session
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    if count >= 0:
        count_minute = str(floor(count/60)).zfill(2)  #360segundos/60 = 6 minutos
        count_second = str(count % 60).zfill(2)

        canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}") # Args -> 1st: element of the canvas to modify, 2nd: attribute
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            tick_label.config(text=tick_label.cget("text") + " ✔")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW) 
window.minsize(400, 400)

# Rows
window.rowconfigure(0, weight=3)
window.rowconfigure(1, weight=6)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=2)

# Columns
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=1)

# Timer label
timer_label = Label(text="Let's start", font=("Courier New", 20, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1, sticky="s")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image = tomato) # half of the values (to get in the center)
timer_text = canvas.create_text(100, 130, text = "0:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Botones
btn_start = Button(text="Start", command=start_timer)
btn_start.grid(row=2, column=0, sticky="e")
btn_reset = Button(text="Reset", command=reset_timer)
btn_reset.grid(row=2, column=2, sticky="w")

# Ticks
tick_label = Label(text="", bg=YELLOW, fg=GREEN, font = (FONT_NAME, 12, "bold"))
tick_label.grid(row=3, column=1, sticky="n")

window.mainloop()

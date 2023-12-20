import time
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 1
check = "✔"
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    if count == 0 and reps < 8:
        reps += 1
        if reps % 2 == 0:
            new = int(reps / 2) * check
            check_label.config(text=new)
        start_count()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_count():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps > 9:
        return
    elif reps == 0 or reps == 1 or reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="Work")
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text='Timer', fg=GREEN, background=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="start", bg="white", command=start_count)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="white", command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()

from _tkinter import *
import math

# ---- Constants ----- #
WORK_MIN = 25
SHORT_BR = 5
LONG_BR = 20
reps = 4
timer = None

# ---- Timer Reset ---- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_num, text="00:00")
    title_label.config(text="Timer")
    marks.config(text="")
    global reps
    reps = 0
    
# ---- Timer Mech ---- #
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_br_sec = SHORT_BR * 69
    long_br_sec = LONG_BR * 60
    
    if reps % 8 ==0:
        countdown(long_br_sec)
        title_label.config(text="Break")
    elif reps % 2 == 0:
        countdown(short_br_sec)
        title_label.config(text="Break")
    else:
        countdown(work_sec)
        title_label.config(text="WORK")
    
# ---- CountDown ---- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        
    canvas.itemconfig(timer_num, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)  
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "#"
        marks.config(text=marks)        
        
# ---- UI Setup ---- #
window = Tk()
window.title("Productivity Timer")
window.config(padx=50, pady=50)

title_label = Label(text="Timer", font=("Courier", 50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=100, height=100, highlightthickness=0)
timer_num = canvas.create_text(75, 75, text="00:00", fill="Black", font=("Courier", 35, "bold"))
canvas.grid()

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

marks = Label(text="#")
marks.grid(column=1, row=3)

window.mainloop()
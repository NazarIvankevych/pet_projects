from tkinter import *
import math
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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    title_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))


# ---------------------------- TIMER MECHANISM ------------------------------- #
# Counting repeats and make the exsact break for that repeat
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    """
    After 1st repeat - 5 minutes break
    After 2nd repeat - 20 minutes break
    After 3rd repeat - 5 minutes
    etc.
    """
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Take a long break", fg=RED, bg=YELLOW, font=(FONT_NAME, 35))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config( text="Take a short break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 35))
    else:
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    # Make a counting of minutes and seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # Draw it
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    title_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        title_label.config(text=f"You need a break", fg=YELLOW, bg=RED, font=(FONT_NAME, 35))
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "V"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=105, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)
# Set up image in the screen and text
canvas = Canvas(height=360, width=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(150, 180, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Buttons
start_bnt = Button(text="Start", font=(FONT_NAME, 15), highlightthickness=0, bg=GREEN, fg="white", command=start_timer)
reset_bnt = Button(text="Reset", font=(FONT_NAME, 15), highlightthickness=0, bg=RED, fg="white", command=reset_timer)
start_bnt.grid(column=0, row=2, pady=10)
reset_bnt.grid(column=2, row=2, pady=10)
# Check marks
check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"), highlightthickness=2)
check_marks.grid(column=1, row=3)

window.mainloop()
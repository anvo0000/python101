from tkinter import Tk, Canvas, PhotoImage, Label, Button
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.3 # 25
SHORT_BREAK_MIN = 0.1 #5
LONG_BREAK_MIN = 0.2# 20
CHECK_MARK = "√"
reps = 0
global_timer = None # global global_timer and set it as None, need define it for using in reset_clicked function

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_clicked():
    global reps
    reps = 0
    window.after_cancel(global_timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")

    # pass


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    reps += 1

    if reps % 2 != 0: # working session, they are the 1st, 3rd, 5th, 7th ... reps
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        print(f"reps={reps} - Working session - {work_sec}")
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
        print(f"reps={reps} - Long Break session - {long_break_sec}")
    else:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
        print(f"reps={reps} - Short Break session - {short_break_sec}")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = int(round(count/60, 0))
    count_sec = count % 60
    global global_timer # global global_timer and set it as None

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count>0:
        # window.after() is the func to do timer in Tkinter
        global_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        if reps % 2 == 0:

            number_of_checked = int(reps/2)
            print(f"-------TEST number_of_checked {number_of_checked}")
            check_label.config(text=CHECK_MARK * number_of_checked)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.config()

#row 0
timer_label =  Label(text="Timer",fg=GREEN,bg=YELLOW, font=("Aral", 30, "bold"))
timer_label.grid(row=0, column=1)

#row 1
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
# count_down(5)

# row 2
start_button = Button(text="Start", bg=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, command=reset_clicked)
reset_button.grid(row=2, column=2)

# row 3
check_label =  Label(fg=GREEN, bg=YELLOW, font=("Aral", 15, "bold"))
check_label.grid(row=3, column=1)

window.mainloop()
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
"""
This program will first copy FILE TO WORDS_TO_LEARN,
Load WORDS_TO_LEARN to data frame, and convert it to a word_list.
When user remember a word and click on "Checked" button, it will remove that pair of word from WORDS_TO_LEARN.
Every card will stay on screen 3 seconds,
    if users didn't click on Checked button, it will flipt the card to show English meaning.
"""

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import Tk, Canvas, PhotoImage, Button, Entry, Label, messagebox
import pandas as pd
import random
import os
import shutil
# ---------------------------- functions ------------------------------- #
FILE = "data/french_words.csv"
WORDS_TO_LEARN = "data/words_to_learn.csv"
FRONT_LANG = "French"
BACK_LANG = "English"

# We can use try except to check if file not exists
print(f"LOG: data file from '{FILE}'")
if not os.path.isfile(WORDS_TO_LEARN):
    shutil.copy(FILE, WORDS_TO_LEARN)


data = pd.read_csv(WORDS_TO_LEARN)
word_list = data.to_dict(orient='records') # Sample word_list = [{'French': 'attendez', 'English': 'Wait'},{}]
current_word = {} # define the global variable
flip_timer = None # define the global variable, it will be defined later in the UI setup
words_to_learn = []


def pick_a_word():
    global current_word # the global variable, the first define at line 16
    global flip_timer
    window.after_cancel(flip_timer) # new word choose, then cancel the previous timer
    current_word = random.choice(word_list)
    print(f"The GLOBAL current_word: {current_word}")
    canvas.itemconfig(title_text, text=FRONT_LANG)
    canvas.itemconfig(word_text, text=current_word[FRONT_LANG])
    flip_timer = window.after(3000, flip_card) # starting a new timer, until the next word was chose.

def checked():
    word_list.remove(current_word)
    print(f"len(word_list) {len(word_list)}")

    new_data = pd.DataFrame(word_list)
    new_data.to_csv(WORDS_TO_LEARN, index=False) #save back to file
    pick_a_word()

def flip_card():
    canvas.itemconfig(title_text, text=BACK_LANG)
    canvas.itemconfig(word_text, text=current_word[BACK_LANG])
    canvas.itemconfig(canvas_background_img, image=back_img)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card) # timer, after 3000 milliseconds (3seconds) the window will call flip_card func

#row 0
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)
canvas_background_img = canvas.create_image(400, 263, image=front_img) #the app starts with the front image

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = canvas.create_text(400,150,text="Title", font=("Ariel",40, "italic"))
word_text = canvas.create_text(400,263,text="French word", font=("Arial",60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#wrong img - wrong_button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=pick_a_word)
wrong_button.grid(row=1, column=0)

# right_img - right_button
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=checked)
right_button.grid(row=1, column=1)


pick_a_word() # pick a random word when the app first load.

window.mainloop()
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
waiting_to_flip = None

# ---------------------------- PANDAS ------------------------------- #

data = pandas.read_csv("./data/french_words.csv")
vocabulary_to_learn = data.to_dict(orient="records")

# ---------------------------- NEXT CARD ------------------------------- #


def next_card():
    global waiting_to_flip
    if waiting_to_flip:
        window.after_cancel(waiting_to_flip)

    word_pair = random.choice(vocabulary_to_learn)
    front = {'img': card_front_img, 'lang': 'French', 'word': word_pair['French'], 'fill': 'black'}
    back = {'img': card_back_img, 'lang': 'English', 'word': word_pair['English'], 'fill': 'white'}

    flip_card(front)
    waiting_to_flip = window.after(3000, flip_card, back)

# ---------------------------- FLIP CARD ------------------------------- #


def flip_card(side):
    flashcard.itemconfig(image, image=side['img'])
    flashcard.itemconfig(title, text=side['lang'], fill=side['fill'])
    flashcard.itemconfig(word, text=side['word'], fill=side['fill'])


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Learn French with Flashcards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

# GRID
# row 1
flashcard = Canvas(width=830, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
image = flashcard.create_image(415, 265)

title = flashcard.create_text(400, 150, text="", font=("Helvetic", 35, "italic"))
word = flashcard.create_text(400, 265, text="", font=("Helvetica", 55, "bold"))

flashcard.grid(row=0, column=0, columnspan=2)

# row 2
wrong_btn_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

right_btn_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, command=next_card)
right_btn.grid(row=1, column=1)

next_card()
window.mainloop()

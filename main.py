from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Learn French with Flashcards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# GRID
# row 1
flashcard = Canvas(width=830, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
flashcard.create_image(415, 265, image=card_front_img)

title = flashcard.create_text(400, 150, text="Title", font=("Helvetic", 35, "italic"))
word = flashcard.create_text(400, 265, text="Word", font=("Helvetica", 55, "bold"))

flashcard.grid(row=0, column=0, columnspan=2)

# row 2
wrong_btn_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0)
wrong_btn.grid(row=1, column=0)

right_btn_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0)
right_btn.grid(row=1, column=1)

window.mainloop()

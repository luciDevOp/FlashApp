from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("C:/Users/ungur/PycharmProjects/FlashApp/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("C:/Users/ungur/PycharmProjects/FlashApp/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def is_known():
    to_learn.remove(current_card)
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_word()


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(current_image, image=front_card)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(current_image, image=back_card)


window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.title("FlashCard")
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_card = PhotoImage(file="C:/Users/ungur/PycharmProjects/FlashApp/images/card_back.png")
front_card = PhotoImage(file="C:/Users/ungur/PycharmProjects/FlashApp/images/card_front.png")
current_image = canvas.create_image(400, 263, image=front_card)
language = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="../FlashApp/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="../FlashApp/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

next_word()

window.mainloop()

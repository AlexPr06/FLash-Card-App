
import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"

# +------------------------------         Data        ------------------------------------+

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

list_of_french_words = data['French'].to_list()

list_of_english_words = data['English'].to_list()

list_French_English = list(zip(list_of_french_words, list_of_english_words))
print(list_French_English)


current_word = []
# +----------------------------------          Functions           --------------------------------+
def word_generation():
    random_pair = random.choice(list_French_English)
    return random_pair


# +-------------------------------    Functionality functions   -----------------------------------+
def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.delete(current_word)
    current_word = word_generation()
    new_word = current_word[0]
    canvas.itemconfig(card_title, text="French", font=("Arial", 40, "italic"), fill="black")
    canvas.itemconfig(card_word, text=new_word, font=("Arial", 60, "bold"), fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer= window.after(3000, func=flip_card)


def flip_card():
    global current_word

    translated_word = current_word[1]
    canvas.itemconfig(card_title, text="English", font=("Arial", 40, "italic"), fill="white")
    canvas.itemconfig(card_word, text=translated_word, font=("Arial", 60, "bold"), fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def unknown_button_pressed():
    next_card()

def known_button_pressed():
    if current_word in list_French_English:
        list_French_English.remove(current_word)
    print(len(list_French_English))
    words_to_learn = pandas.DataFrame(list_French_English, columns=["French", "English"])
    words_to_learn.to_csv('data/words_to_learn.csv', index=False)

    next_card()

# +-------------------------------      GUI           -----------------------------------------------+

#main window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#creating canvas and use it in window object
canvas = Canvas(window, width = 800,height = 526)

#extracting image card_front.png
card_front_image = PhotoImage(file="..\Flash Card App\images\card_front.png")

#extracting image card_back.png
card_back_image = PhotoImage(file="..\Flash Card App\images\card_back.png")

#using image card_back.png in canvas. x=800/2 = 400, y=256 /2 = 263  ->
# (400, 256) - center of the canvas and exactly there with push it
card_background =canvas.create_image(400, 263, image=card_front_image)

# Title
card_title = canvas.create_text(400, 150, text= "", font=("Arial", 40, "italic"))

# Word
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))


#some configurations with canvas object
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

#setting canvas object positions using method grid
canvas.grid(row = 0, column = 0, columnspan = 2)


wrong_image = PhotoImage(file="..\Flash Card App\images\wrong.png")

unknown_button = Button(window, command=unknown_button_pressed, image=wrong_image, highlightthickness=0)
unknown_button.grid(row = 1, column = 0)

right_image = PhotoImage(file="..\Flash Card App\images\\right.png")
known_button = Button(window, command=known_button_pressed, image=right_image, highlightthickness=0)
known_button.grid(row = 1, column = 1)

next_card()


window.mainloop()
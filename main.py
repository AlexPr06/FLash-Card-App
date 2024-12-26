import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"

# +------------------------------         Data        ------------------------------------+

data = pandas.read_csv("data/french_words.csv")

list_of_french_words = data['French'].to_list()

list_of_english_words = data['English'].to_list()

list_French_English = list(zip(list_of_french_words, list_of_english_words))

print(list_French_English)


# +----------------------------------          Functions           --------------------------------+
def word_generation():
    random_pair = random.choice(list_French_English)
    return random_pair




def unknown_button_pressed():
    global text_id
    # Видалення попереднього тексту

    canvas.delete(text_id)

    # Вибір випадкового слова зі списку
    new_word = word_generation()[0]

    # Додавання нового тексту
    text_id = canvas.create_text(400, 263, text=new_word, font=("Arial", 60, "bold"))

def known_button_pressed():
    global text_id

    canvas.delete(text_id)

    # Вибір випадкового слова зі списку
    new_word = word_generation()[0]

    # Додавання нового тексту
    text_id = canvas.create_text(400, 263, text=new_word, font=("Arial", 60, "bold"))


# +-------------------------------      GUI           -----------------------------------------------+

#main window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#creating canvas and use it in window object
canvas = Canvas(window, width = 800,height = 526)

#extracting image card_back.png
card_front_image = PhotoImage(file="..\Flash Card App\images\card_front.png")

#using image card_back.png in canvas. x=800/2 = 400, y=256 /2 = 263  ->
# (400, 256) - center of the canvas and exactly there with push it
canvas.create_image(400, 263, image=card_front_image)

# Title
canvas.create_text(400, 150, text= "Title", font=("Arial", 40, "italic"))

# Word
text_id = canvas.create_text(400, 263, text= word_generation()[0], font=("Arial", 60, "bold"))


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




window.mainloop()
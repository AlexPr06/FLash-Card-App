import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

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
canvas.create_text(400, 263, text="Text", font=("Arial", 60, "bold"))

#some configurations with canvas object
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

#setting canvas object positions using method grid
canvas.grid(row = 0, column = 0, columnspan = 2)


wrong_image = PhotoImage(file="..\Flash Card App\images\wrong.png")

unknown_button = Button(window, command=lambda: print("Unknown Button pressed"), image=wrong_image)
unknown_button.grid(row = 1, column = 0)

right_image = PhotoImage(file="..\Flash Card App\images\\right.png")
known_button = Button(window, command=lambda: print("Known Button pressed"), image=right_image)
known_button.grid(row = 1, column = 1)

window.mainloop()
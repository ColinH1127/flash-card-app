from tkinter import *
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
import random

BACKGROUND_COLOR = "#B1DDC6"
word_df = pd.read_csv("./data/french_words.csv")
word_dict = word_df.to_dict(orient="records")
current_card = {}

def generate_fr_word():
    global current_card
    current_card = random.choice(word_dict)
    random_fr_word = current_card["French"]
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=random_fr_word, fill="black")
    window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_img, image=new_image)
    canvas.itemconfig(title, text="English", fill="white")
    random_en_word = current_card["English"]
    canvas.itemconfig(word, text=random_en_word, fill="white")



window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas_img = canvas.create_image(400, 260, image=card_front_img)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 300, text="", font=("Arial", 60, "bold"))
my_image1 = PhotoImage(file="./images/right.png")
check_button = Button(image=my_image1, highlightthickness=0, command=generate_fr_word)
check_button.grid(row=1, column=1)
my_image2 = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=my_image2, highlightthickness=0, command=generate_fr_word)
wrong_button.grid(row=1, column=0)
new_image = PhotoImage(file="./images/card_back.png")
generate_fr_word()




window.mainloop()

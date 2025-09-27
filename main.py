from tkinter import *
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
import random

BACKGROUND_COLOR = "#B1DDC6"

def generate_fr_word():
    word_df = pd.read_csv("./data/french_words.csv")
    word_dict = word_df.to_dict(orient="records")
    random_index = random.choice(range(0, len(word_dict)))
    random_fr_word = word_dict[random_index]["French"]
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=random_fr_word)


window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 260, image=card_front_img)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 300, text="", font=("Arial", 60, "bold"))
my_image1 = PhotoImage(file="./images/right.png")
check_button = Button(image=my_image1, highlightthickness=0, command=generate_fr_word)
check_button.grid(row=1, column=1)
my_image2 = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=my_image2, highlightthickness=0, command=generate_fr_word)
wrong_button.grid(row=1, column=0)

generate_fr_word()




window.mainloop()

import os


from tkinter import *


def about():
    ab = Tk()

    ab.title("About")
    ab.geometry("500x200")
    ab.resizable(width=False, height=False)
    ab.iconbitmap(os.path.join(os.path.expanduser('~'),'Documents','com.soujatya_sarkar.gap','icon.ico'))

    Label(ab, text="Glaze Additive Predictor", font=("Heveltica Neue", 20, 'bold')).pack(pady=15)
    Label(ab, text="Copyright © 2022, Soujatya Sarkar, All Rights Reserved.", font=("Heveltica Neue", 12, 'bold')).pack()
    Label(ab, text="Computational Development and Research - Soujatya Sarkar").pack()
    Label(ab, text="Chemical Data Collection - Tapabrata Mondal and Soujatya Sarkar").pack()
    Label(ab, text="Author and Inventor - Soujatya Sarkar").pack()
    Label(ab, text="Version - 1.0.0", font=("Heveltica Neue", 12, 'bold')).pack()

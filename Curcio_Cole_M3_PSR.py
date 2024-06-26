import tkinter as tk
from tkinter import *
import random

window = Tk()
window.geometry("350x230")

l = Label(window, text='The Calculation of the Steak Joint')
l.pack()

total_price = Label(text='The total price is: $')

# Display the list of five dinners and prices.
tables = ['Dinner 1 ', 'Dinner 2 ', 'Dinner 3 ', 'Dinner 4 ', 'Dinner 5 ']
price = [35.52, 27.13, 41.71, 39.95, 48.20]

# Allow the user to select the dinners and quantities.
dinner = ['Dinner 1 ', 'Dinner 2 ', 'Dinner 3 ', 'Dinner 4 ', 'Dinner 5 ']
print(random.choice(dinner))
price = [35.52, 27.13, 41.71, 39.95, 48.20]
print(random.choice(price))

def buttonFunction():
    print(random.choice(price))

b1 = Button(window, text='Select the bill', command=buttonFunction)
b1.pack(side=TOP)

b2 = Button(window, text='Cancel the order', command=exit)
b2.pack(side=LEFT)
def stop():
    window.destroy()

b3 = Button(window, text='Close', command=exit)
b3.pack(side=BOTTOM)
def exit():
    window.destroy()

window.mainloop()
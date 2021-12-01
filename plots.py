from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Graphs')
root.iconbitmap('./icon.ico')
root.geometry('400x200')

def graph():
 housePrices = np.random.normal(200000, 25000, 5000)
 plt.hist(housePrices, 50)
 plt.show()


button = Button(root, text='Graph', command=graph)
button.pack()
root.mainloop()
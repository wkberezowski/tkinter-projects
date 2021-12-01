from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Learn to code')
root.iconbitmap('./icon.ico')

def open():
 global myImg
 root.filename = filedialog.askopenfilename(initialdir='./images', title='Select a file', filetypes=(('jpg files', '*.jpg'), ('all files', '*.*')))
 myLabel = Label(root, text=root.filename).pack()
 myImg = ImageTk.PhotoImage(Image.open(root.filename))
 myImgLabel = Label(image=myImg).pack()

btn = Button(root, text='Open file', command=open).pack()

root.mainloop()
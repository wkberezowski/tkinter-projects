from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code')
root.iconbitmap('./icon.ico')

myImg = ImageTk.PhotoImage(Image.open('images/aspen.jpg'))
myImg2 = ImageTk.PhotoImage(Image.open('images/aspen2.jpg'))
myImg3 = ImageTk.PhotoImage(Image.open('images/aspen3.jpg'))

imageList = [myImg, myImg2, myImg3]

status = Label(root, text='Image 1 of {}'.format(len(imageList)), border=1, relief=SUNKEN, anchor=E)

myLabel = Label(image=myImg)
myLabel.grid(row=0, column=0, columnspan=3)

def forward(imageNumber):
 global myLabel
 global buttonNext
 global buttonBack
 
 myLabel.grid_forget()
 myLabel = Label(image=imageList[imageNumber - 1])
 
 buttonNext = Button(root, text='>>', command=lambda: forward(imageNumber + 1))
 buttonBack = Button(root, text='<<', command=lambda: back(imageNumber - 1))
 
 if imageNumber == 3:
  buttonNext = Button(root, text='>>', state=DISABLED)
 
 myLabel.grid(row=0, column=0, columnspan=3)
 buttonBack.grid(row=1, column=0)
 buttonNext.grid(row=1, column=2)
 
 status = Label(root, text='Image {} of {}'.format(imageNumber, len(imageList)), border=1, relief=SUNKEN, anchor=E)
 status.grid(row=2, column=0, columnspan=3, sticky=W + E)
 
 

def back(imageNumber):
 global myLabel
 global buttonNext
 global buttonBack
  
 myLabel.grid_forget()
 myLabel = Label(image=imageList[imageNumber - 1])
 
 buttonNext = Button(root, text='>>', command=lambda: forward(imageNumber + 1))
 buttonBack = Button(root, text='<<', command=lambda: back(imageNumber - 1))
 
 if imageNumber == 1:
  buttonBack = Button(root, text='<<', state=DISABLED)
 
 myLabel.grid(row=0, column=0, columnspan=3)
 buttonBack.grid(row=1, column=0)
 buttonNext.grid(row=1, column=2)
 
 status = Label(root, text='Image {} of {}'.format(imageNumber, len(imageList)), border=1, relief=SUNKEN, anchor=E)
 status.grid(row=2, column=0, columnspan=3, sticky=W + E)


buttonBack = Button(root, text='<<', command=back, state=DISABLED)
buttonExit = Button(root, text='EXIT PROGRAM', command=root.quit)
buttonNext = Button(root, text='>>', command=lambda: forward(2))

buttonBack.grid(row=1, column=0)
buttonExit.grid(row=1, column=1)
buttonNext.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()
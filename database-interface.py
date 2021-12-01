from sqlite3.dbapi2 import connect
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Learn to code')
root.iconbitmap('./icon.ico')
root.geometry('400x400')

# create or connect to a database
conn = sqlite3.connect('address-book.db')

# create cursor 
cursor = conn.cursor()

# create table
# cursor.execute("""
#                CREATE TABLE addresses (
#                 firstName text,
#                 lastName text,
#                 adress text,
#                 city text,
#                 state text,
#                 zipcode integer
#                )""")

# create edit function to update a record
def update():
 # create or connect to a database
 conn = sqlite3.connect('address-book.db')
 # create cursor 
 cursor = conn.cursor()
 
 recordId = deleteBox.get()
 
 cursor.execute("""
           UPDATE addresses SET
           firstName = :first,
           lastName = :last,
           address = :address,
           city = :city,
           state = :state,
           zipcode = :zipcode
           
           WHERE oid = :oid""",
           {'first': firstNameEditor.get(),
            'last': lastNameEditor.get(),
            'address': addressEditor.get(),
            'city': cityEditor.get(),
            'state':stateEditor.get(),
            'zipcode': zipcodeEditor.get(),
            
            'oid': recordId
            })
 # commit changes
 conn.commit()
 # close connection
 conn.close()
 
 editor.destroy()

# create edit function to update a record
def edit():
 global editor
 editor = Tk()
 editor.title('Learn to code')
 editor.iconbitmap('./icon.ico')
 editor.geometry('400x400')
 
 # create or connect to a database
 conn = sqlite3.connect('address-book.db')
 # create cursor 
 cursor = conn.cursor()
 
 recordId = deleteBox.get()
 
 # query the database
 cursor.execute("SELECT * FROM addresses WHERE oid=" + recordId)
 records = cursor.fetchall()
 
 # commit changes
 conn.commit()
 # close connection
 conn.close()
 
 # create global variables
 global firstNameEditor
 global lastNameEditor
 global addressEditor
 global cityEditor
 global stateEditor
 global zipcodeEditor
 
  # create text boxes
 firstNameEditor = Entry(editor, width=30)
 firstNameEditor.grid(row=0, column=1, padx=20, pady=(10, 0))

 lastNameEditor = Entry(editor, width=30)
 lastNameEditor.grid(row=1, column=1, padx=20)

 addressEditor = Entry(editor, width=30)
 addressEditor.grid(row=2, column=1, padx=20)

 cityEditor = Entry(editor, width=30)
 cityEditor.grid(row=3, column=1, padx=20)

 stateEditor = Entry(editor, width=30)
 stateEditor.grid(row=4, column=1, padx=20)

 zipcodeEditor = Entry(editor, width=30)
 zipcodeEditor.grid(row=5, column=1, padx=20)

 # text box labels
 firstNameLabel = Label(editor, text='First name')
 firstNameLabel.grid(row=0, column=0, pady=(10, 0))

 lastNameLabel = Label(editor, text='Last name')
 lastNameLabel.grid(row=1, column=0)

 addressLabel = Label(editor, text='Address')
 addressLabel.grid(row=2, column=0)

 cityLabel = Label(editor, text='City')
 cityLabel.grid(row=3, column=0)

 stateLabel = Label(editor, text='State')
 stateLabel.grid(row=4, column=0)

 zipcodeLabel = Label(editor, text='Zipcode')
 zipcodeLabel.grid(row=5, column=0)
 
 # loop through results
 for record in records:
  firstNameEditor.insert(0, record[0])
  lastNameEditor.insert(0, record[1])
  addressEditor.insert(0, record[2])
  cityEditor.insert(0, record[3])
  stateEditor.insert(0, record[4])
  zipcodeEditor.insert(0, record[5])
 
 # create a save button
 editBtn = Button(editor, text='Save record', command=update)
 editBtn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

# create function to delete from database
def delete():
 # create or connect to a database
 conn = sqlite3.connect('address-book.db')

 # create cursor 
 cursor = conn.cursor()
 
 cursor.execute('DELETE from addresses WHERE oid=' + deleteBox.get())
 # commit changes
 conn.commit()

 # close connection
 conn.close()

# create submit function 
def submit ():
 # create or connect to a database
 conn = sqlite3.connect('address-book.db')

 # create cursor 
 cursor = conn.cursor()
 
 # inser into tabel
 cursor.execute("INSERT INTO addresses VALUES (:firstName, :lastName, :address, :city, :state, :zipcode)", 
           {
            'firstName': firstName.get(),
            'lastName': lastName.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
           })
 # commit changes
 conn.commit()

 # close connection
 conn.close()
 
 
 # clear text boxes
 firstName.delete(0, END)
 lastName.delete(0, END)
 address.delete(0, END)
 city.delete(0, END)
 state.delete(0, END)
 zipcode.delete(0, END)
 
 
# create query function
def query():
 # create or connect to a database
 conn = sqlite3.connect('address-book.db')
 # create cursor 
 cursor = conn.cursor()
 
 # query the database
 cursor.execute("SELECT *, oid FROM addresses")
 records = cursor.fetchall()
 
 # loop through result
 printRecords = ''
 for record in records:
  printRecords += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'
 
 queryLabel = Label(root, text=printRecords)
 queryLabel.grid(row=12, column=0, columnspan=2)
 
 # commit changes
 conn.commit()
 # close connection
 conn.close()

# create text boxes
firstName = Entry(root, width=30)
firstName.grid(row=0, column=1, padx=20, pady=(10, 0))

lastName = Entry(root, width=30)
lastName.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

deleteBox = Entry(root, width=30)
deleteBox.grid(row=9, column=1, pady=5)

# text box labels
firstNameLabel = Label(root, text='First name')
firstNameLabel.grid(row=0, column=0, pady=(10, 0))

lastNameLabel = Label(root, text='Last name')
lastNameLabel.grid(row=1, column=0)

addressLabel = Label(root, text='Address')
addressLabel.grid(row=2, column=0)

cityLabel = Label(root, text='City')
cityLabel.grid(row=3, column=0)

stateLabel = Label(root, text='State')
stateLabel.grid(row=4, column=0)

zipcodeLabel = Label(root, text='Zipcode')
zipcodeLabel.grid(row=5, column=0)

deleteBoxLabel = Label(root, text='Select ID')
deleteBoxLabel.grid(row=9, column=0, pady=5)


# create submit button
submitBtn = Button(root, text='Add record to Database', command=submit)
submitBtn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=111)

# create a query button
queryBtn = Button(root, text='Show records', command=query)
queryBtn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create a delete button
deleteBtn = Button(root, text='Delete record', command=delete)
deleteBtn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create and update button
editBtn = Button(root, text='Edit record', command=edit)
editBtn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=144)

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()
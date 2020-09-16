import sqlite3
from tkinter import *
from tkinter import messagebox,ttk
from PIL import ImageTk,Image

mainwindow = Tk()
mainwindow.title('Fatafat')
mainwindow.configure(background='white')


l1=Label(mainwindow,text='Enter Customer Name',bg='white').grid(row=2,column=2)
t1=Entry(mainwindow)
t1.grid(row=2,column=5)

l2=Label(mainwindow,text='Enter Address',bg='white').grid(row=4,column=2)
t2=Entry(mainwindow)
t2.grid(row=4,column=5,columnspan=3)

l3=Label(mainwindow,text='Enter Phone No.',bg='white').grid(row=6,column=2)
t3=Entry(mainwindow)
t3.grid(row=6,column=5,columnspan=3)

l4=Label(mainwindow,text='Description of Customer',bg='white').grid(row=8,column=2)
t4=Entry(mainwindow)
t4.grid(row=8,column=5,columnspan=3)

canvas = Canvas(mainwindow, width = 100, height = 100,bg='white',highlightthickness=0)
canvas.grid(row=10,column=1, columnspan=3, rowspan=2,
               sticky=W+E+N+S, padx=5, pady=5)
img = ImageTk.PhotoImage(Image.open("Webp.net-compress-image.jpg"))
canvas.create_image(20, 20, anchor=NW, image=img)

connection=sqlite3.connect('fatafat.db')
print('database opened successfully')

TABLE_NAME='fatafat_table'
ID='Customer_Id'
NAME='Customer_Name'
ADDRESS='Customer_Address'
PHONE='Customer_Phone'
DESCRIPTION='Customer_Description'


def savetodatabase():
    name=t1.get()
    address=t2.get()
    phone=t3.get()
    description=t4.get()
    if ((name == '') | (address == '') | (phone == '') | (description == '')):
        messagebox.showerror('ERROR','Fill all the values')
    else:
        try:
            connection.execute('CREATE TABLE IF NOT EXISTS ' +
                                TABLE_NAME +'('+ ID +
                                ' INTEGER PRIMARY KEY ''AUTOINCREMENT, '+
                                 NAME +' TEXT, '+ ADDRESS +
                                ' TEXT, '+ PHONE +' INTEGER, '+
                                DESCRIPTION +' TEXT);')


            connection.execute("INSERT INTO " + TABLE_NAME + " ( " +
                               NAME + ", " + ADDRESS + ", " +
                               PHONE + ", " +
                               DESCRIPTION +
                               " ) VALUES ( '" + name + "','" + address + "'," +
                               "'" + phone + "', '" + description + "'); ")

            connection.commit()
            messagebox.showinfo('Success', 'Values committed to Database')
        except sqlite3.OperationalError:
            messagebox.showerror('ERROR','Enter proper Values')

b1=Button(mainwindow,text='Submit',bg='white',command=lambda:savetodatabase()).grid(row=10,column=5)



def showdatabase():
    secondwindow = Tk()
    secondwindow.title('Fatafat Database')
    tree = ttk.Treeview(secondwindow)
    tree['columns'] = ('one', 'two', 'three', 'four', 'five')
    tree.heading('one', text='Customer Id')
    tree.heading('two', text='Customer Name')
    tree.heading('three', text='Customer Address')
    tree.heading('four', text='Customer Phone')
    tree.heading('five', text='Customer Description')

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i=0
    for row in cursor:
        tree.insert('', i, text='Customer ' + str(row[0]),
                    values=( row[0], row[1],row[2] ,row[3] ,row[4]))
        i=i+1
    tree.pack()
    secondwindow.mainloop()

b3=Button(mainwindow,text='Show Database',bg='white',command=lambda:showdatabase()).grid(row=11,column=5)
# b3.pack()


def closeconnection():
    connection.close()
    print("Connection has been closed.")
    mainwindow.destroy()
    print("Main window destroyed.")

b3=Button(mainwindow,text='Close Connection',bg='white',command=lambda:closeconnection()).grid(row=15,column=5)
# b3.pack()
l5=Label(mainwindow,text='Close the connection before quitting the App',bg='white').grid(row=16,column=2)
# l5.pack()

mainwindow.mainloop()


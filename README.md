# Fatafat
Customer database Software

## Technology Used:

1.Python Language

2.Tkinter Library

3.sqlite3

## Sample Code

1.Saving entered values into database

```
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
```

2.Viewing the saved data

```
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

```

## Screenshots

![img](https://github.com/bitsplease98/Fatafat/blob/master/fatafat1.PNG)

![img](https://github.com/bitsplease98/Fatafat/blob/master/fatafat2.PNG)

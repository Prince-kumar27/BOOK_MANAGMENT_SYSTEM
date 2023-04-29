from tkinter import*


root = Tk()
root.geometry('500x500')
root.title("submitbook_module")

label_0 = Label(root, text="SUBMIT_BOOK",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
label_1 = Label(root, text="User_Name:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)
label_2 = Label(root, text="BOOK_NAME:",width=20,font=("bold", 10))
label_2.place(x=80,y=180)
entry_2 = Entry(root)
entry_2.place(x=240,y=180)


label_3 = Label(root, text="PRICE:",width=20,font=("bold", 10))
label_3.place(x=70,y=220)

entry_3 = Entry(root,text="IN RS")
entry_3.place(x=240,y=220)
def save_info():
    file=open("submit.txt","a+")
    file.write('\n')
    file.write(entry_1.get())
    file.write('\n')
    s1=str(entry_2.get())
    file.write(s1)
    file.write('\n')
    
    file.write(entry_3.get())
    file.write('\n')
    




    
    file.close()



Button(root, text='Submit',width=20,bg='brown',fg='white',command=save_info).place(x=200,y=280)


root.mainloop()

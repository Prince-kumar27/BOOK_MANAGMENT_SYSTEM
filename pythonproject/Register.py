from tkinter import*
from tkinter import messagebox  

root = Tk()
root.geometry('500x500')
root.title("Register_module")

label_0 = Label(root, text="REGISTER",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Name:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Address:",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender:",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Mobile_no:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)
entry_4 = Entry(root)
entry_4.place(x=240,y=290)

label_5 = Label(root, text="Email_Id",width=20,font=("bold", 10))
label_5.place(x=70,y=320)

entry_5 = Entry(root)
entry_5.place(x=240,y=320)
def save_info():
    file=open("register.txt","a+")
    file.write('\n')
    file.write(entry_1.get())
    file.write('\n')
    
    file.write(entry_2.get())
    file.write('\n')
    s1=str(var.get())
    file.write(s1)
    file.write('\n')
    file.write(entry_4.get())
    file.write('\n')

    s2=str(entry_5.get())
    file.write(s2)
    file.write('\n')





    
    file.close()

Button(root, text='Submit',width=20,bg='brown',fg='white',command=save_info).place(x=200,y=380)


root.mainloop()

from tkinter import*


root = Tk()
root.geometry('500x500')
root.title("loginpage_module")

label_0 = Label(root, text="LOGIN_PAGE",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="User_Name:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)
label_2 = Label(root, text="Password:",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)
def save_info():
    file=open("login.txt","a+")
    file.write('\n')
    file.write(entry_1.get())
    file.write('\n')
    
    
   
    s1=str(entry_2.get())
    file.write(s1)
    file.write('\n')




    
    file.close()


Button(root, text='LOGIN NOW',width=20,bg='brown',fg='white',command=save_info).place(x=170,y=210)
Button(root, text='NEW USER',width=20,bg='brown',fg='white').place(x=170,y=240)
root.mainloop()

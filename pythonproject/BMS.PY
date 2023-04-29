
from tkinter import*
from tkinter import messagebox  


root = Tk()

root.geometry('650x550')
root.title("BMS_module")


label_0 = Label(root, text="📚BMS📚",width=30,font=("bold", 20))
label_0.place(x=100,y=63)
def login():
 root = Tk()
 root.geometry('500x500')
 root.title("loginpage_module")

 label_0 = Label(root, text="LOGIN_PAGE",width=20,font=("bold", 20))
 label_0.place(x=90,y=53)

 label_1 = Label(root, text="User_Name:",width=20,font=("bold", 10))
 label_1.place(x=80,y=130)

 entry_11 = Entry(root)
 entry_11.place(x=240,y=130)
 label_2 = Label(root, text="Password:",width=20,font=("bold", 10))
 label_2.place(x=80,y=180)

 entry_22 = Entry(root)
 entry_22.place(x=240,y=180)
 def save_info():
     if(entry_11.get()!="Prince" or entry_22.get()!="12345"):
        
        messagebox.askretrycancel("ALERT⭕‼", "user-not-found?")
         

     if(entry_11.get()=="Prince" and entry_22.get()=="12345"):
       print("scussess-full-login")
       root = Tk()
       root.geometry('500x500')
       root.title("request_module")
       label_0 = Label(root, text="REQUEST BOOK",width=20,font=("bold", 20))
       label_0.place(x=90,y=53)
       label_1 = Label(root, text="USER_NAME:",width=20,font=("bold", 10))
       label_1.place(x=80,y=130)
       entry_1 = Entry(root)
       entry_1.place(x=240,y=130)
     
     def myclick():
         root = Tk()
         root.geometry('600x600')
         root.title("availablebook")

         label_0 = Label(root, text="AVAILABLE_BOOK",width=20,font=("bold", 20))
         label_0.place(x=320,y=230)
   
         lb1=Listbox(root,width=300,height=100)
         lb1.insert(1,"1.Computer Fundamentals and Programming in C.  price:$120")
         lb1.insert(2,"2.The Network Designer’s Handbook: 51 CSE (Concurrent Systems Engineering Series). price:$130")
         lb1.insert(3,"3.Applied Physics – P.K.Palanisamy (SciTech Publications (India) Pvt. Ltd., Fifth Print 2008).  price:$110")
         lb1.insert(4,"4.Data Structures using C, A.M.Tanenbaum, Y.Langsam, and M.J. Augenstein, Pearson Education / PHI. price:$130")
         lb1.insert(5,"5.Engineering Drawing, Basant Agrawal, TMH.")
         lb1.insert(6,"6.Textbook of Engineering Chemistry by S.S. Dara & Mukkati S. Chand & Co,New Delhi(2006). price:$100")
         lb1.insert(7,"7.Python Crash Course: A Hands-On, Project-Based Introduction to Programming (2nd Edition) Author: Eric Matthes. price:$130")
         lb1.insert(8,"8.Learn Python the Hard Way: 3rd Edition. price:$130")
         lb1.insert(9,"9.Python Programming: An Introduction to Computer Science (3rd Edition). price:$130")
         lb1.insert(10,"10.Head First JavaScript Programming. price:$110")
         lb1.insert(11,"11.Eloquent JavaScript, 3rd Edition. price:$100")
   
         def myclick3():
          for i in lb1.curselection():
           print(lb1.get(i))

         
         Button(root, text='display',width=6,height=2,bg='brown',fg='white',command=myclick3).place(x=160,y=200)


    
         lb1.pack()

         root.mainloop()
     label_2 = Label(root, text="Available_books:",width=20,font=("bold", 10))
     label_2.place(x=68,y=180)
     entry_2 = Entry(root)
     entry_2.place(x=235,y=170)
     Button(root, text='available_books:',width=15,bg='brown',fg='white',command=myclick).place(x=240,y=200)
     label_3 = Label(root, text="PRICE:",width=20,font=("bold", 10))
     label_3.place(x=70,y=230)
     entry_3 = Entry(root)
     entry_3.place(x=235,y=230)
     def save_info():
      file=open("request.txt","a+")
      file.write('\n')
      file.write(entry_1.get())
      file.write('\n')
    
      file.write(entry_2.get())
      file.write('\n')
      s1=str(entry_3.get())
      file.write(s1)
      file.write('\n')




    
      file.close()
      
     Button(root, text='Submit',width=20,bg='brown',fg='white',command=save_info).place(x=200,y=280)


     root.mainloop()


 

 Button(root, text='LOGIN NOW',width=20,bg='brown',fg='white',command=save_info).place(x=170,y=210)
 Button(root, text='NEW USER',width=20,bg='brown',fg='white',command=register).place(x=170,y=240)
 root.mainloop()

   
 
 



def register():
   
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




def myclick():
    root = Tk()
    root.geometry('600x600')
    root.title("availablebook")

    label_0 = Label(root, text="AVAILABLE_BOOK",width=20,font=("bold", 20))
    label_0.place(x=320,y=230)
   
    lb1=Listbox(root,width=300,height=100)
    lb1.insert(1,"1.Computer Fundamentals and Programming in C.  price:$120")
    lb1.insert(2,"2.The Network Designer’s Handbook: 51 CSE (Concurrent Systems Engineering Series). price:$130")
    lb1.insert(3,"3.Applied Physics – P.K.Palanisamy (SciTech Publications (India) Pvt. Ltd., Fifth Print 2008).  price:$110")
    lb1.insert(4,"4.Data Structures using C, A.M.Tanenbaum, Y.Langsam, and M.J. Augenstein, Pearson Education / PHI. price:$130")
    lb1.insert(5,"5.Engineering Drawing, Basant Agrawal, TMH.")
    lb1.insert(6,"6.Textbook of Engineering Chemistry by S.S. Dara & Mukkati S. Chand & Co,New Delhi(2006). price:$100")
    lb1.insert(7,"7.Python Crash Course: A Hands-On, Project-Based Introduction to Programming (2nd Edition) Author: Eric Matthes. price:$130")
    lb1.insert(8,"8.Learn Python the Hard Way: 3rd Edition. price:$130")
    lb1.insert(9,"9.Python Programming: An Introduction to Computer Science (3rd Edition). price:$130")
    lb1.insert(10,"10.Head First JavaScript Programming. price:$110")
    lb1.insert(11,"11.Eloquent JavaScript, 3rd Edition. price:$100")
   
    def myclick3():
        for i in lb1.curselection():
         label=Label(root,text=(lb1.get(i)),width=60).place(x=60,y=280)
           
         label.pack()

         
    Button(root, text='display',width=6,height=2,bg='brown',fg='white',command=myclick3).place(x=160,y=200)


    
    lb1.pack()

    root.mainloop()
def myclick3():
  


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



Button(root, text='LOGIN',width=20,height=5,bg='brown',fg='white',command=login).place(x=10,y=100)
Button(root, text='NEW_USER',width=20,height=5,bg='brown',fg='white',command=register).place(x=160,y=100)
Button(root, text='Available_books',width=20,height=5,bg='brown',fg='white',command=myclick).place(x=310,y=100)
Button(root, text='submit_book',width=20,height=5,bg='brown',fg='white',command=myclick3).place(x=460,y=100)


root.mainloop()

from tkinter import*
from tkinter import messagebox


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
Button(root, text='NEW USER',width=20,bg='brown',fg='white').place(x=170,y=240)
root.mainloop()

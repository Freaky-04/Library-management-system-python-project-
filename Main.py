#create database db;
#create table books (bid varchar (20)) primary key, title varchar (30), author varchar(30), status varchar (30));
#create table books_issued(bid varchar(20) primary key, issuedto varchar (30));
from ReturnBook import returnBooks
from tkinter import *
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from PIL import ImageTk
import PIL.Image


mypass = "Pass@123" 
mydatabase="db" 

con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor() 
root = Tk ()
root .title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

# root.mainloop() start

n=0.25

filimg="D:\work\Coding\PY Libraray/bgm.jpg"
bg=PIL.Image.open(filimg)
[imgWidth, imgHeight]=bg.size

newimgWidth=int(imgWidth*n)
# if True:
newimgHeight=int(imgHeight*n)

bg=bg.resize((newimgWidth,newimgHeight),PIL.Image.ANTIALIAS)
img=ImageTk.PhotoImage(bg)
Canva=Canvas(root)
Canva.create_image(300,340,image= img)
Canva.config(bg="white",width=newimgWidth,height=newimgHeight)
Canva.pack(expand=True,fill=BOTH)
    
hframe=Frame(root,bg="#93C645",bd=5)
hframe.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
hlable=Label(hframe, text="Welcome to \n Data Of LIbraray",bg='black',fg='white',font=('Robot',16))
hlable.place(relx=0,rely=0, relwidth=1, relheight=1)



btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBooks)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)



messagebox.showinfo("First do this","\tCopy And Paste This To MySql \n\ncreate database db;\n\ncreate table books (bid varchar (20)) primary key, title varchar (30), author varchar(30), status varchar (30));\n\ncreate table books_issued(bid varchar(20) primary key, issuedto varchar (30)); ")


root.mainloop()
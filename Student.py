from tkinter import *
import mysql.connector
from tkinter import messagebox
from main import *

db=mysql.connector.connect(user='root', password='Rohit@17', host='localhost', database='db_proj1')
c=db.cursor()

class Student:
    def __init__(self):
        self.root=Tk()
        self.root.title('Student')
        self.root.geometry('300x150')

        self.l1=Label(self.root,text='Operation ')
        self.l1.grid(row=0,column=0)
        self.clicked=StringVar()
        self.clicked.set('Choose')
        self.options=["Insert","Delete","Update","Show"]
        self.drop=OptionMenu(self.root,self.clicked,*self.options)
        self.drop.grid(row=0,column=1)
        self.b1=Button(self.root,text="Submit",width=20,command=self.next1)
        self.b1.grid(row=1,column=0,columnspan=2)

    def next1(self):
        if self.clicked.get()=="Insert":
            self.com_insert()
        if self.clicked.get()=="Delete":
            self.com_delete()
        if self.clicked.get()=="Update":
            self.com1_update()
        if self.clicked.get()=="Show":
            self.com_show()
        self.root.destroy()
        
    def com_insert(self):
        self.root1=Tk()
        self.root1.title('Student Insertion')
        self.root1.geometry('300x200')
                    
        self.l1=Label(self.root1,text="Student Id")
        self.l1.grid(row=0,column=0)
        v1=StringVar(self.root1,value="None")
        self.e1=Entry(self.root1,textvariable=v1,borderwidth=5)
        self.e1.grid(row=0,column=1)
                    
        self.l2=Label(self.root1,text="Student Name ")
        self.l2.grid(row=1,column=0)
        v2=StringVar(self.root1,value="None")
        self.e2=Entry(self.root1,textvariable=v2,borderwidth=5)
        self.e2.grid(row=1,column=1)
                    
        self.l3=Label(self.root1,text="Student age")
        self.l3.grid(row=2,column=0)
        v3=StringVar(self.root1,value="None")
        self.e3=Entry(self.root1,textvariable=v3,borderwidth=5)
        self.e3.grid(row=2,column=1)

        self.l4=Label(self.root1,text='College RegId ')
        self.l4.grid(row=3,column=0)
        self.v6=StringVar(self.root1,value="None")
        self.list1=[]
        c.execute(f"select * from College")
        for i in c.fetchall():
            self.list1.append(i[0])
        self.drop=OptionMenu(self.root1,self.v6,*self.list1)
        self.drop.grid(row=3,column=1)
        
        self.l5=Label(self.root1,text='Interviewer Id ')
        self.l5.grid(row=4,column=0)
        self.v9=StringVar(self.root1,value="None")
        self.list8=[]
        c.execute(f"select * from Interviewer")
        for i in c.fetchall():
            self.list8.append(i[0])
        self.drop3=OptionMenu(self.root1,self.v9,*self.list8)
        self.drop3.grid(row=4,column=1)
        
        self.b1=Button(self.root1,text="Submit",width=20,command=self.f_insert)
        self.b1.grid(row=5,column=0,columnspan=2)
        
    def f_insert(self):
        if "None" in [self.e1.get(),self.e2.get(),self.e3.get(),self.v6.get()]:
            messagebox.showerror("Error","All important fields not filled")
        else:
            try:
                c.execute(f'insert into Student values("{int(self.e1.get())}","{self.e2.get()}","{int(self.e3.get())}","{int(self.v9.get())}","{int(self.v6.get())}");')
                db.commit()
                self.root1.destroy()
                messagebox.showinfo("Inserted","Data inserted succesfully")
            except mysql.connector.errors.IntegrityError:
                  db.rollback()
                  self.root1.destroy()
                  messagebox.showerror("Error","Data already exist in relation")
            except:
                  db.rollback()
                  self.root1.destroy()
                  messagebox.showerror("Error","The required data could not be inserted")  
            
        
    def com_delete(self):
        self.root2=Tk()
        self.root2.title('Student Deletion')
        self.root2.geometry('300x150')
        
        self.l1=Label(self.root2,text="Student Id")
        self.l1.grid(row=0,column=0)
        self.v4=StringVar(self.root2,value="None")
        self.list1=[]
        c.execute(f"select * from Student")
        
        for i in c.fetchall():
            self.list1.append(i[0])
        if len(self.list1)==0:
              messagebox.showerror("Error","Database is empty")
              self.root2.destroy()
        else:
            self.drop=OptionMenu(self.root2,self.v4,*self.list1)
            self.drop.grid(row=0,column=1)
            self.b1=Button(self.root2,text="Submit",width=20,command=self.f_delete)
            self.b1.grid(row=1,column=0,columnspan=2)

    def f_delete(self):
        if self.v4.get() == "None":
               messagebox.showerror("Error","Student Id not selected")
        else:
            try:
                  c.execute(f'DELETE FROM Student WHERE Sid= "{int(self.v4.get())}";')
                  db.commit()
                  self.root2.destroy()
                  messagebox.showinfo("Succesfull","Sucessfully deleted")
            except:
                  db.rollback()
                  self.root2.destroy()
                  messagebox.showerror("Error","Could not be deleted")
                  
    def com1_update(self):
        self.root3=Tk()
        self.root3.title('Student Updation')
        self.root3.geometry('300x150')

        self.l1=Label(self.root3,text="Student Id")
        self.l1.grid(row=0,column=0)
        self.v5=StringVar(self.root3,value="None")
        self.list1=[]
        c.execute(f"select * from Student")
        
        for i in c.fetchall():
            self.list1.append(i[0])
        if len(self.list1)==0:
              messagebox.showerror("Error","Database is empty")
              self.root3.destroy()
        else:
            self.drop=OptionMenu(self.root3,self.v5,*self.list1)
            self.drop.grid(row=0,column=1)
            
            self.b1=Button(self.root3,text="Submit",width=20,command=self.com2_update)
            self.b1.grid(row=1,column=0,columnspan=2)
        
    def com2_update(self):
        self.root3.destroy()
        self.root4=Tk()
        self.root4.title('Student Updation')
        self.root4.geometry('300x150')
                    
        self.l2=Label(self.root4,text="Student Name")
        self.l2.grid(row=1,column=0)
        self.e2s=Entry(self.root4,borderwidth=5)
        self.e2s.grid(row=1,column=1)
                    
        self.l3=Label(self.root4,text="Student age")
        self.l3.grid(row=2,column=0)
        self.e3s=Entry(self.root4,borderwidth=5)
        self.e3s.grid(row=2,column=1)

        self.l4=Label(self.root4,text='College RegId ')
        self.l4.grid(row=3,column=0)
        self.v7=StringVar(self.root4,value="None")
        self.list1=[]
        c.execute(f'select * from Interviewer')
        for i in c.fetchall():
            self.list1.append(i[0])
        self.drop2=OptionMenu(self.root4,self.v7,*self.list1)
        self.drop2.grid(row=3,column=1)

        self.l5=Label(self.root4,text='Interviewer Id ')
        self.l5.grid(row=4,column=0)
        self.v10=StringVar(self.root4,value="None")
        self.list4=[]
        c.execute(f'select * from College')
        for i in c.fetchall():
            self.list4.append(i[0])
        self.drop5=OptionMenu(self.root4,self.v10,*self.list4)
        self.drop5.grid(row=4,column=1)

        c.execute(f"SELECT * FROM Student WHERE Sid = {int(self.v5.get())}")
        records=c.fetchall()
        self.b1=Button(self.root4,text="Save Changes",width=20,command=self.f_update)
        self.b1.grid(row=5,column=0,columnspan=2)
    
        for i in records:
            self.e2s.insert(0,i[1])
            self.e3s.insert(0,i[2])
            self.v7.set(i[3])
            self.v10.set(i[4])
        
    def f_update(self):
         c.execute(f'UPDATE Student SET Sname = "{self.e2s.get()}",Sage = "{int(self.e3s.get())}" WHERE Sid= "{int(self.v5.get())}";' )
         db.commit()
         self.root4.destroy()
         messagebox.showinfo("Succesfull","Sucessfully Updated")

    def com_show(self):
        self.root5=Tk()
        self.root5.title("Student Database")
        self.root5.geometry('400x150')

        self.l8=Label(self.root5,text="StudentId  ")
        self.l8.grid(row=0,column=0)
        self.l9=Label(self.root5,text="SName  ")
        self.l9.grid(row=0,column=1)
        self.l10=Label(self.root5,text="Sage  ")
        self.l10.grid(row=0,column=2)
        self.l11=Label(self.root5,text="InterviewerId  ")
        self.l11.grid(row=0,column=3)
        self.l12=Label(self.root5,text="CregId  ")
        self.l12.grid(row=0,column=4)
    
        c.execute(f'select * from Student')
        j=1
        for i in c.fetchall():
            self.l6=Label(self.root5,text=f'{i[0]}')
            self.l6.grid(row=j,column=0)
            j=j+1
        c.execute(f'select * from Student')
        j=1
        for i in c.fetchall():
            self.l11=Label(self.root5,text=f'{i[1]}')
            self.l11.grid(row=j,column=1)
            j=j+1
        c.execute(f'select * from Student')
        j=1
        for i in c.fetchall():
            self.l12=Label(self.root5,text=f'{i[2]}')
            self.l12.grid(row=j,column=2)
            j=j+1
        c.execute(f'select * from Student')
        j=1
        for i in c.fetchall():
            self.l12=Label(self.root5,text=f'{i[3]}')
            self.l12.grid(row=j,column=3)
            j=j+1
        c.execute(f'select * from Student')
        j=1
        for i in c.fetchall():
            self.l12=Label(self.root5,text=f'{i[4]}')
            self.l12.grid(row=j,column=4)
            j=j+1

        self.b5=Button(self.root5,text="Exit",width=20,command=self.dest)
        self.b5.grid(row=j,column=0,columnspan=2)   
    def dest(self):
            self.root5.destroy()

            
if __name__=="__main__":
    Student()

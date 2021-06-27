#from begin import *

from tkinter import *
import tkinter.messagebox
import sqlite3
con=sqlite3.Connection('project_database')
cur=con.cursor()
root=Tk()
root.geometry('600x700')
#root.title("PhoneBook")
#a=PhotoImage(file='C:\\Users\\palak modi\\Desktop\\PhoneBook\\pb_img.gif')
global gl
global addp
addp=0
Label(root,text='PhoneBook',font='Constantia 16',bg='cyan',fg='#ff1a1a').grid(row=0,column=1,pady=8)
#Label(root,image=a).grid(row=1,column=1)
cur.execute('create table if not exists contacts(id integer primary key Autoincrement, fname varchar2(20), lname varchar2(20), company varchar2(20), address varchar2(50), city varchar2(20), pincode integer(6), web varchar2(20), dob date)')
cur.execute('create table if not exists phone(id integer , ph_type varchar2(10), ph_no integer(10),primary key(id ,ph_no),foreign key(id) references contacts(id) ON DELETE CASCADE)')
cur.execute('create table if not exists email(id integer, e_type varchar2(10), e_id varchar2(20),primary key(id,e_id),foreign key(id) references contacts(id) ON DELETE CASCADE)')
Label(root,text='First Name',font='Constantia 12').grid(row=2,column=0,padx=18)
e1=Entry(root)
e1.grid(row=2,column=1,pady=4)
Label(root,text='Last Name',font='Constantia 12').grid(row=3,column=0,padx=18)
e2=Entry(root)
e2.grid(row=3,column=1,pady=4)
Label(root,text='Company',font='Constantia 12').grid(row=4,column=0,padx=18)
e3=Entry(root)
e3.grid(row=4,column=1,pady=4)
Label(root,text='Address',font='Constantia 12').grid(row=5,column=0,padx=18)
e4=Entry(root)
e4.grid(row=5,column=1,pady=4)
Label(root,text='City',font='Constantia 12').grid(row=6,column=0,padx=18)
e5=Entry(root)
e5.grid(row=6,column=1,pady=4)
Label(root,text='Pincode',font='Constantia 12').grid(row=7,column=0,padx=18)
e6=Entry(root)
e6.grid(row=7,column=1,pady=4)
Label(root,text='WebsiteURL',font='Constantia 12').grid(row=8,column=0,padx=18)
e7=Entry(root)
e7.grid(row=8,column=1,pady=4)
Label(root,text='BirthDate',font='Constantia 12').grid(row=9,column=0,padx=18)
e8=Entry(root)
e8.grid(row=9,column=1,pady=4)
Label(root,text='Select Phone Type',font='Constantia 12',fg='#473fd9').grid(row=10,column=0,padx=18)
v1=StringVar()
v1.set(None)
r1=Radiobutton(root,text='office',font='Constantia 12',variable=v1,value='office')
r1.grid(row=10,column=1)
r2=Radiobutton(root,text='home',font='Constantia 12',variable=v1,value='home')
r2.grid(row=10,column=2,padx=4)
r3=Radiobutton(root,text='mobile',font='Constantia 12',variable=v1,value='mobile')
r3.grid(row=10,column=3)
Label(root,text='Phone Number',font='Constantia 12').grid(row=11,column=0,padx=18)
e9=Entry(root)
e9.grid(row=11,column=1,pady=3)
Label(root,text='Select Email Type',font='Constantia 12',fg='#473fd9').grid(row=31,column=0,padx=18)
v2=StringVar()
v2.set(None)
r4=Radiobutton(root,text='office',variable=v2,value='office',font='Constantia 12')
r4.grid(row=31,column=1)
r5=Radiobutton(root,text='personal',variable=v2,value='personal',font='Constantia 12')
r5.grid(row=31,column=2,padx=4)
e10=Entry(root)
e10.grid(row=32,column=1,pady=4)
Label(root,text='Email Id',font='Constantia 12').grid(row=32,column=0,padx=18)

def save():
    notsave=0
    p=e1.get()
    q=e2.get()
    if p!='' and q!='':
        if p==q:
            showinfo('oops','first name and last name cannot be same! please try again.')
            e1.delete(0,END)
            e2.delete(0,END)
            notsave=1
    elif p=='' and q=='' :
        showinfo('oops!!','you should give atleast one name')
        notsave=1
    p=e9.get()
    if p!='':
        p=str(p)
        if len(p)<10:
            if p in ('100','108'):
                print ('ok')
            else:
                showinfo('oops','invalid phone number.')
                e9.delete(0,END)
                notsave=1
    p=e10.get()
    if p!='':
        if p.count('@')!=1 or p.count('.com')!=1:
            notsave=1
            showinfo('oops!','invalid email id')
            e10.delete(0,END)    
    p=e7.get()
    if p!='':
        if p.count('.')==0:
            notsave=1
            showinfo('oops!','invalid website URL')

    p=e8.get()
    if p!='':
        mo=p[3]+p[4]
        mo=int(mo)
        if mo>12 or mo<1:
            showinfo('oops!','invalid date')
            notsave=1
        da=p[0]+p[1]
        da=int(da)
        if mo in (1,3,5,7,8,10,12):
            if da<1 or da>31:
                showinfo('oops!','invalid date')
                notsave=1
        elif mo in (2,4,6,9,11):
            if da<1 or da>30:
                showinfo('oops!','invalid date')
                notsave=1
        ye=p[6]+p[7]+p[8]+p[9]
        ye=int(ye)
        if ye>2009:
            showinfo('oops!','you are too young to maintain a phonebook')
            notsave=1

    p=e6.get()
    if p!='':
        if len(p)<6 or len(p)>6:
            showinfo('oops','invalid pincode')
            notsave=1
        p=str(p)
        if p.isdigit():
            p=p
        else:
            showinfo('oops','invalid pincode')
            notsave=1
    if notsave==0:
        global v99
        global e99
        global addp
        
        
        cur.execute('insert into contacts(fname,lname,company,address,city,pincode,web,dob) values(?,?,?,?,?,?,?,?)',(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get()))
        cur.execute('select max(id) from contacts')
        c=cur.fetchall()
        i=c[0][0]
        cur.execute('insert into phone values(?,?,?)',(i,v1.get(),e9.get()))
        cur.execute('insert into email values(?,?,?)',(i,v2.get(),e10.get()))
        if addp==1:
            global lis
            lis=lis+[[v11.get(),e99.get()]]
            for new in lis:
                #print 'list',new[0]
                #print 'list',new[1]
                #new[0]=str(new[0])
                new[1]=int(new[1])
                cur.execute('insert into phone values(?,?,?)',(i,new[0],new[1]))
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        v1.set(None)
        v2.set(None)
        #cur.execute('insert into phone values(?,?,?)',(i,v11.get(),e99.get()))
        con.commit()
        addp=0
        showinfo('saved','data saved successfully')

def addmorepno():
    global lis
    global addp
    global r99
    if addp==0:
        lis=[]
        r99=12
    if addp==1:
        r99=r99+2
    Label(root,text='Phone Number',font='Constantia 12').grid(row=r99+1,column=0,padx=18)
    e99=Entry(root)
    e99.grid(row=r99+1,column=1,pady=3)
    Label(root,text='Select Phone Type',font='Constantia 12',fg='#473fd9').grid(row=r99,column=0,padx=18)
    
    v99=StringVar()
    v99.set(None)
    r11=Radiobutton(root,text='office',font='Constantia 12',variable=v1,value='office')
    r11.grid(row=r99,column=1)
    r22=Radiobutton(root,text='home',font='Constantia 12',variable=v1,value='home')
    r22.grid(row=r99,column=2,padx=4)
    r33=Radiobutton(root,text='mobile',font='Constantia 12',variable=v1,value='mobile')
    r33.grid(row=r99,column=3)
    if addp==0:
        lis=[e99.get(),v99.get()]
    if addp==1:
        lis=lis+[e99.get(),v99.get()]
    addp=1
'''Button(root,text='search',command=search).grid(row=15,column=1)
def exit1(e=1):
    root.destroy()
con.commit()
Button(root,text='exit',command=exit1).grid(row=15,column=3)
def edit():
    search()
Button(root,text='edit',command=edit).grid(row=15,column=2)'''
#Button(root,text='save',command=save).grid(row=15,column=0,pady=10)
Button(root,text='+',command=addmorepno).grid(row=11,column=2)

root.mainloop()

from begin import*
#some variables to make my life easy.!!!
px=10
py=5
ipy=2
from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.Connection('projectPhonebook_database')
cur=con.cursor()
root=Tk()
root.geometry('600x780')
#title
root.title("PhoneBook")
a=PhotoImage(file='A:\\University\\Sem III\\Python\\Project_PhoneBook\\phone_new\\wide.gif')
#Label(root,text='PHONEBOOK',font='Constantia 18',bg='#96ece7',fg='#ff1a1a').grid(row=0,column=1,pady=5, padx=0)
Label(root,image=a).grid(row=1,column=1,pady=20)
#table creation
cur.execute('create table if not exists contacts(id integer primary key Autoincrement, fname varchar2(20), lname varchar2(20), company varchar2(20), address varchar2(50), city varchar2(20), pincode integer(6), web varchar2(20), dob date)')
cur.execute('create table if not exists phone(id integer , ph_no integer(10),primary key(id ,ph_no),foreign key(id) references contacts(id) ON DELETE CASCADE)')
cur.execute('create table if not exists email(id integer, e_id varchar2(20),primary key(id,e_id),foreign key(id) references contacts(id) ON DELETE CASCADE)')

#new function adding new contact detail
Label(root,text='First Name',font='Constantia 12').grid(row=2,column=0,padx=px,pady=py)
e1=Entry(root)
e1.grid(row=2,column=1,pady=4,ipadx=25,ipady=ipy)
Label(root,text='Last Name',font='Constantia 12').grid(row=3,column=0,padx=px,pady=py)
e2=Entry(root)
e2.grid(row=3,column=1,pady=4,ipadx=25,ipady=ipy)
Label(root,text='Company',font='Constantia 12').grid(row=4,column=0,padx=px,pady=py)
e3=Entry(root)
e3.grid(row=4,column=1,pady=4,ipadx=25,ipady=ipy)
Label(root,text='Address',font='Constantia 12').grid(row=5,column=0,padx=px,pady=py)
e4=Entry(root)
e4.grid(row=5,column=1,pady=4,ipadx=25,ipady=ipy)
Label(root,text='City',font='Constantia 12',).grid(row=6,column=0,padx=px,pady=py)
e5=Entry(root)
e5.grid(row=6,column=1,pady=4,ipadx=25,ipady=ipy)
Label(root,text='Pincode',font='Constantia 12').grid(row=7,column=0,padx=px,pady=py)
e6=Entry(root)
e6.grid(row=7,column=1,pady=4,ipadx=25,ipady=ipy)
Label(root,text='WebsiteURL',font='Constantia 12').grid(row=8,column=0,padx=px,pady=py)
e7=Entry(root)
e7.grid(row=8,column=1,pady=4,ipadx=25,ipady=ipy)
Label(root,text='BirthDate',font='Constantia 12').grid(row=9,column=0,padx=px,pady=py)
Label(root,text='(dd-mm-yyyy)',font='Constantia 10').grid(row=9,column=2,padx=px,pady=py)
e8=Entry(root)
e8.grid(row=9,column=1,pady=4,ipadx=25,ipady=ipy)
e9=Entry(root)
e9.grid(row=11,column=1,pady=py,ipadx=25,ipady=ipy)
e10=Entry(root)
e10.grid(row=13,column=1,pady=py,ipadx=25,ipady=ipy)
Label(root,text='Phone Number',font='Constantia 12').grid(row=11,column=0,padx=px,pady=py)
#Button(root, text='+ add another number',bg="#96ece7",command='addnumber').grid(row=11,column=2,pady=py) 
Label(root,text='Email Id',font='Constantia 12').grid(row=13,column=0,padx=px,pady=py)

def addnumber(e=1):
    print("palak")
    

def save(e=1):
    notsave=0
    p=e1.get()
    q=e2.get()
    if p!='' and q!='':
        if p==q:
            messagebox.showinfo('oops','first name and last name cannot be same! please try again.')
            e1.delete(0,END)
            e2.delete(0,END)
            notsave=1
    elif p=='' and q=='' :
        messagebox.showinfo('oops!!','you should give atleast one name')
        notsave=1
    p=e9.get()
    if p!='':
        p=str(p)
        if len(p)<10:
            if p in ('100','108'):
                print ('ok')
            else:
                messagebox.showinfo('oops','invalid phone number.')
                e9.delete(0,END)
                notsave=1
    p=e10.get()
    if p!='':
        if p.count('@')!=1 or p.count('.com')!=1:
            notsave=1
            messagebox.showinfo('oops!','invalid email id')
            e10.delete(0,END)    
    p=e7.get()
    if p!='':
        if p.count('.')==0:
            notsave=1
            messagebox.showinfo('oops!','invalid website URL')

    p=e8.get()
    if p!='':
        mo=p[3]+p[4]
        mo=int(mo)
        if mo>12 or mo<1:
            messagebox.showinfo('oops!','invalid date')
            notsave=1
        da=p[0]+p[1]
        da=int(da)
        if mo in (1,3,5,7,8,10,12):
            if da<1 or da>31:
                messagebox.showinfo('oops!','invalid date')
                notsave=1
        elif mo in (2,4,6,9,11):
            if da<1 or da>30:
                messagebox.showinfo('oops!','invalid date')
                notsave=1
        ye=p[6]+p[7]+p[8]+p[9]
        ye=int(ye)
        if ye>2009:
            messagebox.showinfo('oops!','you are too young to maintain a phonebook')
            notsave=1

    p=e6.get()
    if p!='':
        if len(p)<6 or len(p)>6:
            messagebox.showinfo('oops','invalid pincode')
            notsave=1
        p=str(p)
        if p.isdigit():
            p=p
        else:
            messagebox.showinfo('oops','invalid pincode')
            notsave=1
    else:
        cur.execute('insert into contacts(fname,lname,company,address,city,pincode,web,dob) values(?,?,?,?,?,?,?,?)',(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get()))
        cur.execute('select max(id) from contacts')
        c=cur.fetchall()
        i=c[0][0]
        cur.execute('insert into phone values(?,?)',(i,e9.get()))
        cur.execute('insert into email values(?,?)',(i,e10.get()))
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
        con.commit()
        messagebox.showinfo('saved','data saved successfully')
    
def exits(e=1):
    root.destroy()


#search function definition
def search(e=1):
    root1=Tk()
    root1.geometry('350x500')
    root1.title("Search")
    e11=Entry(root1)
    e11.grid(row=2,column=1,padx=18,pady=5)
    lb=Listbox(root1,width=50,height=20)
    lb.grid(row=3,column=1,padx=18,pady=5)
    Label(root1,text='enter name here:',font='Constantia 10').grid(row=1,column=1,sticky='W',padx=12,pady=10)
    Label(root1,text='Search in Phonebook',font='Constantia 16 bold',fg='#ff1a1a',bg='#10d6d6').grid(row=0,column=1,padx=50)
    def details(e=1):
        global v
        if v==1:
            return
        root3=Tk()
        root3.title("details")
        root3.geometry('400x500')
        d=lb.curselection()
        lb.delete(0,END)
        global c
        d=d[0]
        l=len(c)
        ind=l-d-1
        global i
        i=c[ind][0]
        cur.execute('select c.id,fname,lname,company,address,city,pincode,web,dob,ph_no,e_id from contacts c inner join phone p on p.id=c.id inner join email e on e.id=c.id where c.id=?',(i,))
        x=cur.fetchall()
        cur.execute('select ph_no from phone where id=?',(i,))
        allph=cur.fetchall();
        Label(root3,text='Details',font='Constantia 16 bold',fg='#ff1a1a',bg='#10d6d6').grid(row=0,column=0,pady=20)
        Label(root3,text='First Name         :  '+x[0][1],font='Constantia 12').grid(row=1,column=0,padx=50,sticky='W')
        Label(root3,text='Last Name          :  '+x[0][2],font='Constantia 12').grid(row=2,column=0,padx=50,sticky='W')        
        Label(root3,text='Company            :  '+x[0][3],font='Constantia 12').grid(row=3,column=0,padx=50,sticky='W')        
        Label(root3,text='Address               :  '+x[0][4],font='Constantia 12').grid(row=4,column=0,padx=50,sticky='W')        
        Label(root3,text='City                      :  '+x[0][5],font='Constantia 12').grid(row=5,column=0,padx=50,sticky='W')
        y=str(x[0][6])
        Label(root3,text='Pincode               :  '+y,font='Constantia 12').grid(row=6,column=0,padx=50,sticky='W')    
        Label(root3,text='Website              :  '+x[0][7],font='Constantia 12').grid(row=7,column=0,padx=50,sticky='W')
        Label(root3,text='Birth Date         :  '+x[0][8],font='Constantia 12').grid(row=8,column=0,padx=50,sticky='W')        
        #y=str(x[0][9])
        string=""
        for p in allph:
            string=string+"  "+str(p[0])
        Label(root3,text='Phone Number :    '+string,font='Constantia 12').grid(row=10,column=0,padx=50,sticky='W')             
        Label(root3,text='Email id             :  '+x[0][10],font='Constantia 12').grid(row=12,column=0,padx=50,sticky='W')
        
        
        def addnum():
            def savenum():
                    p=adn.get()
                    if(p==""):
                        messagebox.showinfo('saved','cannot be empty')
                        root5.destroy()
                        root1.lift()
                        root3.lift()
                    else:
                        p=str(p)
                        if len(p)<10 or p in ('100','108'):
                            messagebox.showinfo('oops','invalid phone number.')
                            adn.delete(0,END)
                        else:
                            cur.execute('insert into phone values(?,?)',(x[0][0],adn.get()))
                            adn.delete(0,END)
                            con.commit()
                            messagebox.showinfo('saved','number saved successfully')
                            root5.destroy()
                            root1.lift()
                            root3.lift()
            root5=Tk()
            root5.title("add number")
            root5.geometry('150x150')
            Label(root5,text='add number',font='Constantia 12',).grid(row=40,column=0,pady=18,padx=20)
            adn=Entry(root5)
            adn.grid(row=41,column=0)
            Button(root5,text='save',bg="#96ece7",command=savenum).grid(row=42,column=0,pady=10,ipadx=8)
                        

            
        def close2():
            root3.destroy()
            root1.lift()
            global v
            v=1
            
        def delete():
            global i
            cur.execute('delete from contacts where id=?',(i,))
            root3.destroy()
            messagebox.showinfo('deleted','contact deleted from the phonebook')
            con.commit()
            root1.lift()
            global v
            v=1
            
        def edit2():
            root4=Tk()
            root4.title("edit")
            root4.geometry('400x450')
            r2=0
            Label(root4,text='Edit',font='Constantia 16',bg='#96ece7',fg='#ff1a1a').grid(row=0,column=1,pady=18)
            Label(root4,text='First Name',font='Constantia 12').grid(row=1,column=r2,padx=18)
            Label(root4,text='Last Name',font='Constantia 12').grid(row=2,column=r2,padx=18)
            Label(root4,text='Company',font='Constantia 12').grid(row=3,column=r2,padx=18)
            Label(root4,text='Address',font='Constantia 12').grid(row=4,column=r2,padx=18)
            Label(root4,text='City',font='Constantia 12').grid(row=5,column=r2,padx=18)
            Label(root4,text='Pincode',font='Constantia 12').grid(row=6,column=r2,padx=18)
            Label(root4,text='Website',font='Constantia 12').grid(row=7,column=r2,padx=18)
            Label(root4,text='Birth Date',font='Constantia 12').grid(row=8,column=r2,padx=18)
            Label(root4,text='Phone Number',font='Constantia 12').grid(row=11,column=r2,padx=18)
            Label(root4,text='Email id',font='Constantia 12').grid(row=14,column=r2,padx=18)
            global i
            cur.execute('select c.id,fname,lname,company,address,city,pincode,web,dob,ph_no,e_id from contacts c inner join phone p on p.id=c.id inner join email e on e.id=c.id where c.id=?',(i,))
            x=cur.fetchall()
            x=list(x)
            a=Entry(root4)
            a.grid(row=1,column=1)
            b=Entry(root4)
            b.grid(row=2,column=1)
            c=Entry(root4)
            c.grid(row=3,column=1)
            d=Entry(root4)
            d.grid(row=4,column=1)
            e=Entry(root4)
            e.grid(row=5,column=1)
            f=Entry(root4)
            f.grid(row=6,column=1)
            g=Entry(root4)
            g.grid(row=7,column=1)
            h=Entry(root4)
            h.grid(row=8,column=1)
            k=Entry(root4)
            k.grid(row=11,column=1)
            j=Entry(root4)
            j.grid(row=14,column=1,pady=4)
            
            a.insert(0,x[0][1])
            b.insert(0,x[0][2])
            c.insert(0,x[0][3])
            d.insert(0,x[0][4])
            e.insert(0,x[0][5])
            f.insert(0,x[0][6])
            g.insert(0,x[0][7])
            h.insert(0,x[0][8])
            k.insert(0,x[0][9])  
                 
            def save2():
                global i
                cur.execute('delete from contacts where id=?',(i,))
                cur.execute('insert into contacts(fname,lname,company,address,city,pincode,web,dob) values(?,?,?,?,?,?,?,?)',(a.get(),b.get(),c.get(),d.get(),e.get(),f.get(),g.get(),h.get()))
                cur.execute('select max(id) from contacts')
                x=cur.fetchall()
                i=x[0][0]
                cur.execute('insert into phone values(?,?)',(i,k.get()))
                cur.execute('insert into email values(?,?)',(i,j.get()))
                root4.destroy()
                root3.destroy()
                messagebox.showinfo('saved','data edited successfully')
                root1.lift()
                
            Button(root4,text='save',bg="#96ece7",command=save2).grid(row=15,column=1,pady=10,ipadx=8)

        
        Button(root3,text='close', bg="#96ece7",command=close2).grid(row=16,column=0,pady=5,ipadx=8)
        Button(root3,text='delete contact',bg="#96ece7",command=delete).grid(row=15,column=0,pady=5,ipadx=8)
        Button(root3,text='edit',bg="#96ece7", command=edit2).grid(row=13,column=0,pady=5,ipadx=8)
        Button(root3,text='add another number',bg="#96ece7", command=addnum).grid(row=14,column=0,pady=5,ipadx=8)
    
    def close(e=1):
        root1.destroy()
    Button(root1,text='close',bg="#96ece7",command=close).grid(row=4,column=1,pady=10,ipadx=8)
    
    def specific(event):
        lb.delete(0,END)
        p=e11.get()
        cur.execute('select id,fname,lname from contacts where fname LIKE "%{}%" OR lname LIKE "%{}%"'.format(p,p,p))
        global c
        global v
        v=0
        c=cur.fetchall()
        for i in c:
            f=i[1]
            l=i[2]
            f=str(f)
            l=str(l)
            n=f+" "+l
            lb.insert(0,n)
        if v==0:
            lb.bind("<Double-Button-1>",details)
    e11.bind("<Button-1>",specific)
    root1.bind('<Key>',specific)
    con.commit()

#edit function definition
def edit(e=1):
    search()

    
Button(root,text='edit',bg="#10d6d6",command=edit).grid(row=21,column=0,pady=40,padx=px,ipadx=8)
Button(root,text="save", bg="#96ece7", command=save).grid(row=20,column=1, pady=20,padx=px,ipadx=8)
Button(root,text="search",bg="#10d6d6", command=search).grid(row=21,column=2, pady=40,padx=px,ipadx=8)
Button(root,text='exit',bg="#10d6d6", command=exits).grid(row=21,column=1,padx=px,ipadx=8)





from tkinter import *
root=Tk()
root.geometry('700x300')
Label(root,text='Project Title : PhoneBook ',font='Arial 18 bold',fg='#ff1a1a').grid(row=0,column=0,padx=20)
Label(root,text='Project of Python and Database ',font='Arial 16 bold').grid(row=1,column=1,sticky='E')
Label(root,text='Developed by : Palak Modi ',font='Arial 14 ',fg='#473fd9').grid(row=2,column=1,sticky='E')
Label(root,text='---------------------------------------------------',fg='#473fd9').grid(row=7,column=1)
Label(root,text='make mouse movement over this screen to close',font='Arial 8',fg='#ff1a1a').grid(row=8,column=1)

def close(e=1):
    root.destroy()
root.bind('<Motion>',close)
root.mainloop()


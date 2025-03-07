import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.geometry('350x300')
window.title('customer feedback')

a=tk.StringVar()
b=tk.StringVar()
c=tk.StringVar()

lblname=tk.Label(window,text='Customer name')
lblname.place(x=50,y=50)
txtname=tk.Entry(window,textvariable=a)
txtname.place(x=150,y=50)

lblemail=tk.Label(window,text='Email id')
lblemail.place(x=50,y=100)
txtemail=tk.Entry(window,textvariable=b)
txtemail.place(x=150,y=100)

lblrating=tk.Label(window,text='Rating')
lblrating.place(x=50,y=150)
for i in range(1,6):
    txtrating=tk.Radiobutton(window,text=str(i),variable=c,value=str(i)).place(x=150+30*i,y=150)

def saveinfo():
    # print(a.get())
    # print(b.get())
    # print(c.get())
    messagebox.showinfo('save info','detailed save successfully')
    window.destroy()

btnsubmit=tk.Button(window,text='submit',command=saveinfo)
btnsubmit.place(x=50,y=200)
window.mainloop()

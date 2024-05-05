##import tkinter as tk
##a=tk.Tk()
##pack,grid,place tells the particular place at whick point we have to take the input
##for next step like submit or login we use button()

##b=tk.Button(a,text='hello',bg='red')
####b.pack(side='bottom')
####b.grid(row=0,column=0)
##b.place(x=10,y=10)
##p=tk.Button(a,text='submit',fg='violet')
####p.pack(side='top')
####p.grid(row=1,column=1)
##p.place(x=10,y=60)
##a.mainloop()

##import tkinter as tk
##a=tk.Tk()
##b=tk.Checkbutton(a,text='hello',fg='orange')
####b.pack(side='left')
####b.place(x=10,y=30)
####b.grid(row=0,column=2)
##c=tk.Checkbutton(a,text='choose',fg='pink')
####c.pack(side='left')
####c.place(x=20,y=50)
####c.grid(row=1,column=2)
##a.mainloop()


##import tkinter as tk
##a=tk.Tk()
####l=tk.Label(a,text='hello everyone',fg='red')
######l.pack()
######l.place(x=10,y=20)
####l.grid(row=0,column=1)
##l1=tk.Label(a,text='first name').grid(row=0,column=0)
##l2=tk.Label(a,text='last name').grid(row=1,column=0)
##e1=tk.Entry(a).grid(row=0,column=1)
##e2=tk.Entry(a).grid(row=1,column=1)
##
##a.mainloop()

import tkinter as tk
a=tk.Tk()
l=tk.Listbox(a)
l.insert(1,'c')
l.insert(2,'cpp')
l.insert(3,'python')
l.insert(4,'java')
l.pack()
a.mainloop()


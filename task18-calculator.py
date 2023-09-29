import tkinter as tk

root = tk.Tk()

def Click(number):
    n = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(n) + str(number))

    return

def Clear():
    e.delete(0, tk.END) 
    return

def Add():
    a = e.get()
    # a = int(a)
    sum1.append(a)
    e.delete(0, tk.END)
    return

def Equal():
    a1 = e.get()
    result = eval(a1)
    e.delete(0, tk.END)
    e.insert(0, result)
    return

def valid(event):
    key = event.keysym
    validkeys = []

    if key not in validkeys:
        e.event_generate('<<InvalidKey>>')
        return 'break'


#Entry, this is the 'visor' of the calculator
e = tk.Entry(root, width=54, border=8, bg='white')
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

e.bind('<Key>', valid)

#Creating a tuple for the sum
sum1 = []

# Defining buttons
b1 = tk.Button(root, text='1', padx=40, pady=21, bg='white', fg= 'black', command =lambda: Click(1)) # To call a function within 'command =', we can't use '()'. If we need to define the parameters, we have to use 'lambda:'
b2 = tk.Button(root, text='2', padx=40, pady=21, bg='white', fg= 'black', command =lambda: Click(2))
b3 = tk.Button(root, text='3', padx=40, pady=21, bg='white', fg= 'black', command =lambda: Click(3))

b4 = tk.Button(root, text='4', padx=40, pady=21, bg='white', fg= 'black', command =lambda: Click(4))
b5 = tk.Button(root, text='5', padx=40, pady=21, bg='white', fg= 'black', command =lambda: Click(5))
b6 = tk.Button(root, text='6', padx=40, pady=21, bg='white', fg= 'black', command =lambda: Click(6))

b7 = tk.Button(root, text='7', padx=40, pady=21, bg='white', fg= 'black', command =lambda: Click(7))
b8 = tk.Button(root, text='8', padx=40, pady=21, bg='white', fg= 'black', command =lambda: Click(8))
b9 = tk.Button(root, text='9', padx=40, pady=21, bg='white', fg= 'black', command =lambda: Click(9))

b0 = tk.Button(root, text='0', padx=40, pady=21, bg='white', fg= 'black', command =lambda: Click(0))

bsum = tk.Button(root, text='+', padx= 21, pady=21, bg='#b89a98', fg= 'black', command =lambda: Click('+'))
bsub = tk.Button(root, text='-', padx= 21, pady=21, bg='#b89a98', fg= 'black', command =lambda: Click('-'))
bdiv = tk.Button(root, text='/', padx= 21, pady=21, bg='#b89a98', fg= 'black', command =lambda: Click('/'))
bprod = tk.Button(root, text='*', padx= 21, pady=21, bg='#b89a98', fg= 'black', command =lambda: Click('*'))
bequal = tk.Button(root, text='=', padx= 40, pady=21, bg='#b89a98', fg= 'black', command =Equal)
bclear = tk.Button(root, text='C', padx= 40, pady=21, bg='#b89a98', fg= 'black', command =Clear)

#Positioning the buttons using .grid
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0)

bsum.grid(row=1,column=3)
bsub.grid(row=2,column=3)
bdiv.grid(row=3,column=3)
bprod.grid(row=4,column=3)
bequal.grid(row=4,column=2)
bclear.grid(row=4,column=1)

#Data validation

















root.mainloop()
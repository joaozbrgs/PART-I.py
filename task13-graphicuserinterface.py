import tkinter as tk

root = tk.Tk()

#Creating texts and layout it using .grid and .pack

# label = tk.Label(root, text="Hello World!")
# label2 = tk.Label(root, text='How are you?')

# label.grid(row=0, column=0)
# label2.grid(row=1, column=0)

# label.pack()

#Entry widgets

# e = tk.Entry(root, width=20, borderwidth=50, bg='green') #this is a field for data input, where the user can type anything
# e.pack()
# e.get()

# #Creating Buttons

# def Click():
#     label = tk.Label(root, text='You clicked the button!')
#     label.pack()

# mButton = tk.Button(text='Clik Me!', padx=50, pady=50, command=Click, fg='black', bg='white')

# mButton.pack()

#Creating a Calculator

# b1 = tk.Button(text=1, padx=12, pady=10).grid(row=3, column=0)
# b2 = tk.Button(text=2, padx=12, pady=10).grid(row=3, column=1)
# b3 = tk.Button(text=3, padx=12, pady=10).grid(row=3, column=2)
# b4 = tk.Button(text=4, padx=12, pady=10).grid(row=2, column=0)
# b5 = tk.Button(text=5, padx=12, pady=10).grid(row=2, column=1)
# b6 = tk.Button(text=6, padx=12, pady=10).grid(row=2, column=2)
# b7 = tk.Button(text=7, padx=12, pady=10).grid(row=1, column=0)
# b8 = tk.Button(text=8, padx=12, pady=10).grid(row=1, column=1)
# b9 = tk.Button(text=9, padx=12, pady=10).grid(row=1, column=2)
# b0 = tk.Button(text=0, padx=12, pady=10).grid(row=4, column=1)

#Trying out entry functions

e2 = tk.Entry(root)
e2.pack()
e2.insert(0, 'enter your name!')

def Click_2():
    label3 = tk.Label(root, text=e2.get())
    label3.pack()

mButton3 = tk.Button(root, padx=20, pady=15, text='Click Me!', command=Click_2, fg='black', bg='white')
mButton3.pack()



root.mainloop()


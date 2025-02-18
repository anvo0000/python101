# https://docs.python.org/3/library/tkinter.html#the-packer
from tkinter import *
window =  Tk()
window.title("GUI program")
window.minsize(width=600, height=300)

# Label
my_label =  Label(text="This is a Label", font=("Aral", 20, "bold"))
# my_label.pack() # this is a requirement code, if not the label won't display on the screen
my_label.grid(column=0, row=0)

#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

my_button = Button(text="Click me", command=button_clicked)
# my_button.pack() # cannot use pack and grid at the same time.
my_button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

# tk.Entry() = Textbox
# tk.Text() = multi lines Entry
input = Entry(width=10)
# text_input.pack()
input.grid(column=3, row=2)

window.mainloop()
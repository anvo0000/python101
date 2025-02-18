# https://docs.python.org/3/library/tkinter.html#the-packer
from tkinter import *
window =  Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)

def button_clicked():
    print("I got clicked")
    mile = int(text_input.get())
    km_converter = str(mile * 1.60934)
    km_converter_label.config(text=km_converter)

# row 0
text_input = Entry(width=10)
text_input.grid(column=1, row=0)
mile_label =  Label(text="Miles", font=("Aral", 10, "bold"))
mile_label.grid(column=2, row=0)

# row 1
my_label =  Label(text="is equal to", font=("Aral", 10, "bold"))
my_label.grid(column=0, row=1)

km_converter_label =  Label(text="0", font=("Aral", 10, "bold"))
km_converter_label.grid(column=1, row=1)

km_label =  Label(text="Km", font=("Aral", 10, "bold"))
km_label.grid(column=2, row=1)

# row 2
my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=2)



window.mainloop()
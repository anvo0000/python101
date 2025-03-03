from json import JSONDecodeError
from tkinter import Tk, Canvas, PhotoImage, Button, Entry, Label, messagebox
import random
import pyperclip
import json

columns_name = ["website", "user_name", "pwd"]
PWD_FILE = "mypwd.json"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = random.randint(8,10)
nr_symbols = random.randint(2,4)
nr_numbers = random.randint(2,4)

def generate_pwd():
    pwd_txt.delete(0, 'end')
    pwd_letter = [random.choice(letters) for _ in range(nr_letters)]
    pwd_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pwd_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    pwd_list = pwd_letter + pwd_symbols + pwd_numbers
    random.shuffle(pwd_list)
    pwd_str = "".join(pwd_list)
    pwd_txt.insert(index=0, string=pwd_str)
    pyperclip.copy(pwd_str)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    print(f"LOG: Save Password Function")
    website = website_txt.get()
    username = username_txt.get()
    pwd = pwd_txt.get()

    if len(website) ==0 or len(username)==0 or len(pwd)==0:
        messagebox.showinfo(title=website,
                            message="Don't let any field is empty")
    else:
        print(f"LOG: Website: {website}")
        data = {}
        new_data = {website:
                        {"email": username,
                         "pwd": pwd
                         }
                    }
        try:
            with open(PWD_FILE, "r") as data_file:
                data = json.load(data_file) # reading the old file
        except FileNotFoundError:
            with open(PWD_FILE, "w") as data_file: # if file not found, then create a new file by "w" mode
                json.dump(new_data, data_file, indent=4)
        except JSONDecodeError:
            data.update(new_data)
        else:
            data.update(new_data)  # if they try block pass, then update the data with new-data
            with open(PWD_FILE, "w") as data_file:
                json.dump(data, data_file, indent=4)  # update the data_file with updated data json.
        finally:
            website_txt.delete(0, 'end')
            pwd_txt.delete(0, 'end')

# ---------------------------- RETRIEVE PASS ------------------------------- #
def search_pwd():
    website = website_txt.get()
    # username = username_txt.get()
    print(f"LOG: Search Password Function: {website}")
    try:
        with open(PWD_FILE, "r") as data_file:
            data = json.load(data_file) # reading the old file
            username = data[website]["email"]
            pwd = data[website]["pwd"]
            messagebox.showinfo(title=website,
                                message=f"user_name = {username}\npassword = {pwd}")
    except FileNotFoundError as err:
        print(f"LOG FileNotFoundError: {err}")
        messagebox.showinfo(title=website,
                            message="No Data File Found.")
    except KeyError as err:
        print(f"LOG KeyError: {err}")
        messagebox.showinfo(title=website,
                            message="No details for the website exists")

    except JSONDecodeError as err:
        print(f"LOG JSONDecodeError: {err}")
        messagebox.showinfo(title=website,
                            message="No details for the website exists")
        with open(PWD_FILE, "w") as data_file:
            json.dump({}, data_file, indent=4)



# ---------------------------- COPY PASSWORD ------------------------------- #
def copy_pwd():
    print("Copy function")
    pyperclip.copy(pwd_txt.get())
    pwd_txt.delete(0, 'end')
    username_txt.delete(0, 'end')
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

row0 = 0
canvas = Canvas(width=200, height=200, highlightthickness=0)
clock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=clock_img)
canvas.grid(row=row0, column=1)

#Website
row1 = 1
website_lbl = Label(text="Website:")
website_lbl.grid(row=row1, column=0)
website_txt = Entry(width=40)
website_txt.grid(row=row1, column=1, columnspan=2)
website_txt.focus()

#Email/Username
row2 = 2
username_lbl = Label(text="Email/Username:")
username_lbl.grid(row=row2, column=0)
username_txt = Entry(width=40)
username_txt.grid(row=row2, column=1, columnspan=2)
username_txt.insert(index=0, string="anvo0000")

row3 = 3
username_lbl = Label(text="Password:")
username_lbl.grid(row=row3, column=0)
pwd_txt = Entry(width=22)
pwd_txt.grid(row=row3, column=1)
generate_button = Button(text="Generate Password", command=generate_pwd)
generate_button.grid(row=row3, column=2)

row4 = 4
add_button = Button(text="Add Password",width=20, command=save)
add_button.grid(row=row4, column=0)
retrieve_button = Button(text="Search Password", command=search_pwd)
retrieve_button.grid(row=row4, column=1)
copy_button = Button(text="Copy Password", command=copy_pwd)
copy_button.grid(row=row4, column=2)


window.mainloop()
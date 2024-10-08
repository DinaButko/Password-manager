from tkinter import *
from tkinter import messagebox
import random
from random import choice, randint, shuffle
import pyperclip
import json

# ------------------------------CONSTANTS----------------------------#

PINK = "#FFE6E6"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_letters = [random.choice(letters) for _ in range(randint(8, 10))]
password_chars = [random.choice(symbols) for _ in range(randint(2, 4))]
password_numbers = [random.choice(numbers) for _ in range(randint(2, 4))]


def generate_password():
    password_list = password_letters + password_chars + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    print(password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_user_data_to_txt():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    # Create a new dictionary to store data in JSON format
    new_data = {website: {
        "email": email,
        "password": password,
    }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.askokcancel(title=website, message=f"Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \n Password: {password} \n Is it okay to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:  # changed data format to .json
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                    with open("data.json", "w") as data_file:
                        # Saving updated data
                        json.dump(data, data_file, indent=4)  # Create a JSON data
            else:
                    # Updating old data with new data
                    data.update(new_data)
                    with open("data.json", "w") as data_file:
                        # Saving updated data
                        json.dump(data, data_file, indent=4)  # Create a JSON data
            finally:
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

# Create a function called find_password()

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:  # changed data format to .json
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found.")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message= f" No details for {website} exists.")






# ---------------------------- UI SETUP ------------------------------- #
# Create a window

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=(PINK))

# Add image to the screen
canvas = Canvas(width=200, height=200, bg=(PINK), highlightthickness=0)
password_manager_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_manager_img)
canvas.grid(column=1, row=0)

# Add Labels
website_label = Label(text="Website", bg=(PINK))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=(PINK))
email_label.grid(column=0, row=2, )

password_label = Label(text="Password:", bg=(PINK))
password_label.grid(column=0, row=3)

# Add text entries

website_entry = Entry(width=21, highlightbackground=(PINK))
website_entry.grid(column=1, row=1)
# Add a cursor for a website entry field
website_entry.focus()

username_entry = Entry(width=38, highlightbackground=(PINK))
username_entry.insert(0, "butkodina@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21, highlightbackground=(PINK))
password_entry.grid(column=1, row=3)

# Add buttons

generate_password_button = Button(text="Generate Password", highlightbackground=(PINK), command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, highlightbackground=(PINK), command=add_user_data_to_txt)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", highlightbackground=(PINK), width=13, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()

from tkinter import *

# ------------------------------CONSTANTS----------------------------#

PINK = "#FFE6E6"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Create a window

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=(PINK))

# Add image to the screen
canvas = Canvas(width=200, height=200, bg=(PINK), highlightthickness=0)
password_manager_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_manager_img)
canvas.grid(column=1, row=0)

# Add Labels
website_label = Label(text="Website", bg=(PINK))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=(PINK))
email_label.grid(column=0, row=2,)

password_label = Label(text="Password:", bg=(PINK))
password_label.grid(column=0, row=3)

# Add text entries

website_entry = Entry(width=38, highlightbackground=(PINK))
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=38, highlightbackground=(PINK))
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21, highlightbackground=(PINK))
password_entry.grid(column=1, row=3)

# Add buttons

generate_password_button = Button(text="Generate Password", highlightbackground=(PINK))
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, highlightbackground=(PINK))
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

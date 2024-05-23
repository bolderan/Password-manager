from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_NAME = "Courier"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


def search():
    website = web_input.get()
    try:
        with open("day29/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}"
            )
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} exists."
            )


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    password_input.delete(0, END)
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_leter = [choice(letters) for item in range(randint(8, 10))]
    password_symlobs = [choice(symbols) for item in range(randint(2, 4))]
    password_number = [choice(numbers) for item in range(randint(2, 4))]

    password_list = password_leter + password_symlobs + password_number

    shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_():
    website_ = web_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website_: {"email": email, "password": password}}
    if len(website_) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Warning", message="Please fill all the empty fields."
        )
    else:
        try:
            with open("day29/data.json", "r") as file:
                # reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("day29/data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("day29/data.json", "w") as file:
                # saving new data
                json.dump(data, file, indent=4)
        finally:
            web_input.delete(0, END)
            password_input.delete(0, END)
            web_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=80, pady=80, bg=YELLOW)


canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file="day29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# website lable=============================================
website_lable = Label(text="Website   :", font=(FONT_NAME, 10, "bold"), bg=YELLOW)
website_lable.grid(column=0, row=1)
# website input
web_input = Entry(width=25)
web_input.focus()
web_input.grid(column=1, row=1, columnspan=1)

# Search button =============================================

search_button = Button(
    text="Search", font=(FONT_NAME, 10, "bold"), width=8, bg="Blue", command=search
)
search_button.grid(column=2, row=1)


# email lable=============================================
email_lable = Label(text="gmail/user:", font=(FONT_NAME, 10, "bold"), bg=YELLOW)
email_lable.grid(column=0, row=2)

# email/username input
email_input = Entry(width=39)
email_input.insert(5, "@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)


# password lable==========================================
password_lable = Label(text="Password  :", font=(FONT_NAME, 10, "bold"), bg=YELLOW)
password_lable.grid(column=0, row=3)
# password input
password_input = Entry(
    width=24,
)
password_input.grid(column=1, row=3)

# button generate
generate_button = Button(
    text="Generate", font=(FONT_NAME, 10, "bold"), bg=RED, command=generate
)
generate_button.grid(column=2, row=3)


# Add generate
add_button = Button(
    text="Add", font=(FONT_NAME, 10, "bold"), width=36, bg=GREEN, command=save_
)
# img = PhotoImage(file="day29/add-icon--endless-icons-21.png") # make sure to add "/" not "\"
# add_button.config(image=img)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()

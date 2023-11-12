from tkinter import messagebox
from tkinter import*
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_code():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    # password_list = []

    #Using list comprehension
    passwords_letters = [choice(letters) for _ in range(nr_letters)]
    passwords_symbols = [choice(symbols) for _ in range(nr_letters)]
    passwords_numbers = [choice(numbers) for _ in range(nr_letters)]

    password_list = passwords_letters + passwords_symbols + passwords_numbers
    shuffle(password_list)

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password) #Quando gerar a senha ja vai estar copiado no teclado para colar no site

    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) < 1 or len(password) < 1:
        messagebox.showerror(title="ERROR!", message="Website or Password can't be empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are details entered: \nEmail: {username}"
                               f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("passwords.txt", mode='a') as file:  # 'w'(write) = reescreve no arquivo. 'r' (readonly) =
                # somente leitura
                file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website")
email_label = Label(text="Email/Username")
password_label = Label(text="Password")
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="w") #se colocar um sticky="ew"ele puxa o grid até o final da coluna
username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2, sticky="w") #se colocar somente o "w" ele alinha
username_entry.insert(0, "rafael@hotmail.com") #Já entra como valor padrão
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, sticky="w")

#Buttons
add = Button(text="Add", command=save)
add.grid(row=4, column=1, columnspan=2, sticky="ew") #ew estica até o final da coluna
generate_password = Button(text="Generate Password", command=generate_code)
generate_password.grid(row=3, column=2, sticky="w")










window.mainloop()
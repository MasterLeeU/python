from tkinter import *
from tkinter import messagebox
from random import choice,randint, shuffle

# ---- Password Generator ---- #
numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n''o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']
symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','-','=','_','+']

pass_letters = [choice(letters) for _ in range(random.randomint(8, 12))]
pass_numbers = [choice(numbers) for _ in range(random.randomint(1, 3))]
pass_symbols = [choice(symbols) for _ in range(random.randomint(1, 3))]

pass_list= []
pass_list.extend(pass_letters)
pass_list.extend(pass_numbers)
pass_list.extend(pass_symbols)

shuffle(pass_list)
password = "".join(pass_list)

# ---- Password Save ---- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }    
    # Check if any fields are empty
    if len(website)== 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please fill out all fields.")
        return
    
    # Check if the website already exists
    with open(shit.json, "w") as data_file:
        json.dump()
    
    #Confirmation
    ok = messagebox.askokcancel(title=website, Message="Please confirm details: \nEmail: {email}"
                                f"")
    
    with open("shit.txt", "a") as data_file:
        data_file.write(f"{website},{email},{password}\n")
        website_entry.delete(0,END)
        password_entry.delete(0, END)
        
# ---- UI Setup ---- #

window = Tk()
window.title("Password Man")
window.config(padx=50, pady=50)
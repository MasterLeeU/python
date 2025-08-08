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
range(0, 100)
for char in range(0, num_letters):
     pass_list.append(random.choice(letters))

for char in range(0, num_numbers):
     pass_list.append(random.choice(numbers))

for char in range(0, num_symbols):
    pass_list.append(random.choice(symbols))

random.shuffle(pass_list)

password = ""
for char in pass_list:
     password += char

# ---- Password Save ---- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password
    
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
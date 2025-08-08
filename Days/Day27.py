# tkinter, args, kwargs

# Movie Pirates of Silicon Valley

import tkinter

# window = tkinter.Tk()
# window.title("Lee Window")
# window.minsize(width=500, height=300)

# #Label
# Lee_label = tkinter.Label(text="This is a Label", font=("Ariel", 24, "bold"))
# Lee_label.pack(side="bottom")

def add(*numbers):
    sum=0
    for n in numbers:
        sum += n
    return sum

def calculate(n, **kwnumbers):
    print(kwnumbers)
    # for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    n += kwnumbers["add"]
    n *- kwnumbers["multiply"]
    print (n)
    
calculate(2, add=3, multiply=5)
    
    



window.mainloop


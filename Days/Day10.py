#Day 10

def format_name(f_name, l_name):
    if f_name == "" or l_name =="":
        return "You did not enter the correct Information"
    f_name.title()
    l_name.title()
    return f"{f_name} {l_name}"

print(format_name(input("What is your first name? \n"), input("What is your last name? \n")))

# #docstrings
# # in between triple ""
#     """this should be a Docstring,
#     A docstring is used to document a function"""

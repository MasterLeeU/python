#Functions, Code Blocks, and While Loops
# Karel the Robot

# Funtions
print("Hello")
num_char = len("Hello")
print(num_char)

def dis_function():
    print("hello")
    print("bye")

dis_function()

#Indentation
def dis_function():
    print("hello") # this is indented
    print("bye")
# indentation is important in python
# Indentation is used to define the scope of a function or a loop
# Indentation should be done with spaces. 

#While Loops
# while #something is true:
    # do something
    print("hello")
    # this will run forever unless you break out of the loop
    # to break out of the loop, you can use a break statement
    # or you can use a condition to break out of the loop
    # for example, if you want to break out of the loop after 10 iterations
    count = 0
    while count < 10:
        print(count)
        count += 1
    # this will print the numbers from 0 to 9
    # you can also use a while loop to create a countdown
    # for example, if you want to create a countdown from 10 to 0
    count = 10
    while count > 0:
        print(count)
        count -= 1
    # this will print the numbers from 10 to 1
    # you can also use a while loop to create a countdown
    # for example, if you want to create a countdown from 10 to 0 
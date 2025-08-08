# Calculator App

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operator["*"](4,8))

n1 = float(input("What is your first number?: "))
for symbol in operator:
    print(symbol)
operator_symbol = input("What operator: ")
n2 = float(input("Second number?: "))

output = print(operator[operator_symbol](n1, n2))

print(output)
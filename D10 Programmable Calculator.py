def add(n1, n2):
    return (n1 + n2)
def subtract(n1, n2):
    return (n1 - n2)
def multiply(n1, n2):
    return (n1 * n2)
def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def operate (n1, n2, op_input, operations):
    ans = operations[op_input](n1, n2)
    return ans

n1 = float(input("Enter the first number - "))

continue_calc = "Y"
while continue_calc.startswith("Y"):
    op_input = input(f"Enter the operation to perform {' '.join(operations.keys())} -> ")
    while op_input not in operations.keys():
        op_input = input(f"Invalid operation entered\nEnter the operation to perform {' '.join(operations.keys())} -> ")
    
    n2 = float(input("Enter the second number - "))

    # Divisor != 0 check for division  
    while op_input == "/" and n2 == 0:
        print("Cannot divide by zero.")
        n2 = float(input("Re-enter the second number - "))

    print(f"{n1} {op_input} {n2} = ")

    n1 = operate(n1, n2, op_input, operations)
    print(f"Answer = {n1}")

    continue_calc = (input("Do you want to continue calculation with the Answer (Y) or Exit the program (N)")).upper().strip()


# Make sure functions dont talk to the user, because such functions cannot be used irl, for in a web server backend 
# Printing can be fine except in special cases, but taking user inputs inside a function is a strict NO
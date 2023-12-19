# Define a function to perform the arithmetic operation
def calculate_expression(x, y, z):
    if y == '+':
        return x + z
    if y == '-':
        return x - z
    if y == '*':
        return x * z
    elif y == '/':
        return x / z

# Prompt the user for input
expression = input("Expression: ")

# Split user input into three parts
x, y, z = expression.split(" ")

# Convert x and z to integers
x, z = int(x), int(z)

# Check for division by zero
if y == '/' and z == 0:
    print("Error: divide by zero not allowed.")
else:
    # Calculate the result
    result = calculate_expression(x, y, z)
    # Format the result to one decimal place and print it
    print(f"{result:.1f}")

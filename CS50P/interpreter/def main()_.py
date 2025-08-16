def main():
    expression = input("Expression: ")  # Example: "3 / 4"

    x, operator, z = expression.split()  # Rename y to 'operator' for clarity
    x = float(x)
    z = float(z)

    if operator == "+":
        print(x + z)
    elif operator == "-":
        print(x - z)
    elif operator == "*":
        print(x * z)
    elif operator == "/":
        print(x / z)
    else:
        print("Not a valid operator.")

main()

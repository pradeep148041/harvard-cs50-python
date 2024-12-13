def calculator(x, operator, z):
    if operator == '+':
        return x + z
    elif operator == '-':
        return x - z
    elif operator == '*':
        return x * z
    elif operator == '/':
        return x / z

def main():
    try:
        user_input = input("Enter an arithmetic expression (e.g., 1 + 1): ")
        x, op, z = map(str, user_input.split())
        x = float(x)
        z = float(z)

        result = calculator(x, op, z)

        print(f"Result: {result:.1f}")

    except ValueError:
        print("Invalid input. Please enter a valid arithmetic expression.")

if __name__ == "__main__":
    main()

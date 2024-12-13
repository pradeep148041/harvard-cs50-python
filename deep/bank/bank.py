def main():

    user_greeting = input("Enter your greeting: ")

    user_greeting = user_greeting.lstrip().lower()

    if user_greeting.startswith("hello"):
        print("$0")
    elif user_greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()

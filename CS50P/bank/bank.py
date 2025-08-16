def main():
    x=value(input("Greeting:").strip())
    print(f"${x}")
    
def value(greeting):
    if greeting == "Hello" or greeting == "Hello, Newman":
        return 0
    elif greeting =="How you doing?":
        return 20
    elif greeting == "What's happening?" or greeting == "What's up?":
        return 100
    else:
        return "Enter valid input"

if __name__ == "__main__":
    main()

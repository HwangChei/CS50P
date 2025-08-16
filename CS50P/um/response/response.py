import validators
def main():
    print(email(input("What's your email address? ")))

def email(s):
    email_address = validators.email(s)
    if email_address:
        return "Valid"
    else:
        return "Invalid"

main()

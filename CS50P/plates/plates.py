def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>=2 and len(s)<=6 and s[0:2].isalpha() :
        for i in range(len(s)):
            if s[i].isdigit():
                if s[i]=="0" :
                    return False
                if not s[i:].isdigit():
                    return False
                break
        return True
    else:
        return False
if __name__ == "__main__":
    main()

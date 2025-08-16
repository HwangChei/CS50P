def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>=2 and len(s)<=6 and s[0:2].isalpha() :
        if s.digit()[0]=="0":
            return False
        else:
            return True
    else:
        return False


main()

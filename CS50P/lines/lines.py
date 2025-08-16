import sys

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    if not sys.argv[1].endswith(".py"):
        print("Not a Python File")
        sys.exit(1)

    try:
        with open(sys.argv[1]) as file:
            count=0
            for line in file:
                if  line.strip().startswith("#") or line.strip() == "":
                    continue
                else:
                    count+=1
            print(count)
    except  FileNotFoundError:
        print("File does not exist")
        sys.exit()


if __name__ == "__main__":
    main()

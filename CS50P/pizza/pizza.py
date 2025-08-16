import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        process_file()

def process_file():
    if not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            table = list(reader)
            headers = table[0]
            rows =  table[1:]
            print(tabulate(rows, headers, tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()

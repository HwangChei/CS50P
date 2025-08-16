import sys
import csv
def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        check_process(input_file, output_file)

def check_process(input_file, output_file):
    try:
        with open(input_file) as csvfile:
            reader = csv.DictReader(csvfile)

            with open(output_file, 'w', newline = '') as file:
                writer = csv.writer(file)
                writer.writerow(["first", "last", "house"])

                for row in reader:
                    sur_name, first_name = row['name'].split(',')
                    sur_name = sur_name.strip()
                    first_name = first_name.strip()
                    house = row['house']
                    writer.writerow([first_name, sur_name, house])

    except FileNotFoundError:
        print(f"Could not read {input_file }")
        sys.exit(1)

if __name__ == "__main__":
    main()

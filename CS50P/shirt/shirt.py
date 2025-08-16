import sys
from PIL import Image, ImageOps
def main():
    valid()
    input = sys.argv[1]
    output = sys.argv[2]
    pic_converter(input, output)

def valid():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif not sys.argv[1].endswith((".jpg", ".jpeg", ".png")) or not sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

def pic_converter(input, output):
    try:
        if input.split(".")[-1] != output.split(".")[-1]:
            sys.exit("Input and output have different extensions")

        else:
            with Image.open(input) as ip:
                shirt = Image.open("shirt.png")
                fit = ImageOps.fit(ip, shirt.size)
                fit.paste(shirt, (0, 0), shirt)
                fit.save(output)
    except FileNotFoundError:
        sys.exit("Input does not exist")
if __name__ == "__main__":
    main()

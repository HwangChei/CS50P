def main():
    x=input("Input:")
    x=shorten(x)
    print("Output:",end="")
    print(x,end="")
    print()


def shorten(word):
    twttr=set("aAeEiIoOuU")
    for letter in twttr:
        if letter in word:
            return word.replace(letter,"")


if __name__ == "__main__":
    main()

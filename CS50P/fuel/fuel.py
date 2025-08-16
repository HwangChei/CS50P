def main():
    while True:
        try:
            fraction = convert(input("Fraction:"))
            percentage = gauge(fraction)
            if percentage == False:
                continue
            else:
                print(percentage)
                break
        except (ValueError, ZeroDivisionError):
            continue


def convert(a):
    x, y = a.split("/")
    x, y = int(x), int(y)
    a = round(x/y, 2)
    if x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    return int(a*100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

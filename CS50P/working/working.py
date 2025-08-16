import re
import sys

def main():
    try:
        print(convert(input("Hours: ").strip()))
    except ValueError:
        raise ValueError
    sys.exit(0)

def convert(s):
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s)
    if time is None:
        raise ValueError

    x = int(time.group(1))
    y = int(time.group(4))
    a = int(time.group(2)) if time.group(2) else 0
    b = int(time.group(5)) if time.group(5) else 0

    if x > 12 or y > 12 or a >= 60 or b >= 60:
        raise ValueError

    m1 = time.group(3)
    m2 = time.group(6)

    if m1 == "PM" and x != 12:
        x += 12
    if m1 == "AM" and x == 12:
        x = 0
    if m2 == "PM" and y != 12:
        y += 12
    if m2 == "AM" and y == 12:
        y = 0

    return f"{x:02}:{a:02} to {y:02}:{b:02}"

if __name__ == "__main__":
    main()

import random


def main():
    level = get_level()
    game(level)

def get_level():
    while True:
        try:
            level = int(input("Level:"))
            if level in [1,2,3]:
                 return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


def game(level):
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        a = x+y
        mis = 0
        while mis < 3:
            try:
                user_input = int(input(f"{x} + {y} = "))
                if user_input == a:
                    score += 1
                    break
                else:
                    print("EEE")
                    mis += 1
            except ValueError:
                print("EEE")
                mis += 1

        if mis == 3:
            print(f"{x} + {y} = {a}")

    print(f"Score: {score}")

if __name__ == "__main__":
    main()

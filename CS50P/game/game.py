import random
import sys
def main():
#loop
    while True:
        try:
            #input and check
            level=int(input("Level:"))
            answer=random.randint(1,level)
            if level >= 1:
                core(answer)
                break
            else:
                continue
        except ValueError:
                 continue

def core(answer):
    while True:
            try:
                guess=int(input("Guess:"))
                if guess > 0:
                        if guess > answer:
                            print("Too large!")
                            continue

                        elif guess == answer:
                            print("Just right!")
                            sys.exit()

                        else:
                            print("Too small!")
                            continue
                else:
                    continue
            except ValueError:
                 continue

main()

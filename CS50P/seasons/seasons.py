from datetime import date
import inflect
import sys

class Person:

    #returns/ prints how many mins in english letters and no "and"
    def __init__(self, birth):
        self.birth = birth

    def Convert(self):
        p = inflect.engine()
        today = date.today()
        delta = abs(today - self.birth)
        into_mins = delta.days*24*60
        x = (p.number_to_words(into_mins, andword="")).capitalize()
        print(f'{x} minutes')


def main():
    ask()

def ask():
    try:
        convert = Person(date.fromisoformat(input("Date of Birth: ")))
        convert.Convert()
    except ValueError:
        sys.exit(1)
if __name__ == "__main__":
    main()

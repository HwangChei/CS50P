import re
import sys

def main():
    print(count(input("Text: ")))
    sys.exit(0)

def count(s):
    try:
        if um:=re.findall(r"\bum\b",s,re.IGNORECASE):
                return len(um)
    except ValueError:
        sys.exit(0)

if __name__ == "__main__":
    main()

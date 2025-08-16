import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    url = re.search(r'<iframe[^>]*[\w\"\=]*src="https?://(www\.)?youtube\.com/(embed/)?([\w\-]{11})', s)
    if url:
        return f"https://youtu.be/{url.group(3)}"

    else:
        return None


if __name__ == "__main__":
    main()

def main():
    d = {}

    while True:
        try:
            item = input()
            n = item.upper()
            if n in d:
                d[n] += 1
            else:
                d[n]=1
        except EOFError:
            break
    for key, count in sorted(d.items()):
        print(count, key)

main()

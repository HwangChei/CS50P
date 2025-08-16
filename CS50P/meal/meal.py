def main():
    x=convert(input("What time is it?"))
    if 7<=x<=8:
        print("breakfast time")
    elif 12<=x<=13:
        print("lunch time")
    elif 18<=x<=19:
        print("dinner time")
def convert(time):
    hour,min=time.split(":")
    hour=float(hour)
    min=float(min)
    a=hour+min/60
    return a

if __name__ == "__main__":
    main()

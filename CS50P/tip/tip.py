def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    if "$" in d:
        a=float(d.replace("$",""))
        return a

def percent_to_float(p):
    if "%" in p:
        b=float(p.replace("%",""))
        b=b/100
        return b


main()

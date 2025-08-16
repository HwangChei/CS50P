#list
m=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
while True:
    try:
#input/check
        date=input("Date:").strip()
        if "/" in date:
            month,day,year=date.split("/")
            month,day,year=int(month),int(day),str(year)

            if day >= 1 and day <= 31 and month >=1 and month <= 12:
                print(year+"-",end="")
                print(f"{month:02}"+"-",end="")
                print(f"{day:02}",end="")

                break
        elif "," in date:
            time,year=date.split(",")
            month,day=time.split(" ")
            day,year=int(day),int(year)
            h=(m.index(month))
            h=h+1

            if day >= 1 and day <= 31:
                year=str(year)
                print(year+"-",end="")
                print(f"{h:02}"+"-",end="")
                print(f"{day:02}")

                break

    except (ValueError, ZeroDivisionError):
        continue


def main():
    x=input("File Name:")
    x=x.lower()
    if ".gif"in x:
        print("image/gif")
    elif ".png" in x:
        print("image/png")
    elif ".jpg" in x:
        print("image/jpeg")
    elif ".jpeg" in x:
        print("image/jpeg")
    elif ".pdf" in x:
        print("application/pdf")
    elif ".zip" in x:
        print("application/zip")
    elif".txt" in x:
        print("text/plain")
    else:
        print("application/octet-stream")


main()


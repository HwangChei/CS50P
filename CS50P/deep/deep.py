x=input("What is the Answer to the Great Question Of Life, the Universe and Everything?")
x=x.lower()
if "42" in x or "forty two" in x or "-" in x:
    print("Yes")
else:
    print("No")

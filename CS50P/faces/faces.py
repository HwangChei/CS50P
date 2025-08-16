x=input("")
if ":)" in x:
    x=x.replace(":)","🙂")
    print(x)
if ":(" in x:
    x=x.replace(":(","🙁")
    print(x)
else:
    print(x)

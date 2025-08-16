Due=50
while Due>0:
    print("Amount Due:",Due)
    insert=int(input("Insert Coin:"))
    if insert==25 or insert==10 or insert==5:
        Due-=insert
if Due<=0:
    Due=abs(Due)
    print("Change Owed:",Due)
    






import inflect
p = inflect.engine()

def main():
    name_list=[]
#try and except
    while True:
        try:
            name=input("Name:")
            name_list+=[name]

        except EOFError:
            print("Adieu, adieu, to",p.join(name_list))
            break

main()


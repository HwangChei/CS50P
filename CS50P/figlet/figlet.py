from pyfiglet import Figlet
import sys
def main ():
    if len(sys.argv) == 3 and sys.argv[1] in ["-f","--font"]:
        if  sys.argv[2] in Figlet().getFonts():
            x=input("Input: ")
            f = Figlet(font=sys.argv[2])
            print("Output:",f.renderText(x))
        else:
            exit()
    else:
        exit()

def exit():
    print("Invalid usage")
    sys.exit(1)
main()

from gooey import Gooey, GooeyParser
import matplotlib.pyplot as plt

class Expenses:
    def __init__(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def mean(self):
        mean = (self._a + self._b+ self._c+ self._d)/4
        print(f"YOUR AVERAGE EXPENSES IS 💲{mean}")

    def total(self):
        all = self._a + self._b+ self._c+ self._d
        print(f"TOTAL EXPENSES: 💲{all}")

@Gooey(program_name="Expenses", default_size=(1280,568))
def main():
    """
    All the inputs and store through parser and args
    Setting the default value to 0 incase of user not having/wanting expenses
    """
    parser = GooeyParser(description="")
    parser.add_argument('--grocery', action="store", type=int, metavar="Grocery Expenses🛒",default=0)
    parser.add_argument('--rent', action="store",  type=int, metavar="Rent🏠", default=0)
    parser.add_argument('--tuition', action="store", type=int, metavar="Tuition Fees🎓", default=0)
    parser.add_argument('--utility', action="store", type=int, metavar="Utilities Fees🔌", default=0)
    parser.add_argument("option", choices=["BARGRAPH📊 ", "PIECHART🥧", "BOTH📶"], metavar="Data Graph")
    args = parser.parse_args()
    a = args.grocery
    b = args.rent
    c = args.tuition
    d = args.utility
    exps = Expenses(a, b, c, d)

    #Calling the function based on users choosen options
    if args.option == "BARGRAPH📊 ":
        bargraph(a, b, c, d)

    elif args.option == "PIECHART🥧":
        piechart(a, b, c, d)

    elif args.option == "BOTH📶":
        bargraph(a, b, c, d)
        piechart(a, b, c, d)
    #calling the total and mean methods
    exps.total()
    exps.mean()
    maximum(a,b,c,d)

def maximum(a,b,c,d):
    m = max(a, b, c, d)
    if m == a:
        print(f'GROCERY HAS THE HIGHEST EXPENSES BEING 💲{a}')

    elif m == b:
        print(f'RENT HAS THE HIGHEST EXPENSES BEING 💲{b}')

    elif m == c:
        print(f'TUITION HAS THE HIGHEST EXPENSES BEING 💲{c}')

    elif m == d:
        print(f'UTILITY HAS THE HIGHEST EXPENSES BEING 💲{d}')

def bargraph(a, b, c, d):
    labels = ['GROCERY', 'RENT', 'TUITION', 'UTILITY']
    values = [a, b, c, d]
    bars = plt.bar(labels, values, color = 'beige')
    bars[0].set_hatch('xo')
    bars[1].set_hatch('/x')
    bars[2].set_hatch('///')
    bars[3].set_hatch('/-')
    plt.show()

def piechart(a, b, c, d):
    labels = ['GROCERY', 'RENT', 'TUITION', 'UTILITY']
    colors=['red','grey','beige','violet']
    explode=(.1,0,0,.1)
    #2% = 1% meaning plt doesnt let auto% give '%'str so have to take 2'%'
    plt.pie([a, b, c, d], labels = labels, colors = colors, autopct='%.2f %%', explode=explode)
    plt.title('Your Expenses')
    plt.show()

if __name__ == "__main__":
    main()

# Adding in colourful text
class Colour:
    Black = "\u001b[30m"
    Red = "\u001b[31m"
    Green = "\u001b[32m"
    Yellow = "\u001b[33m"
    Blue = "\u001b[34m"
    Magenta = "\u001b[35m"
    White = "\u001b[37m"
    Cyan = "\u001b[36m"
    Reset = "\u001b[0m"
    bracketsymbol = Blue
    normaltext = Cyan
    plussymbol = Red
    lines = White
    text = Yellow

class Menu():
    # Takes in three optional attributes to change the title, options shown and result type given (index, actually value)
    def __init__(self, title="Menu",options=[],result='index'):
        self.title = title
        self.options = options
        self.result = result

    def show(self):
        # Displays the title of the menu
        print(f"{Colour.bracketsymbol}[{Colour.plussymbol}+{Colour.bracketsymbol}]{Colour.Yellow} {self.title}\t",end="")
        if type(self.options) == type([]):
            # Displays the options given
            for index, option in enumerate(self.options):
                print(f"{Colour.Yellow}[{index+1}] {option}\t",end="")
            print(f"{Colour.Reset}\n")
        elif type(self.options) == type(""):
            print(f"{Colour.Yellow}[1] {self.options}{Colour.Reset}\n",end="")
        # Stores the value of the user input
        self.value = getinput(self.title, self.options, self.result)
    # Set the default values if no attributes are given
    def update(self, title=None, options=None, result=None):
        if title != None:
            self.title = title
        if options != None:
            self.options = options
        if result != None:
            self.result = result


class List():
    def __init__(self, title="List",options=[],result='index'):
        self.title = title
        self.options = options
        self.result = result

    def show(self):
        print(f"{Colour.bracketsymbol}[{Colour.plussymbol}+{Colour.bracketsymbol}]{Colour.Yellow} {self.title}")
        if type(self.options) == type(""):
            self.options = [self.options]

        for index, name in enumerate(self.options, 1):
            display(f'{index} - {name}')

        self.value = getinput('Option',self.options,self.result)

    def update(self, title=None, options=None, result=None):
        if title != None:
            self.title = title
        if options != None:
            self.options = options
        if result != None:
            self.result = result

# Function to get input with formated and coloured chacters
def getinput(title, options, result):
    while True:
        try:
            if not options:
                return "Error: No options found"

            choice = int(input(f"({Colour.text}{title}{Colour.Reset}) > "))

            if 0 < choice <= len(options):
                if result == 'value':
                    return options[choice-1]
                else:
                    return choice
            else:
                display("Invalid Option")
        except Exception:
            display("Invalid Option")

# Displays text in a nice colourful format
def display(text):
    print(f"{Colour.bracketsymbol}[{Colour.plussymbol}+{Colour.bracketsymbol}] {Colour.Reset}{text}\n")

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

# Function to get input with formated and coloured chacters
def getinput(title, options, result):
    while True:
        try:
            if not options:
                return "Error: No options found"

            choice = int(input(f"({Colour.text}{title}{Colour.Reset}) > "))

            if 0 < choice <= len(options):
                if result == 'index':
                    return choice
                else:
                    return options[choice]
            else:
                display("Invalid Option")
        except Exception:
            display("Invalid Option")

# This function allows the user to display a formatted menu to the cli and get input based on the options provided
def menu(title="Menu",options=[],result='index'):
    print(f"{Colour.bracketsymbol}[{Colour.plussymbol}+{Colour.bracketsymbol}]{Colour.Yellow} {title}\t",end="")
    if type(options) == type([]):
        for index, option in enumerate(options):
            print(f"{Colour.Yellow}[{index+1}] {option}\t",end="")
        print(f"{Colour.Reset}\n")
    elif type(options) == type(""):
        print(f"{Colour.Yellow}[1] {options}{Colour.Reset}\n",end="")

    return getinput(title, options, result)

# Displays text in a nice colourful format
def display(text):
    print(f"{Colour.bracketsymbol}[{Colour.plussymbol}+{Colour.bracketsymbol}] {Colour.Reset}{text}\n")

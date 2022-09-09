# This Program calculates Area of Rectangle or Square

class color:  # Color Class
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print("Rectangle and Square Area Calculator")


def area(number1):
    return number1


def area1(number1, number2):
    return number1 * number2


while True:
    input1 = input(
        "Choose between Rectangle and Square\nIf square then S , if rectangle then R\n(To Quit Type 'quit' or 'q') ")

    if input1 == "S" or input1 == "s" or input1 == "square" or input1 == "Square":
        length = float(input("What is the side-length of your square "))
        Area = float(length * length)
        print("The area of the square is " + str(area(Area)))
        continue

    elif input1 == "R" or input1 == "r" or input1 == "rectangle" or input1 == "Rectangle":

        width = float(input("What is the width of your rectangle "))
        length1 = float(input("What is the length of your rectangle "))
        Area1 = float(width * length1)
        print("The area of the rectangle is " + str(area1(length1, width)))
        continue

    elif input1 == "quit" or input1 == "Quit" or input1 == "q" or input1 == "Q":
        break

    else:
        print("Enter 'S' or 'D'")
        continue

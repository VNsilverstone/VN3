import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    num = random.randint(0,3)

    # Make a variable and initialize it to a random number between 0 and 3

    # If the random number is 0
    input("Enter a Question for the Magic 8 Ball to Answer")
    if num == 0:
        print("Yes")
    else:
        if num == 1:
            print("No")
        else:
            if num == 2:
                print("Maybe you should ask Google?")
            else:
                if num == 3:
                    print("Ask the nearest person near you.")
        # tell the user "Yes"

    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer

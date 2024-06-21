import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment
    for i in range(10):
        if random_number == 1:
            print("Your the Best! Honestly")
        else:
            if random_number == 2:
                print("Your the smartest person on earth")
            else:
                if random_number == 3:
                    print("Your so kind and nice!")
                else:
                    if random_number == 4:
                        print("Your so humble")
                    else:
                        if random_number == 5:
                            print(" Your are so beatiful/handsome.")

    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :) (my mom)

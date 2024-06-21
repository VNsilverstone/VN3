import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    lottery = []
    for i in range(6):
        lottery.append(random.randint(1,100))


    # TODO 2) Display the selected numbers to the user in a pop-up
    answer = simpledialog.askstring(title="Are These Your Lottery Numbers?", prompt=str(lottery), )
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
    if answer == "Yes" or answer == "yes":
        messagebox.showinfo(title="You Won", message="You Just Won the Lottery!!!")
    else:
        if answer == "no" or answer == "No":
            messagebox.showinfo(title,"Sad", message="You did not win the Lottery...")
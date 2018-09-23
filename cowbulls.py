import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Cows And Bulls")
root.geometry("520x400")


def new_sequence():
    global random_sequence, count_guesses
    random_sequence = [random.randrange(0, 10, 1) for i in range(4)]
    count_guesses = 0
    l1.delete('1.0', 'end')


def cows_and_bulls():
    global random_sequence, count_guesses
    try:
        guess_number = [int(d) for d in E1.get()]
    except ValueError:
        messagebox.showinfo("Error", "Not a Valid input")
        return
    if len(guess_number) != 4:
        messagebox.showinfo("Error", "Not a 4-digit number")
        return
    cow = 0
    bull = 0
    count_guess_repeat = []
    save_cow = [10, 10, 10, 10]
    count_guesses += 1
    l2.config(text="Number of Guesses: " + str(count_guesses))
    for j in range(0, len(guess_number)):
        if guess_number[j] == random_sequence[j]:
            cow += 1
            save_cow.insert(j, guess_number[j])
            save_cow.pop(j+1)
    for i in range(0, len(guess_number)):
        if guess_number[i] in random_sequence and guess_number[i] != random_sequence[i]:
            if guess_number.count(guess_number[i]) >= random_sequence.count(guess_number[i]) and guess_number[i] not in save_cow:
                if guess_number[i] in count_guess_repeat:
                    pass
                elif guess_number.count(guess_number[i]) > 1:
                    bull += random_sequence.count(guess_number[i])
                    count_guess_repeat.append(guess_number[i])
                else:
                    bull += random_sequence.count(guess_number[i])
            elif guess_number.count(guess_number[i]) < random_sequence.count(guess_number[i]) and guess_number[i] not in save_cow:
                bull += guess_number.count(guess_number[i])
            elif guess_number.count(guess_number[i]) >= random_sequence.count(guess_number[i]) and guess_number[i] in save_cow:
                if guess_number[i] in count_guess_repeat:
                    pass
                elif guess_number.count(guess_number[i]) > 1:
                    count_cow = save_cow.count(guess_number[i])
                    bull += random_sequence.count(guess_number[i]) - count_cow
                    count_guess_repeat.append(guess_number[i])
                else:
                    count_cow = save_cow.count(guess_number[i])
                    bull += random_sequence.count(guess_number[i]) - count_cow
            elif guess_number.count(guess_number[i]) < random_sequence.count(guess_number[i]) and guess_number[i] in save_cow:
                count_cow = save_cow.count(guess_number[i])
                bull += guess_number.count(guess_number[i]) - count_cow
            else:
                pass
    l1.insert(INSERT, "".join(map(str, guess_number)) + "\n")
    l1.insert(INSERT, str(cow) + " Cows" + " and " + str(bull) + " Bulls" + "\n")
    cow = 0
    bull = 0
    count_guess_repeat = []
    save_cow = [10, 10, 10, 10]
    if guess_number == random_sequence:
        new_sequence()
        l1.insert(INSERT, "YOU WIN!\n")


L1 = Label(root, text="Welcome to Cows And Bulls!").pack()
L2 = Label(root, text="Guess a 4-digit number: ")
L2.place(x=5, y=20)

E1 = Spinbox(root, from_=0, to=10000)
E1.place(x=5, y=55)

B1 = Button(root, text="Guess", command=cows_and_bulls)
B1.pack(side=LEFT, anchor=S, padx=10, pady=10)
B2 = Button(root, text="New Sequence", command=new_sequence)
B2.pack(side=LEFT, anchor=S, padx=10, pady=10)

sb1 = Scrollbar(root)
sb1.pack(side=RIGHT, fill=Y)
l1 = Text(root, height=15, width=30, yscrollcommand=sb1.set)
l1.pack(anchor=E, expand=True, fill=Y)
sb1.config(command=l1.yview)
l2 = Label(root, text="")
l2.place(x=5, y=190)

count_guesses = 0
random_sequence = [random.randrange(0, 10, 1) for i in range(4)]

root.mainloop()

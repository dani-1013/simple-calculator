from tkinter import *


root = Tk()
root.geometry("314x440")
root.resizable(False, False)
root.configure(bg = "#B3CEE5")


# label that displays the users inputs when they press buttons
display = Label(root, background="white", width=50, anchor="w", font=("arial", 40))
display.pack(padx=10, pady=10)


# list where all the numbers + symbols go when user presses buttons
num_list = []


#---------- Functions ----------#


# adds user's inputs into num_list + displays the user's inputs in the label
def show_num(num, list):
   list.append(num)
   display.configure(text="".join(list))


# clears num_list + displays the empty list in the label
def delete_num(list):
   list.clear()
   display.configure(text=list)


# calculates user's inputs
def calculate(list):
   # will only run if the list is not empty
   while len(list) > 0:
    try:
        # combines the items in the list as a string
        answer_str = "".join(list)
        # eval function evaluates the string
        answer = eval(answer_str)
        if answer >= 100000000:
          # turns the answer into scientific notation
          sci_not = "{:.3e}".format(answer)
          # will display scientific notation on the label
          return display.configure(text=sci_not)
        elif answer < 0.01999999999:
          sci_not = "{:.3e}".format(answer)
          return display.configure(text=sci_not)
        else:
          return display.configure(text=answer)
    # if user divides by zero, it will display "error" instead
    except: ZeroDivisionError
    return display.configure(text="Error")
   
#---------- Buttons ----------#


#--- Row 1 ---#
clear = Button(root, text="AC", background="#F7CAC9", width=3, height=1, font=("arial", 20, "bold"), command=lambda: delete_num(num_list)).place(x=10, y=90)
paren1 = Button(root, text="(", background="#F7CAC9", width=3, height=1, font=("arial", 20, "bold"), command=lambda: show_num("(", num_list)).place(x=88, y=90)
paren2 = Button(root, text=")", background="#F7CAC9", width=3, height=1, font=("arial", 20, "bold"), command=lambda: show_num(")", num_list)).place(x=166, y=90)
divide = Button(root, text="÷", background="#F7CAC9", width=3, height=1, font=("arial", 20, "bold"), command=lambda: show_num(" / ", num_list)).place(x=244, y=90)


#--- Row 2 ---#
seven = Button(root, text="7", background="#F7CAC9", width=3, height=1,  font=("arial", 20, "bold"), command=lambda: show_num("7", num_list)).place(x=10, y=160)
eight = Button(root, text="8", background="#F7CAC9", width=3, height=1,  font=("arial", 20, "bold"), command=lambda: show_num("8", num_list)).place(x=88, y=160)
nine = Button(root, text="9", background="#F7CAC9", width=3, height=1,  font=("arial", 20, "bold"), command=lambda: show_num("9", num_list)).place(x=166, y=160)
multiply = Button(root, text="x", background="#F7CAC9", width=3, height=1,  font=("arial", 20, "bold"), command=lambda: show_num(" * ", num_list)).place(x=244, y=160)


#--- Row 3 ---#
four = Button(root, text="4", background="#F7CAC9", width=3, height=1,  font=("arial", 20, "bold"), command=lambda: show_num("4", num_list)).place(x=10, y=230)
five = Button(root, text="5", background="#F7CAC9", width=3, height=1,  font=("arial", 20, "bold"), command=lambda: show_num("5", num_list)).place(x=88, y=230)
six = Button(root, text="6", background="#F7CAC9", width=3, height=1,  font=("arial", 20, "bold"), command=lambda: show_num("6", num_list)).place(x=166, y=230)
subtract = Button(root, text="-", background="#F7CAC9", width=3, height=1,  font=("arial", 20, "bold"), command=lambda: show_num(" - ", num_list)).place(x=244, y=230)


#--- Row 4 ---#
one = Button(root, text="1", background="#F7CAC9", width=3, height=1,  font=("arial", 20, "bold"), command=lambda: show_num("1", num_list)).place(x=10, y=300)
two = Button(root, text="2", background="#F7CAC9", width=3, height=1,  font=("arial", 20, "bold"), command=lambda: show_num("2", num_list)).place(x=88, y=300)
three = Button(root, text="3", background="#F7CAC9", width=3, height=1,  font=("arial", 20, "bold"), command=lambda: show_num("3", num_list)).place(x=166, y=300)
add = Button(root, text="+", background="#F7CAC9", width=3, height=1,  font=("arial", 20, "bold"), command=lambda: show_num(" + ", num_list)).place(x=244, y=300)


#--- Row 5 ---#
zero = Button(root, text="0", background="#F7CAC9", width=8, height=1,  font=("arial", 20, "bold"), command=lambda: show_num("0", num_list)).place(x=10, y=370)
decimal = Button(root, text=".", background="#F7CAC9", width=3, height=1,  font=("arial", 20, "bold"), command=lambda: show_num(".", num_list)).place(x=166, y=370)
equal = Button(root, text="=", background="#F7CAC9", width=3, height=1,  
               font=("arial", 20, "bold"), command=lambda: calculate(num_list)).place(x=244, y=370)


root.mainloop()

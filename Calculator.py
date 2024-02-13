from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x400")
root.resizable(False, False)
root.title("Calculator")
buttons = ttk.Frame(root)
buttons.grid(column=0, row=1, sticky="nsew")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Display screen
display_screen = ttk.Frame(root)
display_screen.grid(column=0, row=0, sticky="e")
result = StringVar(value="0")
display = ttk.Label(display_screen, textvariable=result, font=("TkDefaultFont", 30))
display.grid(column=0, row=0, sticky="e")





def rowConfig(row_number):
    return buttons.rowconfigure(row_number, weight=1)

def columnConfig(column_number):
    return buttons.columnconfigure(column_number, weight=1)

def createButtons(parent, text, command=None):
    return ttk.Button(parent, text=text, command=command, padding=(20, 20))

# Define functions for button clicks
def button_click(value):
    return lambda: displayValue(value)

def enable_buttons():
    for button in one_to_nine:
        button.config(state="normal")


def displayValue(display_value):
        current_value = result.get()

        if display_value == "C":
            result.set("0")  # Clear the display
            enable_buttons()
        elif display_value == "=":
            try:
                result.set(eval(current_value))  # Evaluate expression
                disable_buttons()

            except:
                result.set("Error")

        else:
            if current_value == "0":
                result.set(str(display_value))

            else:
                new_value = current_value + str(display_value)
                result.set(new_value)

                if special_buttons:
                    for button in one_to_nine:
                        button.config(state="normal")

def disable_buttons():
    for button in one_to_nine:
        button.config(state="disabled")








def inverseInt():
    inversed = result.get()
    inversed = -1 * int(inversed)
    result.set(str(inversed))

def add():
    displayValue(" + ")

def substract():
    displayValue(" - ")

def multiply():
    displayValue(" * ")

def divide():
    displayValue(" / ")

def parenthesisFunc():
    x = str(result.get())
    result.set("(" + x + ")")



def percentFunc():
    display_value = result.get()
    try:
        result.set(eval(display_value) / 100)  # Convert percentage to decimal
    except:
        result.set("Error")




# Buttons
plusminus = createButtons(buttons, text="+/-", command=inverseInt)
plusminus.grid(column=0, row=4, sticky="wnes")
zero = createButtons(buttons, text="0", command=button_click(0))
zero.grid(column=1, row=4, sticky="wnes")
comma = createButtons(buttons, text=",", command=button_click("."))
comma.grid(column=2, row=4, sticky="wnes")
equals = createButtons(buttons, text="=", command=button_click("="))
equals.grid(column=3, row=4, sticky="wnes")
one = createButtons(buttons, text="1", command=button_click(1))
one.grid(column=0, row=3, sticky="wnes")
two = createButtons(buttons, text="2", command=button_click(2))
two.grid(column=1, row=3, sticky="wnes")
three = createButtons(buttons, text="3", command=button_click(3))
three.grid(column=2, row=3, sticky="wnes")
plus = createButtons(buttons, text="+", command=add)
plus.grid(column=3, row=3, sticky="wnes")
four = createButtons(buttons, text="4", command=button_click(4))
four.grid(column=0, row=2, sticky="wnes")
five = createButtons(buttons, text="5", command=button_click(5))
five.grid(column=1, row=2, sticky="wnes")
six = createButtons(buttons, text="6", command=button_click(6))
six.grid(column=2, row=2, sticky="wnes")
minus = createButtons(buttons, text="-", command=substract)
minus.grid(column=3, row=2, sticky="wnes")
seven = createButtons(buttons, text="7", command=button_click(7))
seven.grid(column=0, row=1, sticky="wnes")
eight = createButtons(buttons, text="8", command=button_click(8))
eight.grid(column=1, row=1, sticky="wnes")
nine = createButtons(buttons, text="9", command=button_click(9))
nine.grid(column=2, row=1, sticky="wnes")
multiplied = createButtons(buttons, text="X", command=multiply)
multiplied.grid(column=3, row=1, sticky="wnes")
reset = createButtons(buttons, text="C", command=button_click("C"))
reset.grid(column=0, row=0, sticky="wnes")
parenthesis = createButtons(buttons, text="()", command=parenthesisFunc)
parenthesis.grid(column=1, row=0, sticky="wnes")
percent = createButtons(buttons, text="%", command=percentFunc)
percent.grid(column=2, row=0, sticky="wnes")
divided = createButtons(buttons, text="/", command=divide)
divided.grid(column=3, row=0, sticky="wnes")

one_to_nine = [zero ,one, two, three, four, five, six, seven, eight, nine]
special_buttons = [divided, percent, parenthesis, multiplied, comma, plusminus]

# Find number of rows in app
x = buttons.winfo_children()
for i in x:
    max_row = i.grid_info()["row"]
    max_value = 0
    if max_row >= max_value:
        max_value = max_row
    rowConfig(max_value)

# Find number of columns in app
for i in x:
    max_column = i.grid_info()["column"]
    max_value = 0
    if max_column >= max_value:
        max_value = max_column
    columnConfig(max_value)


root.mainloop()

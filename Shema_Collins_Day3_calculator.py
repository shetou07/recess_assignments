import tkinter as tk

def button_click(number):
    current = entry_result.get()
    entry_result.delete(0, tk.END)
    entry_result.insert(tk.END, current + str(number))

def button_clear():
    entry_result.delete(0, tk.END)

def button_add():
    first_number = entry_result.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    entry_result.delete(0, tk.END)

def button_subtract():
    first_number = entry_result.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    entry_result.delete(0, tk.END)

def button_multiply():
    first_number = entry_result.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    entry_result.delete(0, tk.END)

def button_divide():
    first_number = entry_result.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    entry_result.delete(0, tk.END)

def button_equal():
    second_number = entry_result.get()
    entry_result.delete(0, tk.END)
    if math_operation == "addition":
        entry_result.insert(tk.END, f_num + float(second_number))
    elif math_operation == "subtraction":
        entry_result.insert(tk.END, f_num - float(second_number))
    elif math_operation == "multiplication":
        entry_result.insert(tk.END, f_num * float(second_number))
    elif math_operation == "division":
        if float(second_number) != 0:
            entry_result.insert(tk.END, f_num / float(second_number))
        else:
            entry_result.insert(tk.END, "Error: Division by zero")

# This is the window for the calculator
window = tk.Tk()
window.title("Shema Collin's Calculator")

# Create the result entry field
entry_result = tk.Entry(window, width=40, borderwidth=5)
entry_result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define and place number buttons
button_1 = tk.Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

# Define and place operation buttons
button_add = tk.Button(window, text="+", padx=39, pady=20, command=button_add)
button_subtract = tk.Button(window, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = tk.Button(window, text="*", padx=41, pady=20, command=button_multiply)
button_divide = tk.Button(window, text="/", padx=41, pady=20, command=button_divide)
button_equal = tk.Button(window, text="=", padx=91, pady=20, command=button_equal)
button_clear = tk.Button(window, text="Clear", padx=79, pady=20, command=button_clear)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=0, columnspan=4)

# Start the main loop
window.mainloop()

""" Method overriding
import Square as Square


class Cars:
    def drive_me(self):
        print("I'm an automatic car")


class Manual(Cars):
    def drive_me(self):
        print("I use gears, I'm a manual car")

    manual = Manual()
    manual.drive_me()


# Polymorphism
# Helps to write code that can work with different objects.
# Includes -method overriding- Occurs when a derived class(child class) provides its own implemetation of
# a method that is already defined in its parent class.
# - method overloading.- Allows class to have multiple methods with the same name but different parameter
class Shape:
    def calculate_area(self):
        pass


class Square1(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        return 4*self.side
    square = Square1(12)
    square.calculate_area()
"""
import tkinter as tk


def print_receipt():
    # Retrieve input values from the entry fields
    customer_name = name_entry.get()
    item_name = item_entry.get()
    item_price = int(price_entry.get())
    item_quantity = int(quantity_entry.get())
    total = int(item_price * item_quantity)

    # Create the receipt text
    receipt_text = f"Customer: {customer_name}\n\n"
    receipt_text += "Item             Price\n"
    receipt_text += "----------------------------\n"
    receipt_text += f"{item_name}        ${item_price}\n"
    receipt_text += "----------------------------\n"
    receipt_text += f"Quantity:            {item_quantity}\n"
    receipt_text +="----------------------------\n"
    receipt_text += f"Total:           ${total}"

    # Print the receipt
    print(receipt_text)

    # Clear the entry fields
    name_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)


# Create the main window
window = tk.Tk()
window.title("Shema's Receipt Machine ")

# Create labels for the input fields
name_label = tk.Label(window, text="Customer Name:")
item_label = tk.Label(window, text="Item:")
price_label = tk.Label(window, text="Amount:")
quantity_label = tk.Label(window, text="Quantity")

# Create entry fields for the input values
name_entry = tk.Entry(window)
item_entry = tk.Entry(window)
price_entry = tk.Entry(window)
quantity_entry = tk.Entry(window)
# Create a button to print the receipt
print_button = tk.Button(window, text="Print Receipt", command=print_receipt)

# Position the labels, entry fields, and button in the window
name_label.grid(row=0, column=0, sticky="e")
item_label.grid(row=1, column=0, sticky="e")
price_label.grid(row=2, column=0, sticky="e")
quantity_label.grid(row=3, column=0, sticky="e")

name_entry.grid(row=0, column=1, padx=10, pady=5)
item_entry.grid(row=1, column=1, padx=10, pady=5)
price_entry.grid(row=2, column=1, padx=10, pady=5)
quantity_entry.grid(row=3, column=1, padx=10, pady=5)

print_button.grid(row=4, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()



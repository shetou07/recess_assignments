
# Converting celcius degrees to fahrenheit.
def celcius_to_fahrenheit(celcius):
    fahrenheit_degrees = (celcius * 9/5) + 32
    return fahrenheit_degrees
celcius_value = 37
fahrenheit_value = celcius_to_fahrenheit(celcius_value)
print(f"{celcius_value} degrees celcius is equal to {fahrenheit_value} degrees fahrenheit")

#Encapsulation in Python

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def increment_pay(self, increment_amount):
        self._salary += increment_amount


# Employee object
employee = Employee("Ssemakula Peter", 85000)

# Dispalying employee information
print("Employee Information:")
print("Name:", employee.get_name())
print("Salary:", employee.get_salary())

# Incrementing the salary
increment_amount = 15000
employee.increment_pay(increment_amount)

# Displaying the updated salary
print("\nAfter Incrementing Pay:")
print("Name:", employee.get_name())
print("Updated Salary:", employee.get_salary())

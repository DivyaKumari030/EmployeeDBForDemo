# Define the Employee class
class Employee:
    def __init__(self, name, employee_id, address, salary):
        self.name = name
        self.employee_id = employee_id
        self.address = address
        if salary > 45000:
            print("Error: Salary should be less than 45000 per month.")
            self.salary = None
        else:
            self.salary = salary

# Initialize the list of employees
employees = []

# Add employees to the list
employees.append(Employee("Divya Kumari", 123, "123 Main St, Anytown USA", 40000))
employees.append(Employee("Siya Rai", 456, "456 Maple Ave, Anytown USA", 35000))
employees.append(Employee("Samuel Johnson", 789, "789 Oak St, Anytown USA", 42000))
employees.append(Employee("Samantha Akkineni", 101, "101 Elm St, Anytown USA", 38000))
employees.append(Employee("Tom Cruise", 234, "234 Pine St, Anytown USA", 43000))

# Print the employee information
for employee in employees:
    print(f"Name: {employee.name}, Employee ID: {employee.employee_id}, Address: {employee.address}, Salary: {employee.salary}")

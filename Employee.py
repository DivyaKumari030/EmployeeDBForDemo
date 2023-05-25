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
employees.append(Employee("Divya Kumari", 122, "123 Main St, California USA", 40000))
employees.append(Employee("Siya Rai", 456, "456 Maple Ave, Melbourne USA", 35000))
employees.append(Employee("Samuel Johnson", 789, "789 Oak St,Chicago USA", 42000))
employees.append(Employee("Samantha Akkineni", 101, "101 Elm St, New York USA", 38000))
employees.append(Employee("Tom Holland", 234, "234 Pine St, Canada", 43000))
employees.append(Employee("Doja Cat", 234, "234 Pine St, New York USA", 43000))
employees.append(Employee("Teen Thomas", 234, "234 Pine St, Russia", 43000))
employees.append(Employee("Lady Gaga", 234, "234 Pine St, Chian", 43000))
employees.append(Employee("Gagandeep", 234, "234 Pine St, Chian", 43000))


# Print the employee information
for employee in employees:
    print(f"Name: {employee.name}, Employee ID: {employee.employee_id}, Address: {employee.address}, Salary: {employee.salary}")

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount = Employee.empCount + 1

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def displayCount(self):
        print(Employee.empCount)
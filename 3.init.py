class Employee:
    def __init__(self, name, age, salary, gender):
        self.name= name
        self.age= age
        self.salary= salary
        self.gender= gender
    def employee_details(self):
        print("Name of the employee is ", self.name)
        print("Age of the employee is ",self.age)
        print("Salary of the employee is ",self.salary)
        print("Gender of the employee is ",self.gender)
p1= Employee("mohammed", 32, 50000, "male")
p1.employee_details()

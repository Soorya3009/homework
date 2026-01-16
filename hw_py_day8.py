# A fitness center wants to create a simple system to define and display staff profiles based on their roles for record-keeping purposes. You are tasked with creating a Python program to represent different types of staff. Complete the following steps:

# Define a base class Employee with attributes name (string) and role (string), and a method display() that prints the employee’s name and role.
# Create a class Trainer that inherits from Employee, adds an attribute specialization (string), and includes a display() method to print the trainer’s name, role, and specialization.
# Create a class YogaInstructor that inherits from Employee, adds an attribute yoga_style (string), and includes a display() method to print the yoga instructor’s name, role, and yoga style.
# Create a class MultiTrainer that inherits from both Trainer and YogaInstructor, includes both specialization and yoga_style attributes, and has a display() method to print the multi-trainer’s name, role, specialization, and yoga style.
# Create one object from each class (Employee, Trainer, YogaInstructor, MultiTrainer) with sample data.
# Display the details of each object by calling its display() method




class Employee:
    def __init__(self,name,role):
        self.name = name
        self.role = role
    def display(self):
        print("Name: ",self.name)
        print("Role: ",self.role)

class Trainer(Employee):
    def __init__(self, name, specialization):
        super().__init__(name, "Trainer")
        self.specialization = specialization
    def display(self):
        super().display()
        print("Specilization:",self.specialization)

class YogaInstructor(Employee):
    def __init__(self, name, yoga_style):
        super().__init__(name, "Yoga Instructor")
        self.yoga_style = yoga_style
    def display(self):
        super().display()
        print("Yoga Style: ",self.yoga_style)

class MultiTrainer(Trainer,YogaInstructor):
    def __init__(self, name, specialization, yoga_style):
        Employee.__init__(self, name, "Multi Trainer")
        self.specialization = specialization
        self.yoga_style = yoga_style
    def display(self):
        print("Name: ",self.name)
        print("Role: ",self.role)
        print("Specialization: ",self.specialization)
        print("Yoga Style: ",self.yoga_style)

employee = Employee("Miya","Receptionist")
trainer = Trainer("Kiran", "Weight Training")
yogainstructor = YogaInstructor("Meera","Hatha Yoga")
multitrainer = MultiTrainer("Arjun","Strength Training","Power Yoga")

print("Employee")
employee.display()
print("\nTrainer")
trainer.display()
print("\nYoga Instructor")
yogainstructor.display()
print("\nMulti Trainer")
multitrainer.display()
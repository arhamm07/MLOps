class Employee():
    # constructor
    def __init__(self):
        # attributes without uding parameters
        self.id = 123
        self.salary = 10000
        self.designation = "Manager"

    
    # create a method
    def travel(self, destination):
        print("Employee is traveling to", destination)
    

# create an instance/object
sam = Employee()
# prinitng the attributes of the object
print(sam.id, sam.salary, sam.designation)
# calling the method
sam.travel("Hyderabad")

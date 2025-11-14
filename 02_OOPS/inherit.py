# Simple Inheritance


# Parent Class
class Animal():
    def __init__(self,name):
        self.name  = name

    def speak(self):
        print(self.name, 'Makes a sound')


# chlld class
class Dog(Animal):
    def speak(self):
        print(self.name, 'Barks')
 



obj = Animal('Dog')
obj.speak()

dog = Dog('Dog')
dog.speak()
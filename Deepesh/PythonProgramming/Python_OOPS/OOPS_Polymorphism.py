"""
Polymorphism :  when one perticular person perform multiple task, then it is known as polymorphism
There some polymorphism types
-> Method Overriding :  When we setup a inheritance between 2 class, and both the class have method
                      with same name, then child class method, override the parent class method.

-> Method OverLoading : When a class has 2 methods with same name, but different parameter, then it is
                     called method overloading.
                      -> python does not support method overloading, it only consider latest
                      defined method.

-> Operator Overloading

'"""

# Polymorphism

class father:
    def __init__(self, fname, fhouse, fcar):
        self.fname = fname
        self.fhouse = fhouse
        self.fcar = fcar

    def show_father_name(self):
        print("Father name is :", self.fname)

    def show_father_house(self):
        print("Father is owning house:", self.fhouse)

    def show_father_car(self):
        print("Father is owening car ", self.fcar)

    def greeting(self):
        print("From Father class")
        print("Very good evening")

    def addition(self, num1, num2, num3):
        print("addition :", num1+num2+num3)

    def addition(self, num1, num2):
        print("addition :", num1+num2)

class son(father):
    """
    When we setup inheritance between 2 class, then we have initialize the parent class constructor in
    child class using super keyword

    """
    def __init__(self, son_name, fname, fhouse, fcar):
        super().__init__(fname, fhouse, fcar)
        self.son_name = son_name

    def show_son_name(self):
        print(f"The son name is: {self.son_name}")

    def show_all_details(self):
        self.show_father_name()
        self.show_father_car()
        self.show_father_house()
        self.show_son_name()

    def greeting(self):
        print("From Son class")
        print("Very good evening")


obj = son('Rohit', 'Mohan Gupta',  '4 BHK', 'BMW')
obj.show_all_details()
obj.show_father_house()
print("_"*50)
obj.greeting()
obj.addition(50, 60)

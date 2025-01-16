"""
class : Class is nothing but the blueprint of the object where we defined all the properties/method/
        attribute/variables of the object.
object :  Object is the medium through which we can access the properties of the class.
method :  When defined any function inside the class, then it is called method, we have to create
         object of the class to access the methods.
         There are different types of method
         1. Instance/object method :  When we defined any method with self as first parameter, then it is called
                               instance method/object method.
         2. class method. :  When we defined any method with decorator @classmethod and cls as first
                             parameter, then it is called class method. Class method only deals with
                             class variables. 
                             ->  we can call the class method with the help of class name, no need to create
                                 object.
         4. static method. :  static method is associated with class, no need to create object of the class
                            to access the static method.

self :  Self is nothing but the object of the class current class being created.
        ->  when we call any instance method through the object, then internally the first parameter to
            the method is object itself.


constructor : constructor which initialize the memory for the object.

             1. Default constructor: default constructor call by default call internally whenever
                we create the object of the class.
                def __init__():
                    code

             2. Parametrize constructor: When we define the parameter to the constructor, then it
                is called parametrize constructor. we have to provide the value of parameter, while
                creating the object of the class
                def __init__(p1, p2):
                    code

                obj = ABC(30, 40)

variables :  There are different type of variable in the class
            1. instance variable :  when we defined any variable with self, then it is called instance
                        variable. Instance variable are available across the class method.

            2. class variable :  When we defined any variable on class level, then it is known as
                        class variable. we have to provide value to the class variable initially,
                        if we want to change later we can change via class object

Inheritance
Polymorphism
Encapsulation
Data abstraction
"""

var_p = 500
# class with default constructor
class ABC:
    def __init__(self):
        print("Execution started")

    # Instance Method
    def greeting(self):
        print("Good Morning")

# obj = ABC()
#obj.greeting()


# class with parametrized constructor

var_q = 600
class XYZ:
    # class variable
    city = 'Mumbai'

    # parametrized constructor
    def __init__(self, num1, num2):
        print("--- Execution started ---")
        self.n1 = num1  # instance variable
        self.n2 = num2  # instance variable

    # Instance Method
    def greeting(self):
        print("Good Morning")

    # Instance Method
    def addition(self):
        print(f"Addition of values: {self.n1}, {self.n2}: ", self.n1+self.n2)


    @classmethod
    def show_city_name(cls):
        print("city name :", cls.city)
        
    @staticmethod
    def get_factorial(num):
        print("global variable var_q:", var_q)
        fact = 1
        for i in range(num, 0, -1):
            fact = fact*i
        print(f"Factorial of {num}:", fact)
        


obj1 = XYZ(30, 50)
obj1.addition()
obj1.show_city_name()
#obj1.city = 'Kolkata'
obj1.__setattr__('city', 'Bangalore')
obj1.show_city_name()

obj1.__setattr__('n1', 100)
obj1.__setattr__('n2', 200)
obj1.addition()
#print("addition of value :", obj1.n1 + obj1.n2)
print(obj1.city)
print("######### Access method with class name ##############")
XYZ.show_city_name()
#XYZ.addition()
# TypeError: XYZ.addition() missing 1 required positional argument: 'self'


print("######### Access static method with class name ##############")
# No need to create object of the class to access static method.
XYZ.get_factorial(5)


print("######### call the instance method with class name ##############")
# use of self.
obj1.addition()
# XYZ.addition()
# TypeError: XYZ.addition() missing 1 required positional argument: 'self'
XYZ.addition(obj1)

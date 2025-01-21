"""
Abstraction :  When we hide the internal information of the product and provide overview info to the
               user, then it is called Abstraction.

Abstract method : When we impliment the method in child and declare in parent class, then it is known as
                  abstract method.

"""
from abc import abstractmethod

class Animal:

    @abstractmethod
    def animal_name(self):
        pass

    @abstractmethod
    def animal_voice(self):
        pass

    @abstractmethod
    def animal_breed(self):
        pass

class Dog(Animal):

    def animal_voice(self):
        print("Barking")

    def animal_breed(self):
        print("German Shepherd")

    def animal_name(self):
        print("Tommy")

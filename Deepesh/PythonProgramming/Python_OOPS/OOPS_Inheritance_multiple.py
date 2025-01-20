"""
Inheritance in Python

1. Single Inheritance :   class A -> class B
2. Multilevel Inheritance :  class A -> class B ->  class C
# when we have multiple level class inheritance then it is known as multi level inheritance

3. Multiple Inheritance :  class A ->  class B, class C ->  class B
"""


# multiple inheritance

class Mother:
    def __init__(self, m_name, m_business):
        self.m_name = m_name
        self.m_business = m_business

    def show_mother_name(self):
        print(f"Mother Name: {self.m_name}")

    def show_mother_property(self):
        print(f"Mother Property: {self.m_business}")



class father():
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


class son(father, Mother):
    """
    -> When we setup inheritance between 2 class, then we have initialize the parent class constructor in
    child class using super keyword
    -> MRO (Method Resolution Order) :  When we setup a multiple inheritance, then MRO concept will word.
       It means whichever first class name is defined, that class constructor will get priority to
       initialize.

    """

    def __init__(self, son_name, fname, fhouse, fcar, m_name, m_business):
        super().__init__(fname, fhouse, fcar)
        self.mobj = Mother(m_name, m_business)
        self.son_name = son_name

    def show_son_name(self):
        print(f"The son name is: {self.son_name}")

    def show_all_details(self):
        self.mobj.show_mother_name()
        self.mobj.show_mother_property()
        self.show_father_name()
        self.show_father_car()
        self.show_father_house()
        self.show_son_name()


obj = son('Rohit', 'Mohan Gupta', '4 BHK', 'BMW', 'Rohini', 'Fashion')
obj.show_all_details()


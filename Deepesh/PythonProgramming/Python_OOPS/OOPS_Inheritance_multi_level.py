"""
Inheritance in Python

1. Single Inheritance :   class A -> class B
2. Multilevel Inheritance :  class A -> class B ->  class C
# when we have multiple level class inheritance then it is known as multi level inheritance

3. Multiple Inheritance :  class A ->  class B, class C ->  class B
"""


# multi inheritance

class grandfather:
    def __init__(self, gf_name, gf_property):
        self.grand_father_name = gf_name
        self.grand_father_property = gf_property

    def show_grand_father_name(self):
        print(f"GrandFather Name: {self.grand_father_name}")

    def show_grand_father_property(self):
        print(f"Grand Father Property: {self.grand_father_property}")


class father(grandfather):
    def __init__(self, fname, fhouse, fcar, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
        self.fname = fname
        self.fhouse = fhouse
        self.fcar = fcar

    def show_father_name(self):
        print("Father name is :", self.fname)

    def show_father_house(self):
        print("Father is owning house:", self.fhouse)

    def show_father_car(self):
        print("Father is owening car ", self.fcar)


class son(father):
    """
    When we setup inheritance between 2 class, then we have initialize the parent class constructor in
    child class using super keyword

    """

    def __init__(self, son_name, fname, fhouse, fcar, gf_name, gf_property):
        super().__init__(fname, fhouse, fcar, gf_name, gf_property)
        self.son_name = son_name

    def show_son_name(self):
        print(f"The son name is: {self.son_name}")

    def show_all_details(self):
        self.show_grand_father_name()
        self.show_grand_father_property()
        self.show_father_name()
        self.show_father_car()
        self.show_father_house()
        self.show_son_name()


obj = son('Rohit', 'Mohan Gupta', '4 BHK', 'BMW', 'Madanlal', '200Acr')
obj.show_all_details()
obj.show_grand_father_property()


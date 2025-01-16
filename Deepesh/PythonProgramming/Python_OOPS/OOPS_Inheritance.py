"""
Inheritance in Python

1. Single Inheritance :   class A -> class B
2. Multilevel Inheritance :  class A -> class B ->  class C
3. Multiple Inheritance :  class A ->  class B, class C ->  class B
"""
# single inheritance
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


class son(father):
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


obj = son('Rohit', 'Mohan Gupta',  '4 BHK', 'BMW')
obj.show_all_details()

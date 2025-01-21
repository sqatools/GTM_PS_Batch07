"""
Data Hiding : When we want to restrict the data sharing out side of the class, then it is known as
            data hiding.

Data hiding in python can be achieved with the help single _ and double __ as prefix in the
variable/method name.

->  If we defined any method/variables with single/double underscore as prefix, thn
    methods/variables will not show in suggestion list

-> The variable/method with single underscore as prefix won't show in suggestion list, but
   still if we want to access it, we can access with name.


"""


class Car:
    def __init__(self, car_name, car_comp, car_price):
        self.car_name = car_name
        self._car_company = car_comp
        self.__car_price = car_price

    def show_car_name(self):
        print("Car name is :", self.car_name)

    def _show_car_company_name(self):
        print("Car Company Name :", self._car_company)

    def __show_car_price(self):
        print("Car Price :", self.__car_price)

    def show_car_details(self):
        self.show_car_name()
        self._show_car_company_name()
        self.__show_car_price()


obj = Car('Curvv', 'TATA', '20 lac')


# The variable/method with single underscore as prefix won't show in suggestion list, but
#  still if we want to access it, we can access with name.
obj._show_car_company_name()

# The variable/method with double underscore as prefix won't show in suggestion list, but
# still we want to access the data, then we have follow the rule .e.g  _classname__variable/method
#obj.__show_car_price()

obj._Car__show_car_price()


print("_"*50)
obj.show_car_details()

str1 = "Hello"
str1.upper()

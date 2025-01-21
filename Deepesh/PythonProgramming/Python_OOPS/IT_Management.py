
class ITService:
    def __init__(self, comp_name, comp_address, comp_product):
        self.comp_name = comp_name
        self.comp_address = comp_address
        self.comp_product = comp_product

    def show_company_name(self):
        print("The company name :", self.comp_name)


if __name__ == '__main__':
    """
    # each python file is called module
    # Default module name of each file is __main__
    """
    obj = ITService('TCS', 'Hinjewadi Pune', 'Container Service')
    print("Module name :", obj.__module__)
    print("Class name :", obj.__class__)
    print("Module name :", __name__)
    obj.show_company_name()

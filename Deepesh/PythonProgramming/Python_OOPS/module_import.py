# import specific class
# from IT_Management import ITService

# import all method/variables/classes
from IT_Management import *


# create object of the class
obj = ITService('TechM', 'Pune Hinjewadi', 'Weather API')
print(obj.__module__)
obj.show_company_name()

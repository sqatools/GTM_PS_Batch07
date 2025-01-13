from faker import Faker
"""
pip install Faker
"""
fk = Faker()
print(dir(fk))
for i in range(50):
    print(i)
    print("Username :", fk.user_name())
    print("Email :", fk.email())
    print("Phone :", fk.phone_number())
    print("_"*50)

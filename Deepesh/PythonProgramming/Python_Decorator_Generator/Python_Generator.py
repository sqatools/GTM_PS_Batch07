def greeting_msg():
    return "good morning"
    return "good evening"


output = greeting_msg()
print(output)


def greeting_generator():
    yield "Good Morning"
    yield "Good Evening"
    yield "Good Afternoon"
    yield "Hope you are doing good"
    yield "Thank you"


var = greeting_generator()
print(var)
"""
print(next(var)) # Good Morning
print(next(var)) # Good Evening
print(next(var)) # Good Afternoon
print(next(var)) # Hope you are doing good
print(next(var)) # Thank you
#print(next(var)) # StopIteration
"""

for data in var:
    print(data)


def get_list_square_value(list1):
    for data in list1:
        return data**2


output = get_list_square_value([4, 5, 7, 2, 8])
print(output)

# generator code
def get_list_square_value2(list1):
    for data in list1:
        yield data**2


print("_"*40)
output2 = get_list_square_value2([6, 7, 2, 8, 12, 56, 44])
for val in output2:
    print(val)



import tracemalloc

def get_list_square_value(list1):
    for data in list1:
        print(data**2)

def get_list_square_value2(list1):
    for data in list1:
        yield data**2


tracemalloc.start()

get_list_square_value([4, 5, 7, 2, 8]*100000)
for val in get_list_square_value2([4, 5, 7, 2, 8]*100000):
    print(val)

print("memory usage :", tracemalloc.get_tracemalloc_memory())
# generator code

tracemalloc.stop()



print(dir(set))

# add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
# 'intersection', 'intersection_update', 'isdisjoint', 'issubset',
# 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update']

set1 = {1, 2, 3, 4}
set1.add(5)
print(set1)

# {1, 2, 3, 4, 5}

print()
set2 = {5, 6, 7, 8}
set2.clear()
print(set2)
# set()

print()
set3 = {2, 4, 7, 88, 99, 123, 43, 67}
set4 = {45, 65, 88, 2, 98, 23, 67, 43}

set3.difference(set4)
set4.difference(set3)

print(set3)
print(set4)



print("-"*50)
set5 = {2, 4, 7, 88, 99, 43, 67}
set6 = {45, 65, 88, 98, 23, 43}

set5.difference_update(set6)
print(set5)
# {2, 67, 99, 4, 7}


set6.difference_update(set5)
print(set6)
# {65, 98, 23, 88, 43, 45}

print("-"*50)

set8 = {"hai", "i", "am", "satya"}
set9 = {"this", "is", "santhi", "hai", "i"}
#set8.difference(set9)
set9.difference(set8)
print(set8)
print(set9)

#set8.difference_update(set9)
print(set8)
# {'am', 'satya'}
set9.difference_update(set8)
print(set9)
# {'santhi', 'hai', 'i', 'this', 'is'}


print("-"*50)
set10 ={1, 2, 3, 4, 5}
set11 = {6, 7, 8, 9}

set10.intersection(set11)
print(set10)

#set11.intersection(set11)
print(set10)

set10.difference_update(set11)
print(set10)
print()
set11.intersection_update(set10)
print(set11)

print("-"*50)

set13 = {1, 3, 4, 5, 8,7, 9}
set14 = {2, 4, 6, 8, 10}

set14.intersection_update(set13)
print(set14)


set13.difference_update(set14)
print(set13)

set13.intersection_update(set14)
print(set13)


set15 = {1, 2, 3, 4}
set16 = {3, 4, 5, 6}

set15.intersection_update(set16)
print(set15)


set17 = {1, 2, 3, 4}
set18 = {3, 4, 5, 6}

set18.intersection_update(set17)
print(set18)


set17.intersection_update(set18)
print(set17)

set17.intersection(set18)
print(set17)


set19 = {1,2, 3, 4, 5}
set20= {3, 4, 5, 6, 7}

set19.intersection(set20)
print(set19)

set19.difference_update(set20)
print(set19)

set19.difference(set20)
print(set19)

print("-"*50)
set21 = {1,2, 3, 4, 5}

set21.pop()
print(set21)

set21.discard(2)
print(set21)

set21.remove(3)
print(set21)

set21.discard(7)
print(set21)

print("-"*50)

set25 = {"a", "b", "c", "d"}
set26 = {"e", "f", "g", "h"}

set25.add(23)
print(set25)


set25.update(set26)
print(set25)


set26.union(set25)
print(set26)


print("-"*50)
set27 = {1, 2, 3, 4, 5, 6, 7}
set28 = {6, 3, 5}

set28.issubset(set27)

print(set28)

set28.issuperset(set27)
print(set28)

set27.issubset(set28)
print(set27)


set30 = {1, 2, 3, 4, 5,6 ,7, 8, 9}
set31 = {4, 5, 7, 10}

set31.issubset(set30)
print(set31)

set30.issuperset(set31)
print(set30)

set32 = {1, 2, 3, 4, 5}
set32.discard(2)
set32.discard(22)
print(set32)
set32.remove(4)
print(set32)

print()
set_p = {"a", "b", "c", "d", 3, 5, 7}
set_q = {"d", 3, 5}
set_r = {"a", "b", 35}

print(set_q.issubset(set_p)) # True

print(set_p.issuperset(set_q)) # True
print(set_p.issuperset(set_r)) # False

print(set_q.isdisjoint(set_r)) # True

set_x = {4, 5, 6, 7}
set_y = set_x
set_y.add(8)

print(set_x) # {4, 5, 6, 7, 8}

print(set_y) #{4, 5, 6, 7, 8}

set_a = {1, 2, 3, 4}
set_b = set_a.copy()
set_b.add(6)

print(set_a) # {1, 2, 3, 4}
print(set_b) # {1, 2, 3, 4, 6}


set_c = {1, 3, 5, 6}
set_c.clear()
print(set_c) # set()

# common values between two sets

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 2, 4, 5]

result = set(list1).intersection(set(list2))
print(result) # {2, 4, 5}

for val in list1:
    if val in list2:
        print(val, end="")


common = []
for val in list1:
    if val in list2:
        common.append(val)
    else:
        continue
print(common)
# [2, 4, 5]







tup1 = (3, 5, 7, 8, 12, 5, 7)
print(tup1, type(tup1))


tup2 = (
    3, 43.5, 'Hello',[3, 5, 7],
    (7, 8, 9), {'a' : 123, 'b': 345, 'c': 3343},
    {4, 6, 7}, True, False
)

print(tup2[2])
print(tup2[-4]['b'])
print(tup2[3][2])
print(tup2[6:])
print(tup2[2::2])
print(tup2[-1::-2])


########################################## Apply loop on tuple ###################
tup3 = (3, 5, 8, 2, 9)

for val in tup3:
    print(val)


    print("_"*50)

    for i in range(len(tup3)):
        print(i, tup3[i])


        print(dir(tuple))
        tup_a = (3, 6, 3, 7, 3, 8, 3)
        print("count of 3 :", tup_a.count(3))
        print("Index of 8 :",tup_a.index(8))
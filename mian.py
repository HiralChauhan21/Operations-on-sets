my_set = {1,2,2,3,4,4,4}
print("Set : ", my_set)

my_set.add(5)
print("updated set: ", my_set)

set1= my_set
set2= {2,4,4,6}

print("\nSet 1: ", set1)
print("set 2 ", set2)
print("difference: ")
print(set1.difference(set2))
print("symetric difference ")
print(set1.symmetric_difference(set2))
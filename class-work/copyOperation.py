# General copy

# l1 = [1,2,3]
# l2 = l1
# l2[1]= 200
# l1[2]= 200
# print(l1)
# print(l2)


#---------------------------------------------


# Shallow copy

# l1 = [1,2,3]
# l2 = l1.copy()
# l2[1]= 200
# print(l2)
# print(l1)

# l1 = [1,2,3, [4,5,6]]   # but shallow has disadvantage, if there is list in list, then both list (original and new) cell(where another's list address is there) address will be pointing to same value space address
# l2 = l1.copy()
# l2[3][2] = 600
# print(l2)
# print(l1)


#------------------------------------------------


# Deep copy -> Really satisfies the objective of copying

import copy
l1 = [1,2, [3,4]]
l2 = copy.deepcopy(l1)
l2[0] = 100
l2[2][1] = 400
print(l2)
print(l1)
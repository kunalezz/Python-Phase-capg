'''
Simple pattern
***
***
***
'''
# row = int(input("Enter row value: "))
# col = int(input("Enter col value: "))
# for i in range(0, row):
#     for j in range(0, col):
#         print("#", end=" ")
#     print()   


#-------------------------------------------------------------


'''
Primary diagonal -> where i == j
@**
*@*
**@
'''
# n = int(input("Enter a val: "))
# for i in range(0, n):
#     for j in range(0, n):
#         if i == j:
#             print("@", end=" ")
#         else:
#             print("*", end=" ")
#     print()


#-------------------------------------------------------------


'''
Secondary diagonal -> where i+j == no of rows + 1
**@
*@*
@**
'''
# row = int(input("Enter no of row: "))
# col = int(input("Enter no of col: "))
# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if i+j == row+1:
#             print("@", end=" ")
#         else:
#             print("#", end=" ")
#     print()


#-------------------------------------------------------------


'''
Lower triangle -> i>j
Upper triangle -> i<j
'''    
# n = int(input("Enter a val: "))
# for i in range(0, n):
#     for j in range(0, n):
#         if(i>j):
#             print("@", end=" ")
#         elif(i<j):
#             print("#", end=" ")
#         else:
#             print("*", end=" ")
#     print()


#-------------------------------------------------------------


'''
Task 1: 
**#
*#@
#@@
'''
# row = int(input("Enter no of row: "))
# col = int(input("Enter no of col: "))

# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if(i+j > row +1):
#             print("@", end="")
#         elif( i+j < row +1):
#             print("*", end="")    
#         elif(i+j == row+1):
#             print("#", end="")   

#     print()         


#-----------------------------------------------------------


'''
Task 2: 
* #
 # 
# *
'''
# row = int(input("Enter no of row: "))
# col = int(input("Enter no of col: "))

# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if(i+j == row +1):
#             print("#", end="")
#         elif( i == j ):
#             print("*", end="")    
#         else:
#             print(" ", end="")   

#     print()      
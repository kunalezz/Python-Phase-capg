# First 20 even no.

# a = 0
# count = 1
# while a < 100:
#     if a % 2 == 0:
#         print(a)
#         count = count+1
#     a = a+1
#     if count == 20:
#         break

# Reverse a number

# num = int(input("Enter a number"))
# num1 = 0
# while num > 0:
#     lastNo = num%10
#     num1 = (num1*10)+ lastNo
#     num = num // 10
# print(num1)


# Print a table with f in print

# n = int(input("Enter a num"))
# a = 1
# while a < 11:
#     print(f"{n}X{a}={n*a}")
#     a += 1

# To replace space with "_"
name = "Bhavik Sirohiya"
# name.replace(" ","_",1)
# print(name)

new = ""
for i in name:
    if i==" ":
        new += "_"
    new += i
print(new)
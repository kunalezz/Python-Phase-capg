a = int(input("Enter a num"))
if len(str(a)) != 3:
    print(False)
elif a // 100 == 0:
    print(False)
elif (a%100) // 10 == 0:
    print(False)
elif len(str(a)) == 3:
    print(True)        


# b = input("Enter")
# print(len(b) > 5)
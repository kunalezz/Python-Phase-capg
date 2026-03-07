# question 1
# def funAdd(a, b, c=0,d=0):
#     return a+b+c+d

# print(funAdd(5,6,7,8))
# print(funAdd(5,6))

# question 2
def indiSum(x : int):
    y = int(0)
    while x!=0:
        y += x%10
        x = x//10
    
    return y

print(indiSum(int(123)))


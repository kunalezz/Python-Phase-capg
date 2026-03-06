totalAmount = 0
def calcBill(units):
    if units <= 100:
        totalAmount = units*5
    elif units <= 300:
        totalAmount = (100*5)+(units-100)*7
    else:
        totalAmount = (100*5)+(200*7)+(units-300)*10 
    return totalAmount

print(calcBill(200))
           
# int to all

# a = 1
# aStr = str(a) 
# print( type (aStr))
# print(aStr)

# aBool = bool(a)
# print( type (aBool))
# print(aBool)

# aFlo = float(a)
# print( type (aFlo))
# print(aFlo)

# aCom = complex(a)
# print( type (aCom))
# print(aCom)

#------------------------------------------------


# float to all

# b = 1.7

# bInt = int(b)
# print( type (bInt) )
# print(bInt)

# bStr = str(b)
# print( type (bStr) )
# print(bStr)

# bCom = complex(b)
# print( type (bCom) )
# print(bCom)

# bBool = bool(b)
# print( type (bBool) )
# print(bBool)

#--------------------------------

# complex to all ----> But it can't be type casted in int and float

# c = (1+5j)

# cStr = str(c)
# print( type (cStr) )
# print( cStr )

# cBool = bool(c)
# print( type (cBool) )
# print( cBool )


#----------------------------------------

# bool to all

# d = True

# dInt = int(d)
# print( type (dInt) )
# print( dInt )

# dFlo = float(d)
# print( type (dFlo) )
# print( dFlo )

# dCom = complex(d)
# print( type (dCom) )
# print( dCom )

# dStr = str(d)
# print( type (dStr) )
# print( dStr )


#---------------------------------


# String to all -> Can't be converted to any single valued data type (if value is alphabet) except boolean
# Can be converted to all SVDT if value is like "1234" (int)
# And can be converted into any multi valued data type ( List, tuple, set) except to Dictionary

# eAlpha = "namee"

# eBool = bool(eAlpha)
# print( type (eBool) )
# print( eBool )

# eList = list(eAlpha)
# print( type (eList) )
# print( eList )

# eTup = tuple(eAlpha)
# print( type (eTup) )
# print( eTup )

# eSet = set(eAlpha)
# print( type (eSet) )
# print( eSet )

# eNum = "1234"
# eBoolean = "True"


#----------------------------------------------------

# List to all

l = ["hi", [1, 2], "to", ["hi",'hhe']]
lDict = dict(l)
print(lDict)
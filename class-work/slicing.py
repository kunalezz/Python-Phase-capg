# Syntax of slicing -> 
# varName[ start : End +/-1 : step]

a = [10, 2j, "python", [2+5j, 11, 22.2]]
a[1:3:1]

[2j, 'python']
b = [1,2,3,4,5,6,7,8,9]
b[1:6:1]

[2, 3, 4, 5, 6]
b[0:6:2]
[1, 3, 5]

str = "hiii python"
print( str[1::1] )            
print( str[::1] )
print( str[::] )
print( str[::-1] )
print( str[0::-1] )
print( str[2::-1] )
print( str[0::2] )
print( str[-6::] )

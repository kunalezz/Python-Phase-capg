a = [1, 2, 3, 1, 4, 1]

len(a)
id(a)
type(a)

abs(-400)
round(2.4)
round(10.2345, 2)
round(2.5) # Exception - round off to nearest even no.

max(a)
min(a)

sum(a) 

a.index(1, 2)
a.count(1)


ord("a") # for finding ascii value


# Split Function -> Split parts in list format

l = ["P1.py", "first.txt", "T3.py", "TK.txt", "TFK.com"]
dict = {}
for i in l:
    parts = i.split(".")
    print(parts)

    if parts[1] in dict:
        dict[parts[1]].append(parts[0])
    else:
        dict[parts[1]] = [parts[0]]          
print(dict)
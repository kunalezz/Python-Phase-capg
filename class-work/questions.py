# Q1. input = "aaabbaabcc" Output = "a3b2a2b1c2"
# inp = str(input("Enter some STRING: "))
# count = 1
# stri = ""
# for i in range(0, len(inp)-1):
#     if inp[i] != inp[i+1]:
#         stri += (inp[i])
#         stri += str(count)
#         count = 1
#     else:
#         count += 1   
# stri += inp[-1] + str(count)
# print(stri)   

# Q2 All vowels in names list
# inp = ["Krishn", "Ram", "Hanuman"]
# out = ""
# for i in inp:
#     for j in i:
#         if j in "aeiouAEIOU":
#             out += j

# print(out)


# Q3. output = {"Program": "oa", "Python":"o"}
inp = [(2+3j), 12, "Program", "Python", False]
dict = {}
for i in inp:
    st = ""
    if type(i) == str:
        for j in i:
            if j in "aeiouAEIOU":
                st += j
        dict[i] = st
print(dict)

# s = "racecar"
# result = s == s[::-1]
# print(id(s))
# print(id(s[::-1]))
# print(id(s)==id(s[::-1]))

x="Python"
i="P"
while i in x:
    x=x[:-1]
    print(i)
    print(x)
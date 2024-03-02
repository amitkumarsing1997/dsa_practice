l1=[1,5,9,3,2]
def max_find(l1):
 max=0
 for i in l1:
    if i>max:
        max=i
 return max

print(max_find(l1))


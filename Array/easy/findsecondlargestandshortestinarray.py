# l1=[3,5,6,2,1,8]
# l1.sort()
# print(l1[1])
# print(l1[-2])


def second_min_logic(l1):
    min=2**32-1
    min_second = 2**32-1
    for i in l1:
        if i<min:
            min_second=min
            min=i
        elif i<min_second and i!=min:
            min_second=i
    return min_second

def second_large_logic(l1):
    max=-2**32
    max_second=-2**32
    for i in l1:
        if i>max:
            max_second=max
            max=i
        elif i>max_second and i!=max:
            max_second=i
           
    return max_second

l1=[1, 2, 4, 7, 7, 5]
print(second_large_logic(l1))
print(second_min_logic(l1))

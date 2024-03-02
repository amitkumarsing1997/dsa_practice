def reverse(x:int) -> int:
    reverse=0
    max_int = 2**31//10
    min_int = -(2**31)//10
    while x!=0:
     rem = x % 10
     if (reverse > max_int or reverse < min_int):
        return 0
    reverse = reverse*10 + rem
    x=x//10
    return reverse

# def reverse(x:int)->int:
#    reverse=0
#    max_int = 2**31//10
#    min_int = -(2**31)//10
#    print(max_int)
#    print(min_int)
#    while x!=0:
#       rem = x % 10
#       reverse = reverse *10 + rem
#       x = x // 10
#    return reverse

# print(reverse(-123))


# def reverse(x):
#     answer = 0

#     while x != 0:
#         digit = x % 10
#         if answer > 2**31 // 10 or answer < -(2**31) // 10:
#             return 0

#         answer = answer * 10 + digit
#         x = x // 10

#     return answer

# # Example usage
# result = reverse(-123)
# print(result)




# This answer is useful
# 3

# def reve(x):
#     x=str(x)
#     if x[0]=='-':
#         a=x[::-1]
#         return f"{x[0]}{a[:-1]}"
#     else:
#         return type(int(x[::-1]))

# # print(reve("abc"))
# # print(reve(123))
# print(reve(-123))




def reverse(x:int) -> int:
    reverse=0
    max_int = 2**31
    min_int = -(2**31)
    print(max_int)
    print(min_int)
    x=str(x)
    if(x[0]=="-"):
        a=x[::-1]
        reverse =int(f"{x[0]}{a[:-1]}")
    else:
        reverse = int(x[::-1])
        if (reverse > max_int or reverse < min_int):
            return 0 
    return reverse

print(reverse(-2147483412))

# print(reverse(-2142))


    

    
# ans = float('inf')
# print(ans)

# #
# ans = int('inf')
# print(ans)


# ------
# arr = [1, 6, 11, 5]
# print(sum(arr))


# -----
# input
# arr = [1, 1, 2, 3]
# diff = 1

arr = [1, 1, 2, 3]
diff = 2


"""some logic"""
# value = (diff + sum(arr)) / 2
# print(value)
# # if the result is a float, set the value to 0, otherwise convert to int
# value = 0 if isinstance(value, float) else int(value)
#
# print(value)

# Assuming 'diff' and 'arr' are already defined
result = (diff + sum(arr)) / 2
print(result)
# Check if the result is a whole number (i.e., has no decimal part)
value = int(result) if result.is_integer() else 0

print(value)


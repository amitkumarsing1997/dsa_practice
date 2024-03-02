
# # #  APPROACH -1 (BRUTE APPROACH)
# # Step 1: Copy the first d elements into temp array


# def solve(arr, n, d):
#     if n == 0:
#      return
#     d = d % n
#     if(d > n):
#         return
#     temp = [0] * n
#     # Step-1: Copy the first d elements into temp array

#     for i in range(0,d):
#         temp[i]=arr[i]

#     # Step-2 : Shift from d to last element to the left
#     for i in range(d,n):
#         arr[i-d] = arr[i]

#     # Step-3: Copy the elements into the main array from the temp array
        
#     for i in range(n-d, n):
#        arr[i] = temp[i-(n-d)]
#     return arr
        
#         # OR

#     # j=0
#     # for i in range(n-d,n):
#     #     arr[i] = temp[j]
#     #     j = j + 1
#     # return arr

# n = 5
# arr = [1, 2, 3, 4, 5]
# d=3
# print(solve(arr, n, d))



## APPROACH - 2  Using ” Reversal Algorithm “

def reverse(arr, start, end):
    while (start <= end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start + 1
        end = end - 1

def solve(arr, n, d):
    if n==0:
        return 
    d = d % n
    if (d > n):
        return
    
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)

    return arr

n = 5
arr = [1, 2, 3, 4, 5]
d=3
print(solve(arr, n, d))







   
    # if 
    # for i in range(n-1):
    #     arr[i] = arr[i+1]
    # arr[n-1] = temp
    # for i in range(n):
    #     print(arr[i], end=" ")
    # print()


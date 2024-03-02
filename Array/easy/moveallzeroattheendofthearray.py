## First approach - brute force approach (amit)
# def moveAllzero(arr):
#     # Temporary array
#     temp = []

#     # Copy non-zero elements from original to temp array
#     for i in range(0, n):
#         if arr[i] != 0:
#             temp.append(arr[i])
#     for i in range(0,n):
#          # Copy elements from temp to fill first nz fields of original array
#         if i < len(temp):
#          arr[i] = temp[i]
#            # Fill the rest of the cells with 0
#         else:
#            arr[i] = 0

#     return arr








# arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
# n = len(arr)

# print(moveAllzero(arr))



## First approach - brute force approach (striver)
# def moveAllzero(arr):
#     # Temporary array
#     temp = []

#     # Copy non-zero elements from original to temp array
#     for i in range(0, n):
#         if arr[i] != 0:
#             temp.append(arr[i])
#     temp_len = len(temp)
#     for i in range(0,temp_len):
#          # Copy elements from temp to fill first nz fields of original array
#         arr[i] = temp[i]
#            # Fill the rest of the cells with 0
#     for i in range(temp_len,n):
#         arr[i] = 0

#     return arr







# arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
# n = len(arr)

# print(moveAllzero(arr))

# Complexity Analysis
# Time Complexity: O(N) + O(X) + O(N-X) ~ O(2*N), where N = total no. of elements,
# X = no. of non-zero elements, and N-X = total no. of zeros.
# Reason: O(N) for copying non-zero elements from the original to the temporary array. O(X) for again copying it back from the temporary to the original array. O(N-X) for filling zeros in the original array. So, the total time complexity will be O(2*N).

# Space Complexity: O(N), as we are using a temporary array to solve this problem and the maximum size of the array can be N in the worst case.
# Reason: The temporary array stores the non-zero elements. In the worst case, all the given array elements will be non-zero.











## Second approach - optimal approach -> using 2 pointers


 # swaping logic 
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def moveAllzero(n, arr):
    j = -1

    # place the pointer j
    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    # No non-zero elements
    if j == -1:
        return arr
    
    # Move the pointers i and j and swap accordingly
    for i in range(j+1, n):
        if arr[i] != 0:
            swap(arr, i, j)
            # arr[i], arr[j] = arr[j], arr[i]
            j+=1
    return arr
    


arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = len(arr)

print(moveAllzero(n, arr))




# Complexity Analysis
# Time Complexity: O(N), N = size of the array.
# Reason: We have used 2 loops and using those loops, we are basically traversing the array once.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.
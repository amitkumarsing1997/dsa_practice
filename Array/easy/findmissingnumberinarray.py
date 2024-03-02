# #(1) brute force approach
# def find_missing_number(arr,N):
#     #  Outer loop that runs from 1 to N:
#     for i in range(1,N+1):
#         # flag variable to check if an element exists
#         flag = 0
#         # Search the element using linear search:
#         for j in arr:
#             if i==j:
#                 # i is present in the array:
#                 flag=1
#                 break
#         # check if the element is missing (i.e., flag == 0):
#         if flag==0:
#          return i
#     return -1



# N=5
# arr=[1,2,4,5]
# print(find_missing_number(arr,N))


# Complexity Analysis
# Time Complexity: O(N2), where N = size of the array+1.
# Reason: In the worst case i.e. if the missing number is N itself, the outer loop will run for N times, and for every single number the inner loop will also run for approximately N times. So, the total time complexity will be O(N2).

# Space Complexity: O(1)  as we are not using any extra space.






# # (2) Better Approach(using Hashing)  Algorithm (Intuition)

# def find_missing_number(arr,N):
#    hash = [0] * (N+1)
# # storing the frequencies
#    for i in arr:
#       hash[i] += 1
# # checking the frequencies for numbers 1 to N
#    for i in range(1,N+1):
#       if hash[i] == 0:
#          return i
#    return -1

# N=5
# arr=[1,2,4,5]
# print(find_missing_number(arr,N))

# Time Complexity: O(N) + O(N) ~ O(2*N),  where N = size of the array+1.
# Reason: For storing the frequencies in the hash array, the program takes O(N) time complexity and for checking the frequencies in the second step again O(N) is required. So, the total time complexity is O(N) + O(N).

# Space Complexity: O(N), where N = size of the array+1. Here we are using an extra hash array of size N+1.





# # (3) optimal approach 1

# def find_missing_number(arr,N):
#     # summation of first N numbers:
#     summation = (N*(N+1)) // 2

#     # Summation of all array elements:
#     s2 = sum(arr)
#     missingNum = summation - s2
#     return missingNum

# N=5
# arr=[1,2,4,5]
# print(find_missing_number(arr,N))

# # Time Complexity: O(N), where N = size of array+1.
# # Reason: Here, we need only 1 loop to get the sum of the array elements. The loop runs for approx. N times. So, the time complexity is O(N).

# # Space Complexity: O(1) as we are not using any extra space.








# (4) optimal approach 2 (XOR Approach)

# Now, let’s XOR all the numbers between 1 to N.
# xor1 = 1^2^…….^N

# Let’s XOR all the numbers in the given array.
# xor2 = 1^2^……^N (contains all the numbers except the missing one).

# Now, if we again perform XOR between xor1 and xor2, we will get:
# xor1 ^ xor2 = (1^1)^(2^2)^……..^(missing Number)^…..^(N^N)

# Here all the numbers except the missing number will form a pair and each pair will result in 0 according to the XOR property. The result will be = 0 ^ (missing number) = missing number (according to property 2).

# So, if we perform the XOR of the numbers 1 to N with the XOR of the array elements, we will be left with the missing number.




def find_missing_number(arr,N):
   xor1 = 0
   xor2 = 0
   for i in range(N-1):
      xor1 = xor1 ^ (i+1)    # XOR up to [1......N-1] 
      xor2 = xor2 ^ arr[i]     # XOR of array elements
   xor1 = xor1 ^ N           # XOR up to [1....N]
   return xor1 ^ xor2        # the missing number

N=5
arr=[1,2,4,5]
print(find_missing_number(arr,N))



# Complexity Analysis
# Time Complexity: O(N), where N = size of array+1.
# Reason: Here, we need only 1 loop to calculate the XOR. The loop runs for approx. N times. So, the time complexity is O(N).

# Space Complexity: O(1) as we are not using any extra space.



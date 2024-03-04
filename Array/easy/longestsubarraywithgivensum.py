# # approach 1) brute force approach




# def getlongestSubarray(arr, n, k):
#     leng=0
    
#     # for starting index of subarray
#     for i in range(0, n):
#         # for ending index of subarray
#         for j in range(i, n):
#             sum=0
#             for m in range(i,j+1):
#                 sum=sum+arr[m]
#             if sum == k:
#                 leng = max(leng, j - i + 1)
#     return leng

# # Test cases
# arr = [10, 12, 13]
# arr = [2,3,5,1,9]
# n = len(arr)
# k = 10
# print(getlongestSubarray(arr, n, k))  # Output: 1

# Complexity Analysis
# Time Complexity: O(N3) approx., where N = size of the array.
# Reason: We are using three nested loops, each running approximately N times.

# Space Complexity: O(1) as we are not using any extra space.




# approach-2 (Optimize above approach by two loops)


# def getlongestSubarray(arr,n,k):
    
#     length = 0
#     # start of the index
#     for i in range(0,n):
#         sum=0
#         # end of the index
#         for j in range(i,n):
#             sum = sum + arr[j]
#             if sum == k:
#                 length = max(length,j-i+1)
#     return length


# # Test cases
# # arr = [10, 12, 13]
# arr = [2,3,5,1,9]
# n = len(arr)
# k = 10
# print(getlongestSubarray(arr, n, k)) 


# Time Complexity: O(N2) approx., where N = size of the array.
# Reason: We are using two nested loops, each running approximately N times.

# Space Complexity: O(1) as we are not using any extra space.




# # approach-3 (Using Hashing)

# def getLongestSubarray(arr,k):
#     n = len(arr)
#     preSumMap = {}
#     maxLen = 0
#     sum = 0

#     for i in range(n):
#         # calculate the prefix sum till index i
#         sum = sum +arr[i]

#         if sum == k:
#             maxLen = max(maxLen, i+1)

#         #  calculate the sum of remaining part ex x-k
#         rem = sum - k

#         # calculate the length and update maxLen

#         if rem in preSumMap:
#             length = i - preSumMap[rem]
#             maxLen = max(maxLen,length)

#         # Finally update the map checking the conditions
#         if sum not in preSumMap:
#             preSumMap[sum] = i
#     return maxLen

# arr = [2, 3, 5, 1, 9]
# k = 10

# print(getLongestSubarray(arr,k))


# Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.
# Reason: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N)(though in the worst case, unordered_map takes O(N) to find an element and the time complexity becomes O(N2)) but if we are using a map data structure, the time complexity will be O(N*logN). The least complexity will be O(N) as we are using a loop to traverse the array.

# Space Complexity: O(N) as we are using a map data structure.


 
# approach -4 (two pointer approach)

def getLongestSubarray(a, k) -> int:
    n = len(a) # size of the array.

    left, right = 0, 0 # 2 pointers
    Sum = a[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < n: 
            Sum += a[right]

    return maxLen


if __name__ == "__main__":
	a = [2, 3, 5, 1, 9]
	k = 10

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")


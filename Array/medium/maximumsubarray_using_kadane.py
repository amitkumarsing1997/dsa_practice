# def maxSubArray(nums):
#         n = len(nums)
#         max = nums[0]
#         for i in range(0,n):
#             sum = 0
#             for j in range(i,n):
#                 sum=sum+nums[j]
#                 if sum>max:
#                     max=sum
#         return max

# nums = [5,4,-1,7,8]
# print(maxSubArray(nums))

# Time Complexity: O(N2), where N = size of the array.
# Reason: We are using two nested loops, each running approximately N times.

# Space Complexity: O(1) as we are not using any extra space.




# 2) -> optimal approach by using kadane algorithms

# import sys
# def maxSubarraySum(arr,n):
#     maxi = -sys.maxsize-1
#     sum = 0 
#     for i in range(n):
#         sum += arr[i]
#         if sum > maxi:
#             maxi = sum

#         if sum < 0:
#             sum = 0
#     return maxi

# arr = [-2,1-3,4,-1,2,1,-5,4]
# n = len(arr)
# maxSum = maxSubarraySum(arr,n)
# print("The maximum subarray is : ",maxSum)

# time complexity is O(n)
# space complexity is O(1)


import sys
def maxSubarraySum(arr,n):
    maxi = -sys.maxsize-1
    sum = 0 
    ans_start = -1
    ans_end = -1
    for i in range(n):
        if (sum==0):
            ans_start = i
        sum += arr[i]
        if sum > maxi:
            maxi = sum
            ans_end = i

        if sum < 0:
            sum = 0
    for m in range(ans_start,ans_end+1):
        print(arr[m]," ")
    # return maxi,ans_end,ans_start

arr = [-2,1-3,4,-1,2,1,-5,4]
n = len(arr)
maxSubarraySum(arr,n)
# maxSum = maxSubarraySum(arr,n)
# print("The maximum subarray is : ",maxSum)


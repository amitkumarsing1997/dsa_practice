# def majorityElement(nums):
#     n = len(nums)
#     m = {}
#     for num in nums:
#         if num not in m:
#             m[num] = 1
#         else:
#             m[num] += 1
#     n = n // 2
#     for key, value in m.items():
#         if value > n:
#             return key
#     return 0

# nums = [2,2,1,1,3,3,1,2,2,3,3,3,3]
# print(majorityElement(nums))





# #  amit code
def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_dict={}
        for num in nums:
            if num in temp_dict:
                temp_dict[num]+=1
            else:
                temp_dict[num]=1
        maxi=0
        maxi_val=0
        for k,v in temp_dict.items():
            if v>maxi:
                maxi=v
                maxi_val=k
        return maxi_val

# nums = [2,2,1,1,1,2,2]
nums = [2,2,2,2,1,1,3,3,1,2,2,3,3,3,3,3]
print(majorityElement(nums))
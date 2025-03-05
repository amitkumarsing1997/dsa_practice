# input: nums=[1,1,1,2,2,3]
# output 5, nums = [1,1,2,2,3]

# input: nums = [0,0,1,1,1,1,2,3,3]
# output 7 , nums = [0,0,1,1,2,3,3]


def output(temp_list):
    temp_dict = {}
    for i in temp_list:
        temp_dict[i] = temp_dict.get(i,0)+1
    # return temp_dict
    threshold = 2
    breaching_count = 0
    for values in temp_dict.values():
        if values > threshold:
            breaching_count += (values-threshold)
    return len(temp_list)-breaching_count
  

# nums=[1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]

print(output(nums))






# second approach
from collections import Counter
def output(temp_list):
    num_counter = Counter(temp_list)
   
    threshold = 2
    breaching_count = 0
    for values in num_counter.values():
        if values > threshold:
            breaching_count += (values-threshold)
    return len(temp_list)-breaching_count
# nums=[1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]

print(output(nums))






# print(round(45.8))
# print(round(6352.898,2,5))
# print(round(7463.123,2,1))


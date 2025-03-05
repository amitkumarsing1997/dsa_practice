
# def count_letter(s):
#     temp_dict = {}

#     for i in s:
#         if i in temp_dict:
#             temp_dict[i]+=1
#         else:
#             temp_dict[i]=1
    
#     # for k in temp_dict.values():
#     # for k in temp_dict.keys():
#     for k,v in temp_dict.items():
#         print(k," ",v)


# s="amit kumar singh"
# count_letter(s)




def find_occurence_index(haystack,needle):
    #  make sure we don,t
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
        
    
haystack = "leetcode"
needle = "code" 
print(find_occurence_index(haystack,needle))

    # def strStr(self, haystack, needle):
    #     # makes sure we don't iterate through a substring that is shorter than needle
    #     for i in range(len(haystack) - len(needle) + 1):
    #         # check if any substring of haystack with the same length as needle is equal to needle
    #         if haystack[i : i+len(needle)] == needle:
    #             # if yes, we return the first index of that substring
    #             return i
    #     # if we exit the loop, return -1        
    #     return -1
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# def word_length(s):
#     length = len(s)
#     tem_str=""

#     # print(length)
#     count=0
#     for i in s:
#         if i != " ":
#             count=count+1
#         else:
#             break
        
#     # print(count)
#     print(length-count-1)


def word_length(s):
    length = len(s)
    tem_str=""
    temp_list=[]
    # print(length)
    # count=0
    for i in s:
        if i != " ":
            tem_str=tem_str+i
        else:
            temp_list.append(tem_str)
            

    list_length = len(temp_list)
    final_length = len(temp_list[list_length-1])-len(temp_list[list_length-2])
    print("final_length =",final_length)
    print(temp_list)

s = "Hello Amit kumarsin "
word_length(s)

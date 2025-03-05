# approach-1

# def reverse_word_in_string(s):
#     s2=s.split(" ")
#     s2.reverse()
#     fin = ""
#     for st in s2:
#         if st=="":
#             pass
#         else:
#          fin=fin+st+" "
#     return fin.strip()
        
#     # s3 = " ".join(s2)
#     # return s3

# print(reverse_word_in_string("the sky is blue"))
# # print(reverse_word_in_string("a good   example"))

# # example good a


# # approach 2
# # very important to understansd this
# def reverseWords(s: str):
    
#     list1 = []
#     str1 = ""
#     # Append a space at the end to ensure the last word is captured
#     s += " "
#     length = len(s)

#     for i in range(length):
#         if s[i] != " ":
#             str1 += s[i]
#         elif str1:
#             list1.append(str1)
#             str1 = ""


#     final_str=""
#     length2 = len(list1)
#     for j in range(0,length2):
#         final_str = final_str+list1[length2-j-1]+" "
#     return final_str.strip()
# print(reverseWords("the sky is blue"))




# approach-3

def reverse_word_in_string(s):
    s2=s.split(" ")
    # s2= s2.reverse()
    s2 = s2[::-1]
    return " ".join(s2)
print(reverse_word_in_string("the sky is blue"))




                        
                        
                        
                    
                    
                        
                
        # for st in s:
        #     if st==" " :
        #         str1 = str1+st 
        #     # elif (st==" "):
        #     #     list1.append(str1)
        #     #     str1=""
        #     else:
        #         list1.append(str1)
        #         str1=""
                 
        # # return "".join(list1)
        # return list1



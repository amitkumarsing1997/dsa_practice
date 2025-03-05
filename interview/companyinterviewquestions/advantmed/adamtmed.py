

def reverse_string(str1):
   string_length = len(str1)
   temp_str = ""

#    for i in range(0,string_length):
#       temp_str = temp_str+str1[string_length-i-1]
#    return temp_str
   i=0
   while(i<string_length):
      temp_str = temp_str+str1[string_length-i-1]
      i += 1
   
   return temp_str
    


# #    return temp_str
#     #   temp_str+str1[string_length-i-1]
#     #   print(str1[string_length-i-1])
# #    

     
     


#     # list1 = str1.strip()
#     # return list1[::-1]



str1 = "amit"
# reverse_string(str1)
print(reverse_string(str1))



# def factorial_num(num):
#     fact = 1
#     if num==0:
#         return 1
#     for i in range(1,num+1):
#         fact = fact * i
#     return  fact

# num = 5
# print(factorial_num(num))


# import pandas as pd
# data = pd.read_excel("C:\\Users\\sumit\\OneDrive\\desktop\\advantmed_data.xlsx")
# print(data)

# def temp_fun(respone):
#     if respone=="yes":
#         return 1
#     else:
#         return 0
    
# data["temp_ans"] = data["response"].apply(lambda x:temp_fun(x))
# print(data) 

# def temp_remove_unser_score(random):
#     ans=""
#     temp = random.split("_")
#     for data in temp:
#         ans=ans+data
#     return ans

# data["random"] = data["random"].apply(lambda x:temp_remove_unser_score(x))
# print(data) 

    




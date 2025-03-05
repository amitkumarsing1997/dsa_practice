
# # brute force approach

# def sliding_window(arr1,n,len1):
#     temp_dict = {}
#     for i in range(0,len1-n+1):
#         sum=0

#         temp_str=""
#         for j in range(0,n):
#             sum = sum+arr1[i+j]
#             temp_str = temp_str+" "+str(arr1[i+j])
#         temp_dict[temp_str] = sum
            
            
#         # sum=sum+arr1[i]+arr1[i+1]+arr1[i+2]
#         # temp_str = temp_str + str(arr1[i])+" "+ str(arr1[i+1])+" "+str(arr1[i+2])
#         # temp_dict[temp_str] = sum

#     max = -1
#     temp_max=""
#     for k,v in temp_dict.items():
#         if v>max:
#             max=v
#             temp_max=k
#     print(temp_max," ",max)
            

    
#     return temp_dict

# A = [1, 3, -1, -3, 5, 3, 6, 7,1,13,-1]
# # A = [1, 3,-1, 4,5,8,6]
# n = 3
# len1 = len(A)
# sliding_window(A,n,len1)








def sliding_window(A,size,k):
    i=0
    j=0
    sum=0
    max_sum = -2**31
    while(j < size):
        windowsize = j-i+1
        sum=sum+A[j]
        if(windowsize < k):
            j += 1
        elif(windowsize==k):
            max_sum = max(max_sum,sum)
            sum = sum - A[i]
            i += 1
            j += 1
    return max_sum




A = [1, 3, -1, -3, 5, 3, 6, 7,1,13,-1]
size = len(A)
k=3
var = sliding_window(A,size,k)
print(var)







def sliding_window(A,size,k):
    i=0
    j=0
    sum=0
    start_index=-1
    end_endex=-1
    max_sum = -2**31
    while(j < size):
        windowsize = j-i+1
        sum=sum+A[j]
        if(windowsize < k):
            j += 1
        elif(windowsize==k):
            # max_sum = max(max_sum,sum)
            if sum > max_sum:
                max_sum=sum
                start_index = i
                end_endex = j
            sum = sum - A[i]
            i += 1
            j+=1
    return max_sum,start_index,end_endex




A = [1, 3, -1, -3, 5, 3, 6, 7,1,13,-1]
size = len(A)
k=3
var = sliding_window(A,size,k)
print(var)
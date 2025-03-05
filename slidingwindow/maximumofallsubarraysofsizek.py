
# brute force approach
# def sliding_window(arr,k):
#     ans = []
#     size = len(arr)
#     for i in range(0,size-k+1):
#         maxi = -2**31
#         for j in range(i,i+k):
#             if arr[j]>maxi:
#                 maxi=arr[j]
#         ans.append(maxi)
#     return ans

# arr = [1,3,-1,-3,5,3,6,7]
# k=3
# print(sliding_window(arr,k))






def sliding_window(arr,k):
    if k==1:
        return arr
    max_vals = []
    ans = []
    size = len(arr)
    i=j=0
    while(j<size):
        windowsize = j-i+1
        # calculation

        if len(max_vals) == 0:
            max_vals.append(arr[j])
        else:
            while len(max_vals)!=0 and max_vals[-1]<arr[j]:
                max_vals.pop(-1)
            max_vals.append(arr[j])

        if windowsize < k:
            j+=1
        elif (windowsize == k):
            ans.append(max_vals[0])
            if arr[i] == max_vals[0]:
                max_vals.pop(0)
            i+=1
            j+=1
    return ans

# arr = [1,3,-1,-3,5,3,6,7]
# k=3
arr = [7,2,4]
k=2
print(sliding_window(arr,k))








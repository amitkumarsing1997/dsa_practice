
def first_negative_number(arr,size,k):
    i=0
    j=0
    # to store -ve numbers
    lis = []
    # count of windows
    window_count = 0
    # store the negative value with the window numbers
    temp_dict = {}
    while(j<size):
        windowsize = j-i+1
        # calculation
        if(arr[j]<0):
            lis.append(arr[j])
        if(windowsize < k):
            j += 1  
        elif (windowsize == k):
         
        #  calculation
         window_count += 1
         if (lis):
            temp_dict[window_count] = lis[0]
         else:
            temp_dict[window_count] = 0
         if (arr[i] in lis):
          lis.pop(0)
         i+=1
         j+=1
    return temp_dict
    

arr = [12,-1,-7,8,-15,30,16,28]
size = len(arr)
k = 3
print(first_negative_number(arr,size,k))

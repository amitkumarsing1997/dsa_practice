
def sliding_window(arr1,n,len1):
    temp_dict = {}
    for i in range(0,len1-n+1):
        sum=0

        temp_str=""
        for j in range(0,n):
            sum = sum+arr1[i+j]
            temp_str = temp_str+" "+str(arr1[i+j])
        temp_dict[temp_str] = sum
            
            
        # sum=sum+arr1[i]+arr1[i+1]+arr1[i+2]
        # temp_str = temp_str + str(arr1[i])+" "+ str(arr1[i+1])+" "+str(arr1[i+2])
        # temp_dict[temp_str] = sum



    max = -1
    temp_max=""
    for k,v in temp_dict.items():
        if v>max:
            max=v
            temp_max=k
    print(temp_max," ",max)
            

    
    return temp_dict

A = [1, 3, -1, -3, 5, 3, 6, 7,1,13,-1]
# A = [1, 3,-1, 4,5,8,6]
n = 3
len1 = len(A)
sliding_window(A,n,len1)
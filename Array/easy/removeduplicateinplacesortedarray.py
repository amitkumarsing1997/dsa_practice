
# very important by two pointer approach
arr=[1,1,2,2,2,3,3]
arr2=[]
def remove_duplicate(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return i+1



      


for j in range(remove_duplicate(arr)):
    print(arr[j])

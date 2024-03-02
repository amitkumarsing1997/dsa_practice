# Input: arr[1,1,1,2,2,3,3,3,3,4,4]

# Output: arr[1,2,3,4,_,_,_,_,_,_,_]





#  by using two pointer approach 
# optimal approach O(n)
from typing import List

def removeDuplicates(arr: List[int]) -> int:
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = removeDuplicates(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k+1):
        print(arr[i], end=" ")
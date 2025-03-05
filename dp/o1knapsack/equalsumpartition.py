""""
----------Equal sum partition if it is possible than return true or false-------
arr = [1,5,11,5]

so our job is to find out whether in above array is it possible that equal sum partition is possible or not

--> how to solve
we do sum of array
sum = 1 + 5 + 11 + 5 = 22 means 22 is even means it is possible but if it is odd than it never possible to get
equal sum partition in odd
"""


def equalsumpartition(arr):
    n = len(arr)
    sum = 0
    for i in range(0, n):
        sum = sum + arr[i]
    if (sum % 2 != 0):
        return False
    else:
        return subsetsum(arr, int(sum/2))


def subsetsum(arr, sum):
    n = len(arr)
    # t[n+1][w+1]
    t = [[-1] * (sum + 1) for i in range(0, n + 1)]
    for i in range(0, n + 1):
        for j in range(0, sum + 1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i-1] <= j:
                t[i][j] = t[i - 1][j - arr[i-1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
    return t[n][sum]

arr = [1, 5, 11, 5]  # sum= 22
# arr = [1, 5, 11, 9] # sum = 26
# arr = [1, 5, 11, 6]   # sum = 23
print(equalsumpartition(arr))


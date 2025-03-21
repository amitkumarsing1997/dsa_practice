"""
arr = [2,3,5,6,8,10]
sum = 10
ans = {2,8} , {5,2,3} , {10}
final ans = 3

"""

def countofsubsetsum(arr, sum):
    n = len(arr)
    # t = [ [-1] * (sum + 1) for i in range(0, n+1)]
    t = [[0 for _ in range(sum + 1)] for _ in range(n + 1)]
    for i in range(0, n + 1):
        for j in range(0, sum + 1):
            if i == 0:
                t[i][j] = 0
            if j == 0:
                t[i][j] = 1
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][sum]


arr = [2, 3, 5, 6, 8, 10]
sum = 10
print(countofsubsetsum(arr, sum))

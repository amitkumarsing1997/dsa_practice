"""
TYPE -> --------subset sum problem-------

arr [] = 2,3,7,8,10
sum = 11

Find out that is subset possible of arr to produce sum 11 YES/No or True/False
"""


# top down approach


def knapsack(n,sum,arr):
    # t[n+1][w+1]
    t = [[-1] * (sum + 1) for i in range(n + 1)]
    print(t)
    for i in range(0, n + 1):
        for j in range(0, sum + 1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i - 1][j]
    return t[n][sum]


# n=4
# w=7
# wt = [1,3,4,5]
# val=[1,4,5,7]

# n = 3
# w= 4
# val=[1, 2, 3]
# wt= [4, 5, 1]


n = 3
sum = 5
arr = [2, 3, 7]

print(knapsack(n,sum,arr))

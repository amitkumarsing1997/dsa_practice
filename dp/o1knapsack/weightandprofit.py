# Input: N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
# Output: 3
# Explanation: There are two items which have weight less than or equal to 4. If we select the item with weight 4, the possible profit is 1. And if we select the item with weight 1, the possible profit is 3. So the maximum possible profit is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.

# Input: N = 3, W = 3, profit[] = {1, 2, 3}, weight[] = {4, 5, 6}
# Output: 0



# # by using recursion approach
# def knapsack(wt,val,w,n):
#     if (n==0) | (w == 0):
#         return 0
#     if (wt[n-1] <= w):
#         return max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1),
#                    knapsack(wt,val,w,n-1))
#     elif (wt[n-1]>w):
#         return knapsack(wt,val,w,n-1)

# # n=3
# # w=3
# # wt = [4,5,6]
# # val=[1,2,3]

    
# n=4
# w=7
# wt = [1,3,4,5]
# val=[1,4,5,7]


# print(knapsack(wt,val,w,n))











# # by using memoization approach

# def knapsack(wt,val,w,n):
#     # t[n+1][w+1] all value should be initialized with -1
#     t = [[-1] * (w+1) for i in range(n+1)]
    
#     if (n==0 or w ==0 ):
#         return 0
#     if (t[n][w] != -1):
#         return t[n][w]
#     if (wt[n-1] <= w):
#         t[n][w] = max(val[n-1] + knapsack(wt,val,w-wt[n-1],n-1),knapsack(wt,val,w,n-1))
#         return t[n][w]
#     elif(wt[n-1] > w):
#         t[n][w] = knapsack(wt,val,w,n-1)
#         return t[n][w]


# n=4
# w=7
# wt = [1,3,4,5]
# val = [1,4,5,7]
# print(knapsack(wt,val,w,n))

# n = 3
# w= 4
# val=[1, 2, 3]
# wt= [4, 5, 1]

# n= 3
# w = 3
# val=[1, 2, 3]
# wt=[4, 5, 6]
# print(knapsack(wt,val,w,n))











# top down approach


def knapsack(wt,val,w,n):
    # t[n+1][w+1]
    t = [[-1] * (w+1) for i in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,w+1):
            if (i==0 or j == 0):
                t[i][j]=0
    
    for i in range(1,n+1):
        for j in range(1,w+1):
            if (wt[i-1] <= j):
                t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]],
                              t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[i][j]

# n=4
# w=7
# wt = [1,3,4,5]
# val=[1,4,5,7]

# n = 3
# w= 4
# val=[1, 2, 3]
# wt= [4, 5, 1]


n= 3
w = 3
val=[1, 2, 3]
wt=[4, 5, 6]
print(knapsack(wt,val,w,n))



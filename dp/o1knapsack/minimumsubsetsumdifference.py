"""Im concenpt


Ex - 1
arr = [1,6,11,5]
(1)-> {1,6} {11,5} = 7 - 16 = 9
(2) -> {1+6+5},{11} = 12 - 11 = 1
(3) -> {11,6}, {1,5} = 17 - 6 = 11
(4) -. {1,6,11,5},{} = 23 - 0 = 23
so in above minimum is 1

Ex - 2
arr = [1,2,7]
(1) -> {1},{2,7} = 1 -9 = 8
(2) -> {1,2},{7} = 3- 7 = 4
(3) -> {1,7},{2} = 8 - 2 = 6
(4) -> {1,2,7},{} = 10 -0 = 10
"""


def minimumsubsetsumdifference(arr):
    total_sum = sum(arr)
    n = len(arr)
    t = [[0 for _ in range(total_sum + 1)] for _ in range(n + 1)]
    # t = [[-1] * (total_sum + 1) for i in range(0, n + 1)]

    for i in range(0, n + 1):
        for j in range(0, total_sum + 1):
            if i == 0:
                t[i][j] = 0
            if j == 0:
                t[i][j] = 1

    for i in range(1, n + 1):
        for j in range(1, total_sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
    # return t[n][total_sum]


    # initialize the answer with a large value
    ans = float('inf')
    # iterate through the last row to find the minimum subset sum difference
    for j in range(total_sum + 1):
        if t[n][j] == 1:
            ans = min(ans, abs(total_sum - 2 * j))
    return ans


# arr = [1, 6, 11, 5]
arr = [1, 2, 7]
print(minimumsubsetsumdifference(arr))

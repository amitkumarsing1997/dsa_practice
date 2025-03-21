""""


arr = [1,1,2,3]
diff = 1
S1-S2 = diff
(1) -> {1,3},{1,2} = S1-S2 = 4 - 3 = 1
(2) -> {1,3},{1,2} = S1-S2 = 4 - 3 = 1
(3) -> {1,1,2},{3} = S1-S2 = 4 - 3 = 1

ans = 1

logic
sum(S1) - sum(S2) = diff
sum(S1) + sum(S2) = sum(all)

-----------------------------------
2 sum(S1) = diff + sum(all)

value = sum(s1) = (diff + sum(all))/2

code logic
subsetsum(arr, sum(s1))

"""


def countthenumberofsubsetwithagivendiff(arr, value):
    if value == 0:
        return 0
    n = len(arr)
    t = [[0 for _ in range(value + 1)] for _ in range(n + 1)]
    # t = [[0] * (value + 1) for i in range(0, n + 1)]
    for i in range(0, n + 1):
        for j in range(0, value + 1):
            if i == 0:
                t[i][j] = 0
            if j == 0:
                t[i][j] = 1

    for i in range(1, n + 1):
        for j in range(1, value + 1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][value]


# input
# arr = [1, 1, 2, 3]
# diff = 1

# arr = [1, 1, 2, 3]
# diff = 2

# arr = [1, 1, 2, 4]
# diff = 0


arr = [3, 1, 2, 4]
diff = 2


"""some logic"""
value = (diff + sum(arr)) / 2

value = int(value) if value.is_integer() else 0

print(countthenumberofsubsetwithagivendiff(arr,value))

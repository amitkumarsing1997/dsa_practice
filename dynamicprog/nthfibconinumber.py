
# # using top down approach (memoization)
# def f(n, dp):
#     if n <= 2:
#         return 1
    
#     if dp[n] != -1:
#         return dp[n]
#     dp[n] = f(n-1, dp) + f(n-2, dp)
#     return dp[n]

# if __name__ == "__main__":
#     n = 6
#     dp = [-1] * (n+1)
#     print(f(n, dp))







# using bottom up approach( tabulation)
    


# def main():
#     n = 6
#     dp = [-1]*(n+1)

#     dp[1] = 1
#     dp[2] = 1

#     for i in range(3, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
    
#     print(dp[n])

# if __name__ == "__main__":
#     main()



#  space optimization
def main():
    n=6
    prev2=1
    prev=1
    for i in range(3,n+1):
        cur=prev + prev2
        prev2=prev
        prev=cur
    print(prev)

if __name__ == "__main__":
    main()


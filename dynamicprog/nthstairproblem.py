# def climbStairs(n: int) -> int:
#     prev=1
#     prev2=1
#     for i in (2,n+1):
#         cur_i = prev + prev2
#         prev2=prev
#         prev=cur_i
#     return prev

# print(climbStairs(2))


# #  by using recurssion

# class Solution:
#  def climbStairs(self,n):
#     df = [-1] * (n+1)
#     def callstair(df,n):
#         if n<=1:
#             return 1
#         if df[n] != -1:
#             return df[n]
#         df[n]=callstair(df,n-1) + callstair(df,n-2)
#         return df[n]
#     return callstair(df,n)

# # Example usage:
# solution_instance = Solution()
# result = solution_instance.climbStairs(5)  # Replace 5 with the desired value of n
# print(result)

# by using tabulation 

def callstair(n):
   df =[-1] * (n+1)
   df[0]=1
   df[1]=1
   for i in range(2,n+1):
    df[i]=df[i-1]+df[i-2]
   return df[n]

print(callstair(5))
    
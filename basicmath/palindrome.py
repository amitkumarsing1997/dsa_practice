class Solution:
    def isPalindrome(self, x: int) -> bool:
        max_int = 2**31-1
        min_int = -2**31
        b=x
        num=0
        if x < 0:
         return False  
        while(b!=0):
            rem = b % 10
            num = num*10 + rem
            b= b//10 
        else:   
         if (num>max_int or num < min_int):
            return False
         if x==num:
            return True
         else:
            return False
         



class Solution:
    def isPalindrome(self, x: int) -> bool:
        max_int = 2**31-1
        min_int = -2**31
        b=str(x)
        if b[0]=="-":
            return False
            
        else:
            num=int(b[::-1])
        if (num>max_int or num < min_int):
            return False
        if x==num:
            return True
        else:
            return False
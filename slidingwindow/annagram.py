
def sliding_window(A,ann):
    mp = {}
    ans = 0

    # storing the occurence of characters in string p in the dictoonay
    for x in ann:
         mp[x] = mp.get(x,0) + 1
    count =  len(mp)
    k = len(ann)
    i=j=0
    size = len(A)
    while (j < size):
        #  calculation part
        if A[j] in mp:
             mp[A[j]] -= 1
             if mp[A[j]] == 0:
                  count -= 1
        
        windowsize = j -i + 1

        # window length not achieved yet
        if (windowsize < k):
              j = j+1
        # window length achieved, find ans and slide the window
        elif(windowsize == k):
          if count==0: 
            ans += 1
          if A[i] in mp:
            mp[A[i]] += 1
            if mp[A[i]] == 1:
             count += 1
          
          i += 1
          j += 1
    
    return ans
        
                
            
       

A = "abcbcaefdcba"
ann = "abc"


var = sliding_window(A,ann)
print(var)

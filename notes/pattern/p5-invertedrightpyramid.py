def number_pyramid(n):
    for i in range(0,n):
        for j in range(n,i,-1):
         print("*",end=" ")
        print()

number_pyramid(5)
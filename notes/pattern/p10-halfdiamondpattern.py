#  this is different logic of my
def pattern10(N):
    # Outer loop for the number of rows.
    for i in range(1, 2 * N):
        # Stars would be equal to the row no. up till the first half
        stars = i if i <= N else 2 * N - i
        
        # if i <= N:
        #     stars = i
        # else:
        #     stars = 2*N -i
        # For printing the stars in each row.
        for j in range(1, stars + 1):
            print("*", end="")
        
        # As soon as the stars for each iteration are printed, we move to the
        # next row and give a line break, otherwise, all stars
        # would get printed in 1 line.
        print()

# Here, we have taken the value of N as 5.
# We can also take input from the user.
N = 5
pattern10(N)




# # amit logic
# def firsthalf(N):
#     for i in range(N):
#         for j in range(i+1):
#             print("*",end="")
#         print()


# def secondhalf(N):
#     for i in range(N-1):
#         for j in range(N-1,i,-1):
#             print("*",end="")
#         print()


# firsthalf(5)
# secondhalf(5)
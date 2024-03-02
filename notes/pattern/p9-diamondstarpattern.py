def erect_pyramid(N):
    # This is the outer loop which will loop for the rows.
    for i in range(N):
        # For printing the spaces before stars in each row
        for j in range(N - i - 1):
            print(" ", end="")
        
        # For printing the stars in each row
        for j in range(2 * i + 1):
            print("*", end="")
        
        # For printing the spaces after the stars in each row
        for j in range(N - i - 1):
            print(" ", end="")
        
        # As soon as the stars for each iteration are printed, we move to the
        # next row and give a line break, otherwise, all stars
        # would get printed in 1 line.
        print()

def inverted_pyramid(N):
    # This is the outer loop which will loop for the rows.
    for i in range(N):
        # For printing the spaces before stars in each row
        for j in range(i):
            print(" ", end="")
        
        # For printing the stars in each row
        for j in range(2 * N - (2 * i + 1)):
            print("*", end="")
        
        # For printing the spaces after the stars in each row
        for j in range(i):
            print(" ", end="")
        
        # As soon as the stars for each iteration are printed, we move to the
        # next row and give a line break, otherwise, all stars
        # would get printed in 1 line.
        print()

# Here, we have taken the value of N as 5.
# We can also take input from the user.
N = 5
erect_pyramid(N)
inverted_pyramid(N)



# # amit logic
# def firstpart(N):
#     for i in range(N):
        
#         # for printing space
#         for j in range(N-(i+1)):
#             print(" ",end="")
#         # for printing star
#         for j in range(2*i+1):
#             print("*",end="")
#         # for printing rest space
#         for j in range(N-(i+1)):
#             print(" ",end="")
#         print()


# def secondpart(N):
#     for i in range(N):
#         # for printing space
#         for j in range(i):
#             print(" ",end="")
#         # for printing star
#         for j in range(2*N-(2*i+1)):
#             print("*",end="")
#         # for printing rest space
#         print()

# def main(N):
#  firstpart(5)
#  secondpart(5)

# main(5)
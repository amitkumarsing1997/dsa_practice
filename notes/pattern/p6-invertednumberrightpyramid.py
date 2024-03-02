


def pattern6(N):
    # This is the outer loop which will loop for the rows.
    for i in range(N):
        # This is the inner loop which loops for the columns
        # no. of columns = (N - row index) for each line here
        # as we have to print an inverted pyramid.
        # (N-j) will give us the numbers in a row starting from 1 to N-i.
        for j in range(N, i, -1):
            print(N - j + 1, end=" ")

        # As soon as numbers for each iteration are printed, we move to the
        # next row and give a line break otherwise all numbers
        # would get printed in 1 line.
        print()

# Here, we have taken the value of N as 5.
# We can also take input from the user.
N = 5
pattern6(N)



# #  by amit logic
# def inveted_number_right_pyramid(n):
#     for i in range(1,n+1):
#         t=1
#         for j in range(n+1,i,-1):
#             print(t,end=" ")
#             t=t+1
#         print()


# inveted_number_right_pyramid(5)
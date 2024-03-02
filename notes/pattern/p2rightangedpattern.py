def pattern2(N):
    # This is the outer loop which will loop for the rows.
    for i in range(N):
        # This is the inner loop which loops for the columns
        # no. of columns = row number for each line here.
        for j in range(i + 1):
            print("* ", end="")

        # As soon as stars for each iteration are printed, we move to the
        # next row and give a line break otherwise all stars
        # would get printed in 1 line.
        print()

# Example usage with N=5
pattern2(5)

class Main:
    @staticmethod
    def pattern7(N):
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
            
            # As soon as the stars for each iteration are printed,
            # we move to the next row and give a line break.
            print()

    @staticmethod
    def main():
        # Here, we have taken the value of N as 5.
        # We can also take input from the user.
        N = 3
        Main.pattern7(N)

# Call the main method when the script is executed
Main.main()

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
"""
    Asks user for two inputs, converts them to integers, and returns them as x, y.


    PARAMS:
        - user_x: str 1 with whatever the user wants
        - user_y: str 2 with whatever the user wants
    RETURNS:
        - int x: int of whatever str 1 is
        - int y: int of whatever str 2 is
"""
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    user_x=str(input("give me x: "))
    x = int(user_x)
    user_y=str(input("give me y: "))
    y = int(user_y)
    return x, y

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
"""
    Takes int x and int y from the user input and performs various mathematical functions.
    
    int x and int y are first multiplied together. this new number is called num for the numerator
    of our final function. x*y is then printed. int x and int y are then added together. this new
    number is called den for the denominator of our final function. the final function is defined
    by variable ab_multadd, which is then returned.


    PARAMS:
        - num: int x multiplied by int y
        - den: int x added to add y
        - ab_multadd: num/den (a*b)/(a+b)
    RETURNS:
        - ab_multadd: quotient of a*b divided by a+b
"""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    num = a*b
    print(f"mult result: {num}")
    den = a+b
    print(f"add result: {den}")
    ab_multadd = num/den
    return ab_multadd

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
"""
    Prints out various inputs and the results of various mathematical functions.
    
    Creates a string of 16 stars; creates a string of 16 equal signs; prints stars, "RESULTS:", prints
    our int x, int y, the result of ab_multadd, prints equal signs.
    
    PARAMS:
        - stars: str of 16 "*"
        - stripes: str of 16 "="
    RETURNS:
        - ab_multadd: quotient of a*b divided by a+b
"""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    stars = "*"*16
    stripes = "="*16
    print(stars)
    print("RESULTS:")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", ab_multadd)
    print(stripes)
    
def main ():
"""
    Calls the read_two_ints, compute_multadd, and print_fancy functions within the main
    function and assigns them the correct corresponding variables.

    PARAMS:
        - none
    RETURNS:
        - none
"""
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
    x, y=read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd
    ab_multadd=compute_multadd(x, y)

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;
    print_fancy(x, y, ab_multadd)

    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
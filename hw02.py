# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    # ADD a Docstring for this function
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
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    a = 45
    b = 54
    numerator = a*b
    print(f"mult result: {numerator}")
    denominator = a+b
    print(f"add result: {denominator}")
    return (a*b)/(a+b)

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    pass

def main ():
    # ADD a Docstring for this function
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
    read_two_ints()
    x, y=read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    compute_multadd()
    a, b=compute_multadd()


    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    # TODO: add your call instead of this line


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()

# Programmer: Aiden Sterling
# Date: 9/27/21
# Description: Creating an input function that gives the average of three integers.

# The Input
number_1 = int(input("Enter an integer: "))
number_2 = int(input("Enter another integer: "))
number_3 = int(input("Enter one more integer: "))
print(end="\n")

# The Math
average = ((number_1 + number_2 + number_3)/3)

# The Output
print("The average is: ", average, ".", sep="")
# Programmer: Aiden Sterling
# Date: 9/27/21
# Description: Creating an input function that gives the average of three integers.

# The Input
number_1 = int(input("Enter an integer: "))
number_2 = int(input("Enter another integer: "))
number_3 = int(input("Enter one more integer: "))
print()

# The Math
total = (number_1 + number_2 + number_3)
average = (total/3)

# The Output
print(f"The average is: {average}.")
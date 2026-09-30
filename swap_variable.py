# Practice Problem: 
# Write a program to swap the values of two variables, a and b, without using a third temporary variable.
# Given Input: a = 5, b = 10
def swap_variables(a, b):

    a, b = b, a
    print(a)
    print(b)
    
swap_variables(5, 10)



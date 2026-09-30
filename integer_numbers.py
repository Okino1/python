# A Python function that accepts two integer numbers. 
# If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
def two_integer_numbers(number1, number2):
    product = number1 * number2
    total_sum = number1 + number2
    if product <= 1000:
        return f"The result is {product}"
    else:
        return f"The result is {total_sum}"


print(two_integer_number(number1 = int(input("Enter number1:")), number2 = int(input("Enter number2:"))))
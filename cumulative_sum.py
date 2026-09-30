# Iterate through the first 10 numbers (0–9). 
# In each iteration, print the current number, the previous number, and their sum.
def cumulative_sum(numbers):
    previous_number = 0
    for number in numbers:
        if number == 0:
            print(f"Current Number {number} Previous Number {previous_number} Sum: {number + previous_number}")
        else:
            print(f"Current Number {number} Previous Number {previous_number} Sum: {number + previous_number}")
            previous_number += 1
cumulative_sum(range(10))
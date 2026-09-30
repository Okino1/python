# Write a function to remove characters from a string starting from index 0 up to n and return a new string.
# Given Input:

# remove_chars("pynative", 4)
# remove_chars("pynative", 2)
def remove_chars(characters, n):
   character = characters[n:]
   return character

print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

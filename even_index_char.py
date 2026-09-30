# Display only those characters which are present at an even index number in given string.
def even_characters(characters):
    result = characters[::2]

    print(result)

even_characters(input("Enter character: \n"))
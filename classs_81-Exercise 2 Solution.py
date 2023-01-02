# Exercise
# Define is_palindrom funtion that take one word in string as input
# and return True if it is palindrom else return false

def is_palindrom(word):
    return word == word[::-1]
print(is_palindrom("madam"))
print(is_palindrom("horse"))

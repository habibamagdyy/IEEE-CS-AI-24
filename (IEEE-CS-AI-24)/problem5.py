def is_palindrome(word):
    return word == word[::-1]

input_word = input("Enter a word: ")

if is_palindrome(input_word):
    print(f"The word '{input_word}' is a palindrome.")
else:
    print(f"The word '{input_word}' is not a palindrome.")

def stringPalindromeChecker(string_1):
    if string_1[0] == string_1[-1]:
        return "This string is a Palindrome string."
    else:
        return "This string isn't a Palindrome string."

str_input = input("Enter a string to check if it's Palindrome or not: ")
print(stringPalindromeChecker(str_input))

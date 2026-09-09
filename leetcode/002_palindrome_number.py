def isPalindrome(x):
    return str(x) == str(x)[::-1]
print(isPalindrome(121))   # Expected: True
print(isPalindrome(-121))  # Expected: False
print(isPalindrome(10))    # Expected: False
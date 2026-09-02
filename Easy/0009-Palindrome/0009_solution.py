class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Base cases: 
        # Negative numbers are not palindromes.
        # Numbers ending in 0 are not palindromes (unless the number is 0 itself).
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0

        # The loop runs until we reach the middle of the number
        while x > reversed_num:
            # 1. Pop the last digit off of x
            last_digit = x % 10

            # 2. Push it onto the back of reversed_num
            reversed_num = (reversed_num * 10) + last_digit

            # 3. Remove the last digit from x using integer division
            x = x // 10
    
        # Check if it's a palindrome (handles even and odd length numbers)
        return x == reversed_num or x == reversed_num // 10


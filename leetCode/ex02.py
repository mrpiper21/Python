# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        reverse = y[::-1]  # Reverse the string
        if reverse == y:  # Compare the reversed string to the original
            return True
        return False
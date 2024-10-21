class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Helper function to expand around the center
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # return the palindrome found by expanding around the center
            return s[left + 1:right]
        
        # If the string is empty or has 1 character, it's already the longest palindrome
        if len(s) <= 1:
            return s
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            # Odd length palindromes (single character center)
            palindrome1 = expand_around_center(i, i)
            
            # Even length palindromes (two character center)
            palindrome2 = expand_around_center(i, i + 1)
            
            # Update the longest palindrome if a longer one is found
            longest_palindrome = max(longest_palindrome, palindrome1, palindrome2, key=len)
        
        return longest_palindrome


# def longest_palindromic_substring(self,s: str):
#     name = input("enter the name")
#     length = 0
#     left = 0
#     max_length = 0
#     count = 0

#     for i in range(len(s):
#         palindromic1 = expand_   

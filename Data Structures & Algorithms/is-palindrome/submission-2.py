class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(s)-1
        return s == s[::-1]

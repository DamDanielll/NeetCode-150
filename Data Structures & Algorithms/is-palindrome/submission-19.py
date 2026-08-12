class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = "".join(char for char in s if char.isalnum()).lower()
        left = 0
        right = len(ns) - 1
        while left < right:
            if ns[left] == ns[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
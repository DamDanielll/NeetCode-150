class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = {}
        td = {}
        for char in s:
            if char in sd:
                sd[char] += 1
            else:
                sd[char] = 1
        for char in t:
            if char in td:
                td[char] += 1
            else:
                td[char] = 1
        if td == sd:
            return True
        else:
            return False

            

    



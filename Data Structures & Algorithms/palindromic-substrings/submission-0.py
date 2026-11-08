class Solution:
    def countSubstrings(self, s: str) -> int:
        number_of_pali = 0
        for i in range(len(s)):
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                number_of_pali += 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                number_of_pali += 1
                l -= 1
                r += 1
        return number_of_pali
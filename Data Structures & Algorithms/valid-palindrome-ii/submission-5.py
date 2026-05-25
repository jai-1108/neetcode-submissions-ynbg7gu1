class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1

        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return self.palindrome(s,l+1,r) or self.palindrome(s,l,r-1)
        return True

    def palindrome(self,s,l,r):
        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
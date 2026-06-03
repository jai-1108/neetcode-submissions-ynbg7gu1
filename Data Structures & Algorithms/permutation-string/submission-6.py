class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counts1 = [0]*26
        counts2 = [0]*26
        for c in s1:
            counts1[ord(c) - ord("a")] += 1
        l = 0
        r = 0
        while l<=r and r<len(s2):
            counts2[ord(s2[r]) - ord("a")] += 1
            while r-l+1 == len(s1):
                if counts1 == counts2:
                    return True
                else:
                    counts2[ord(s2[l]) - ord("a")] -= 1
                    l += 1
            r+=1
        return False


            

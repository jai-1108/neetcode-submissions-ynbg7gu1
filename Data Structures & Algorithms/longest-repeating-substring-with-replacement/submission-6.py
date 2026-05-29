class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Count = {A:4, B:3}

        """
        l = 0
        r = 0
        longest = 0
        count = {}
        maxF = 0
        while r<len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            length = r-l+1
            while length - maxF > k:
                count[s[l]] -= 1
                l += 1
                length = r-l+1
            r += 1
            longest = max(length,longest)
        return longest


                
                
            

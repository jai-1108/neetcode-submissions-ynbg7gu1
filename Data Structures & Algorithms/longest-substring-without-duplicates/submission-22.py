class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        length = 0
        window = set()
        for r in range(len(s)):

            if s[r] in window:
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
            window.add(s[r])
            length = r-l+1
            longest = max(length, longest)
        return longest
            
                
    
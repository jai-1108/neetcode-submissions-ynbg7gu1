class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        countS1 = {a:1, b:1, c:1}
        window_size = len(s1)
        current_window_length = r - l + 1 
        l = 0
        r = 0 
        countS2 = {l:1}
        r = 1
        countS2 = {l:1, e:1}
        r = 2
        countS2 = {l:1, e:1, c:1}
        if curent_window_length = window_size:
         if countS1 == countS2:
            return True
         countS2[s2[l]] -= 1
         l += 1
         countS2 = {e:1, c:1}
        r = 3
        countS2 = {e:1, c:1, a:1, l:0}
        countS2 = {c:1, a:1}
        r = 4
        countS2 = {c:1, a:1, b:1}
        True

        return False 



        """
        if len(s1) > len(s2):
            return False
        countS1 = [0]*26
        countS2 = [0]*26
        max_window_length = len(s1)
        for c in s1:
            countS1[ord(c) - ord("a")] += 1
        l = 0
        r = 0
        while l<=r and r<len(s2):
            current_window_length = r - l + 1
            countS2[ord(s2[r]) - ord("a")] += 1
            if current_window_length == max_window_length:
                if countS1 == countS2:
                    return True
                countS2[ord(s2[l]) - ord("a")] -= 1
                l += 1
            r+=1
        return False



        

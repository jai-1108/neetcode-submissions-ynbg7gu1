class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
    
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        return self.merge(left_half, right_half)
            
    def merge(self, a1, a2):
        res = []
        i, j = 0, 0 
        while i < len(a1) and j < len(a2):
            if a1[i] < a2[j]:
                res.append(a1[i])
                i += 1
            else:
                res.append(a2[j])
                j += 1
                
        res.extend(a1[i:])
        res.extend(a2[j:])
        
        return res
        
                
        
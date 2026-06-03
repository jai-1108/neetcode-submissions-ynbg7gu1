class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        stack = []
        hashmap = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack and c in hashmap.keys():
                    return False
                if stack and stack[-1] != hashmap[c]:
                    return False
                else:
                    stack.pop()
            
        return True if not stack else False
                    
        
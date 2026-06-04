class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        stack = []
        1, stack.append(1), stack = [1]
        2, stack.append(2), stack = [1,2]
        +, a = stack.pop(2), b = stack.pop(1), stack.append(a+b), stack = [3]
        3, stack = [3,3]
        *, a = stack.pop(3), b = stack.pop(3), stack.append(a*b), stack = [9]
        4, stack = [9,4]
        -, a = stack.pop(4), b = stack.pop(9), stack.append(b-a), stack.append(9-4)
        stack = [5]
        return stack[-1]
        """
        stack = []
        for c in tokens:
            if c == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif c == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif c == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif c == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(c))
        return stack[-1] 
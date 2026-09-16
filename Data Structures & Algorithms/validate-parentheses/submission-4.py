class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] #list
        pairs = { ")" : "(", 
                  "}" : "{",
                  "]" : "[" }

        if len(s) < 2:
            return False

        for i in s:
            if i in pairs:
                if not stack or stack[-1] != pairs.get(i):
                    return False
                else: 
                    stack.pop()
            else:
                stack.append(i)
        return not stack

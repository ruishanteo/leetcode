class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pair = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for char in s:
            if (char == '(' or char == '[' or char == '{'):
                stack.append(char)
            if (char == ')' or char == ']' or char == '}'):
                if (len(stack) == 0):
                    return False
                elif (stack.pop() != pair[char]):
                    return False
                else:
                    continue
        if not stack:
            return True
        else:
            return False
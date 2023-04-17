# https://leetcode.cn/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        length = len(s)
        
        stack = []

        l = 0
        max_l = 0
        for c in s:

            if c == '(':
                stack.append(c)
                
            if c == ')' and stack != []:
                stack.pop()
                l += 2
                
            elif c == ')' and stack == []:
                max_l = max(max_l, l)
                l = 0
                
        max_l =  max(l, max_l)
        
        stack = []
        r = 0
        max_r = 0
        for i in range(len(s)):
            c = s[length - i -1]

            if c == ')':
                stack.append(c)
                
            if c == '(' and stack != []:
                stack.pop()
                r += 2
                
            elif c == '(' and stack == []:
                max_r = max(max_r, r)
                r = 0
                
        max_r =  max(r, max_r)
        print(max_l, max_r)
        
        return min(max_r, max_l)
    
x = Solution()

print(x.longestValidParentheses("))))())()()(()"))
                
            
            
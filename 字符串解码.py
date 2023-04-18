# https://leetcode.cn/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        # idea: use recursion
        
        # use stack to remember the index of [ and ]
        stack = []
        result = ''
        for i, c in enumerate(s):
            if c == '[':
                stack.append(i)
                continue
            
            if c == ']':
                j = stack.pop()
                
                if not stack:
                    # search for the number
                    k = j-1
                    while s[k].isdigit():
                        k -= 1
                    
                    result += int(s[k+1:j]) * self.decodeString(s[j+1:i])
                continue
            
            if not stack and not c.isdigit():
                result += c
                
        return result
    
                
            
x = Solution()

print(x.decodeString('2[a2[c]]'))
            
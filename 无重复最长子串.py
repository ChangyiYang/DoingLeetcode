# https://leetcode.cn/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        # characters = set(s)
        
        taken_substring = list()
        i = 0
        
        size = 0
        max_size = 0
        
        while i < len(s):
            if s[i] in taken_substring:
                index = taken_substring.index(s[i])
                taken_substring = taken_substring[ index+1:]
                size -= index + 1
                
            taken_substring.append(s[i])
            size += 1
            if (size > max_size):
                max_size = size
            
            i+=1    
            
        return max_size
    
x = Solution()

print(x.lengthOfLongestSubstring('1223'))
        
        
        

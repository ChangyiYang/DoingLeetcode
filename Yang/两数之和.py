# https://leetcode.cn/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        
        # first, subtract target/2 from the list
        length = len(nums)
        new_nums = [x - target/2 for x in nums]
        
        # Then, in the new list, two aimed number will be negative to each other
        
        for i in range(length-1):
            number = new_nums[i]
            
            
            # if the negative is not in the rest of 
            if (-number) not in new_nums[i+1:length]:
                continue
            
            for j in range(i+1, length):
                if new_nums[j] == -number:
                    return [i,j]
                
                
x = Solution()
print(x.twoSum([1,2,3],3))
                
                

                
                
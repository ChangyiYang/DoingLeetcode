# https://leetcode.cn/problems/first-missing-positive/submissions/
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        
        # 写一下那个置换形式
        # 我只能说，最关键的点是看出只有【1，N】的数有重要
        
        N = len(nums)
        for i,num in enumerate(nums):
            
            while 1<= num <= N and num != nums[num -1] :
                nums[i], nums[num -1] = nums[num -1], nums[i]
                num = nums[i]
                
        for i in range(N):
            if nums[i] != i+1:
                return i + 1
            
        return N + 1
            
        
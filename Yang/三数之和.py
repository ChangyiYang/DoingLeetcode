# https://leetcode.cn/problems/3sum/


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        

        # sort takes O(nlog(n)), which is quite small
        nums = sorted(nums)
        n = len(nums)
        result = []

        print(nums)

        for i, x_i in enumerate(nums):

            left = i+1
            right = n-1
            aim = -x_i

            while left < right:
                
                if left == i or nums[left] == nums[left-1]:
                    left += 1
                    continue
                    
                if right == i :
                    right -= 1
                    continue
                
                if right != n-1 and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                

                if nums[left] + nums[right] < aim:
                    left += 1
                    continue

                if nums[left] + nums[right] > aim:
                    right -= 1
                    continue
                
                if nums[left] + nums[right] == aim:
                    print(i,left,right)
                    result.append([x_i, nums[left], nums[right]])
                    left += 1
                    continue

        return result
                    
                


x = Solution()

print(x.threeSum([-1,0,1,2,-1,-4]))


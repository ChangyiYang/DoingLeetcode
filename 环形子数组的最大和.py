#  https://leetcode.cn/problems/maximum-sum-circular-subarray/


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:


        # nums = nums + nums[:]
        f_max = nums[0]

        result_max = nums[0]

        f_min = nums[0]
        result_min = nums[0]

        # Using DP to calculate the max subarray and min subarray

        for i in range(1,len(nums)):

            f_max = max( f_max + nums[i], nums[i])
            result_max = max(f_max,result_max)

            f_min = min(f_min + nums[i], nums[i])
            result_min = min(f_min,result_min)

        
        if result_max < 0:
            return result_max

        return max(result_max, sum(nums) - result_min)


x = Solution()

print(x.maxSubarraySumCircular([5,-3,5]))

